from __future__ import absolute_import
import time
import struct
import operator

from .api import BlueGigaAPI, BlueGigaCallbacks
from .cmd_def import gap_discoverable_mode, gap_connectable_mode, gap_discover_mode, \
    connection_status_mask, sm_io_capability
from threading import Event
import logging
import sys

GET_ADDRESS = "Read Address in Progress"
PROCEDURE = "Procedure in Progress"
START_ENCRYPTION = "Start Encryption in Progress"
READ_ATTRIBUTE = "Attribute Read in Progress"
CONNECT = "Connection Attempt in Progress"
DISCONNECT = "Disconnect in Progress"
CONN_PARAM_UPDATE = "Connection Parameter Update Expected"

class BlueGigaModuleException(Exception):
    pass


class BLEScanResponse(object):
    def __init__(self, rssi, packet_type, sender, address_type, bond, data):
        self.rssi = rssi
        self.packet_type = packet_type
        self.sender = sender
        self.address_type = address_type
        self.bond = bond
        self.data = data
        self.services = []
        self.adv_payload = []
        self.created = time.time()

    def get_sender_address(self):
        return self.sender

    def parse_advertisement_data(self):
        remaining = self.data
        while len(remaining) > 0:
            length, = struct.unpack('B', remaining[:1])
            gap_data = remaining[1:length+1]

            adv_seg={}
            adv_seg_type, = struct.unpack('B', gap_data[:1])
            adv_seg["Type"] = self.get_ad_type_string(adv_seg_type)
            adv_seg["Data"] = gap_data[1:]
            self.adv_payload.append( adv_seg)
            #print("GAP Data: %s" % ("".join(["\\x%02x" % ord(i) for i in gap_data])))
            remaining = remaining[length+1:]

            if adv_seg_type == 0x1:  # Flags
                pass
            elif adv_seg_type == 0x02 or adv_seg_type == 0x03:  # Incomplete/Complete list of 16-bit UUIDs
                for i in range(1, len(gap_data) - 1, 2):
                    self.services += [gap_data[i:i+2]]
            elif adv_seg_type == 0x04 or adv_seg_type == 0x05:  # Incomplete list of 32-bit UUIDs
                for i in range(1, len(gap_data) - 3, 4):
                    self.services += [gap_data[i:i+4]]
            elif adv_seg_type == 0x06 or adv_seg_type == 0x07:  # Incomplete list of 128-bit UUIDs
                for i in range(1, len(gap_data) - 15, 16):
                    self.services += [gap_data[i:i+16]]

    def get_services(self):
        self.parse_advertisement_data()
        return self.services

    def get_ad_type_string(self, type_ord):
        return {
            0x01: "BLE_GAP_AD_TYPE_FLAGS",
            0x02: "BLE_GAP_AD_TYPE_16BIT_SERVICE_UUID_MORE_AVAILABLE",
            0x03: "BLE_GAP_AD_TYPE_16BIT_SERVICE_UUID_COMPLETE",
            0x04: "BLE_GAP_AD_TYPE_32BIT_SERVICE_UUID_MORE_AVAILABLE",
            0x05: "BLE_GAP_AD_TYPE_32BIT_SERVICE_UUID_COMPLETE",
            0x06: "BLE_GAP_AD_TYPE_128BIT_SERVICE_UUID_MORE_AVAILABLE",
            0x07: "BLE_GAP_AD_TYPE_128BIT_SERVICE_UUID_COMPLETE",
            0x08: "BLE_GAP_AD_TYPE_SHORT_LOCAL_NAME",
            0x09: "BLE_GAP_AD_TYPE_COMPLETE_LOCAL_NAME",
            0x0A: "BLE_GAP_AD_TYPE_TX_POWER_LEVEL",
            0x0D: "BLE_GAP_AD_TYPE_CLASS_OF_DEVICE",
            0x0E: "BLE_GAP_AD_TYPE_SIMPLE_PAIRING_HASH_C",
            0x0F: "BLE_GAP_AD_TYPE_SIMPLE_PAIRING_RANDOMIZER_R",
            0x10: "BLE_GAP_AD_TYPE_SECURITY_MANAGER_TK_VALUE",
            0x11: "BLE_GAP_AD_TYPE_SECURITY_MANAGER_OOB_FLAGS",
            0x12: "BLE_GAP_AD_TYPE_SLAVE_CONNECTION_INTERVAL_RANGE",
            0x14: "BLE_GAP_AD_TYPE_SOLICITED_SERVICE_UUIDS_16BIT",
            0x15: "BLE_GAP_AD_TYPE_SOLICITED_SERVICE_UUIDS_128BIT",
            0x16: "BLE_GAP_AD_TYPE_SERVICE_DATA",
            0x17: "BLE_GAP_AD_TYPE_PUBLIC_TARGET_ADDRESS",
            0x18: "BLE_GAP_AD_TYPE_RANDOM_TARGET_ADDRESS",
            0x19: "BLE_GAP_AD_TYPE_APPEARANCE",
            0x1A: "BLE_GAP_AD_TYPE_ADVERTISING_INTERVAL",
            0x1B: "BLE_GAP_AD_TYPE_LE_BLUETOOTH_DEVICE_ADDRESS",
            0x1C: "BLE_GAP_AD_TYPE_LE_ROLE",
            0x1D: "BLE_GAP_AD_TYPE_SIMPLE_PAIRING_HASH_C256",
            0x1E: "BLE_GAP_AD_TYPE_SIMPLE_PAIRING_RANDOMIZER_R256",
            0x20: "BLE_GAP_AD_TYPE_SERVICE_DATA_32BIT_UUID",
            0x21: "BLE_GAP_AD_TYPE_SERVICE_DATA_128BIT_UUID",
            0x3D: "BLE_GAP_AD_TYPE_3D_INFORMATION_DATA",
            0xFF: "BLE_GAP_AD_TYPE_MANUFACTURER_SPECIFIC_DATA"
        }[type_ord]


class GATTCharacteristicDescriptor(object):
    def __init__(self, handle, value):
        self.handle = handle
        self.value = value


class GATTService(object):
    PRIMARY_SERVICE_UUID = b"\x00\x28"  # [0x00, 0x28]
    SECONDARY_SERVICE_UUID = b"\x01\x28"  # [0x01, 0x28]

    def __init__(self, start_handle, end_handle, uuid):
        self.start_handle = start_handle
        self.end_handle = end_handle
        self.uuid = uuid


class GATTCharacteristic(object):
    CHARACTERISTIC_UUID = b"\x03\x28"
    CLIENT_CHARACTERISTIC_CONFIG = b"\x02\x29"
    USER_DESCRIPTION = b"\x01\x29"

    def __init__(self, handle, properties):
        self.handle = handle
        self.properties, self.value_handle = struct.unpack("<BH", properties[:3])
        self.uuid = properties[3:]
        self.descriptors = {}
        self.value = None

    def is_readable(self):
        return (self.properties & 0x02) > 0

    def is_write_no_response(self):
        return (self.properties & 0x04) > 0

    def is_writable(self):
        return (self.properties & 0x08) > 0

    def has_notify(self):
        return (self.properties & 0x10) > 0

    def has_indicate(self):
        return (self.properties & 0x20) > 0

    def has_reliable_write(self):
        return (self.properties & 0x80) > 0

    def add_descriptor(self, uuid, handle, value):
        if uuid == self.uuid:
            self.value = value
        else:
            self.descriptors[uuid] = GATTCharacteristicDescriptor(handle, value)

    def get_descriptor_by_uuid(self, uuid):
        if uuid not in self.descriptors:
            return None
        else:
            return self.descriptors[uuid]


class ProcedureManager(object):
    def __init__(self):
        self._event = Event()
        self._procedure_type = False
        self._procedure_result = 0

    def start_procedure(self, procedure_type):
        self._procedure_type = procedure_type
        self._procedure_result = 0x0000
        self._event.clear()

    def wait_for_procedure(self, timeout=3):
        return self._event.wait(timeout)

    def procedure_complete(self, procedure_type, result=0x0000):
        self._procedure_result = result
        if self._procedure_type == procedure_type:
            self._event.set()


class BLEConnection(ProcedureManager):
    def __init__(self, api, handle, address, address_type, interval, timeout, latency, bonding):
        super(BLEConnection, self).__init__()
        self._api = api
        self.handle = handle
        self.address = address
        self.address_type = address_type
        self.interval = interval
        self.timeout = timeout
        self.latency = latency
        self.bond_handle = bonding
        self.services = {}
        self.characteristics = {}
        self.handle_uuid = {}
        self.uuid_handle = {}
        self.handle_value = {}
        self.attrclient_value_cb = {}

    def get_conn_interval_ms(self):
        return self.interval * 1.25

    def get_timeout_ms(self):
        return self.timeout * 10

    def assign_attrclient_value_callback(self, handle, callback):
        self.attrclient_value_cb[handle] = callback

    def get_connected_address(self):
        return self.address

    def update_service(self, start_handle, end_handle, uuid):
        self.services[start_handle] = GATTService(start_handle, end_handle, uuid)

    def get_services(self):
        return [j for i, j in sorted(self.services.items(), key=operator.itemgetter(0))]

    def get_characteristics(self):
        return [j for i, j in sorted(self.characteristics.items(), key=operator.itemgetter(0))]

    def update_uuid(self, handle, uuid):
        self.handle_uuid[handle] = uuid
        if uuid in self.uuid_handle:
            self.uuid_handle[uuid] += [handle]
        else:
            self.uuid_handle[uuid] = [handle]

    def get_handles_by_uuid(self, uuid):
        if uuid in self.uuid_handle:
            return self.uuid_handle[uuid]

    def get_uuid_by_handle(self, handle):
        if handle in self.handle_uuid:
            return self.handle_uuid[handle]

    def update_handle(self, handle, value):
        if handle in self.handle_uuid:
            if self.handle_uuid[handle] == GATTCharacteristic.CHARACTERISTIC_UUID:
                self.characteristics[handle] = GATTCharacteristic(handle, value)
            else:
                for characteristic in self.get_characteristics()[::-1]:
                    if characteristic.handle < handle:
                        characteristic.add_descriptor(self.handle_uuid[handle], handle, value)
                        break
        else:
            raise BlueGigaModuleException("Attribute Value for Handle %d received with unknown UUID!" % (handle))
        if handle in self.attrclient_value_cb:
            self.attrclient_value_cb[handle](value)

    def read_by_group_type(self, group_type, timeout=3):
        self.start_procedure(PROCEDURE)
        self._api.ble_cmd_attclient_read_by_group_type(self.handle, 1, 65535, group_type)
        if not self.wait_for_procedure(timeout=timeout):
            raise BlueGigaModuleException("Read By Group procedure did not complete before timeout!")

    def read_by_type(self, service, type, timeout=3):
        self.start_procedure(PROCEDURE)
        self._api.ble_cmd_attclient_read_by_type(self.handle, service.start_handle, service.end_handle, type)
        if not self.wait_for_procedure(timeout=timeout):
            raise BlueGigaModuleException("Read By Type procedure did not complete before timeout!")

    def find_information(self, service, timeout=5):
        self.start_procedure(PROCEDURE)
        self._api.ble_cmd_attclient_find_information(self.handle, service.start_handle, service.end_handle)
        if not self.wait_for_procedure(timeout=timeout):
            raise BlueGigaModuleException("Find Information did not complete before timeout!")

    def read_by_handle(self, handle, timeout=3):
        self.start_procedure(READ_ATTRIBUTE)
        self._api.ble_cmd_attclient_read_by_handle(self.handle, handle)
        if not self.wait_for_procedure(timeout=timeout):
            raise BlueGigaModuleException("Read Attribute by Handle did not complete before timeout!")

    def write_by_uuid(self, uuid, value, timeout=3):
        for handle in self.uuid_handle[uuid]:
            self.write_by_handle(handle, value, timeout)

    def write_by_handle(self, handle, value, timeout=3):
        self.start_procedure(PROCEDURE)
        self._api.ble_cmd_attclient_attribute_write(self.handle, handle, value)
        if not self.wait_for_procedure(timeout=timeout):
            raise BlueGigaModuleException("Write did not complete before timeout! Connection:%d - Handle:%d" % self.handle, handle)

    def wr_noresp_by_uuid(self, uuid, value, timeout=3):
        for handle in self.uuid_handle[uuid]:
            self.wr_noresp_by_handle(handle, value, timeout)

    def wr_noresp_by_handle(self, handle, value, timeout=3, attempts=1):
        for i in range(attempts):
            self.start_procedure(PROCEDURE)
            self._api.ble_cmd_attclient_write_command(self.handle, handle, value)
            if not self.wait_for_procedure(timeout=timeout):
                raise BlueGigaModuleException("Write without response did not complete before timeout! Connection:%d - Handle:%d" % (self.handle, handle))
            if self._procedure_result != 0x0000:
                time.sleep(self.interval * 0.00125)  # Sleep for a connection interval
            else:
                break

    def read_long_by_uuid(self, uuid, timeout=3):
        for handle in self.uuid_handle[uuid]:
            self.read_long_by_handle(self.uuid_handle[uuid])

    def read_long_by_handle(self, handle, timeout=3):
        self.start_procedure(PROCEDURE)
        self._api.ble_cmd_attclient_read_long(self.handle, handle)
        if not self.wait_for_procedure(timeout=timeout):
            raise BlueGigaModuleException("Long Read did not complete before timeout! Connection:%d - Handle:%d" % self.handle, handle)

    def reliable_write_by_uuid(self, uuid, value, offset=0, timeout=3):
        for handle in self.uuid_handle[uuid]:
            self.reliable_write_by_handle(handle, value, offset, timeout)

    def reliable_write_by_handle(self, handle, value, offset=0, timeout=3):
        for i in range((len(value) / 20)+1):
            chunk = value[20*i+offset:min(20*(i+1)+offset, len(value))]
            self.start_procedure(PROCEDURE)
            self._api.ble_cmd_attclient_prepare_write(self.handle, handle, 20*i+offset, chunk)
            self.wait_for_procedure(timeout=timeout)
        self.start_procedure(PROCEDURE)
        self._api.ble_cmd_attclient_execute_write(self.handle, 1) # 1 = commit, 0 = cancel
        self.wait_for_procedure(timeout=timeout)

    def characteristic_subscription(self, characteristic, indicate=True, notify=True):
        descriptor = characteristic.get_descriptor_by_uuid(GATTCharacteristic.CLIENT_CHARACTERISTIC_CONFIG)
        if not descriptor:
            raise BlueGigaModuleException("Unable to find Client Characteristic Config (must Read by Type 0x2902)")
        config = struct.pack('BB', (2 if indicate else 0) + (1 if notify else 0), 0)
        self.write_by_handle(descriptor.handle, config, timeout=1)

    def request_encryption(self, bond=True, timeout=1):
        self.start_procedure(START_ENCRYPTION)
        self._api.ble_cmd_sm_encrypt_start(self.handle, 1 if bond else 0)
        if not self.wait_for_procedure(timeout=timeout):
            raise BlueGigaModuleException("Start Encryption did not complete before timeout!")


class BlueGigaModule(BlueGigaCallbacks, ProcedureManager):
    CONNECTION_OBJECT = BLEConnection

    def __init__(self, port, baud=115200, timeout=0.1):
        super(BlueGigaModule, self).__init__()
        self._api = BlueGigaAPI(port, callbacks=self, baud=baud, timeout=timeout)
        self.address = None
        self._module_info = None
        self.scan_responses = None
        self.connections = {}
        self._api.start_daemon()
        self.procedure_in_progress = False

    def pipe_logs_to_terminal(self, level=logging.INFO):
        term = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(self._api._serial.portstr + ': %(asctime)s - %(name)s - %(levelname)s - %(message)s')
        term.setFormatter(formatter)
        api_logger = logging.getLogger("bgapi")
        api_logger.addHandler(term)
        api_logger.setLevel(level=level)

    def shutdown(self):
        self._api.stop_daemon()

    def get_module_info(self, timeout=0.5):
        start = time.time()
        if not self._module_info:
            self._api.ble_cmd_system_get_info()
        while not self._module_info and time.time() < start + timeout:
            pass
        return self._module_info

    def get_ble_address(self, timeout=1):
        self.start_procedure(GET_ADDRESS)
        self._api.ble_cmd_system_address_get()
        if not self.wait_for_procedure(timeout=timeout):
            raise BlueGigaModuleException("No response to get_ble_address!")
        else:
            return self.address

    def reset_ble_state(self):
        """ Disconnect, End Procedure, and Disable Advertising """
        self._api.ble_cmd_gap_set_mode(gap_discoverable_mode['gap_non_discoverable'],
                                       gap_connectable_mode['gap_non_connectable'])
        for i in range(8):
            self.disconnect(i)
        self._api.ble_cmd_gap_end_procedure()

    def disconnect(self, connection):
        self.start_procedure(DISCONNECT)
        try:
            self._api.ble_cmd_connection_disconnect(connection=connection.handle)
        except AttributeError:
            self._api.ble_cmd_connection_disconnect(connection=connection)
        self.wait_for_procedure()

    def allow_bonding(self):
        self._api.ble_cmd_sm_set_bondable_mode(1)

    def disallow_bonding(self):
        self._api.ble_cmd_sm_set_bondable_mode(0)

    def delete_bonding(self):
        self._api.ble_cmd_sm_delete_bonding(0)

    def set_device_capabilities(self, mitm=True, keysize=16, io=sm_io_capability['sm_io_capability_noinputnooutput']):
        self._api.ble_cmd_sm_set_parameters(mitm=1 if mitm else 0, min_key_size=keysize, io_capabilities=io)

    def set_out_of_band_data(self, oob):
        self._api.ble_cmd_sm_set_oob_data(oob.decode("hex"))

#------------- Response and Event Callbacks  -------------#

    def ble_rsp_system_address_get(self, address):
        super(BlueGigaModule, self).ble_rsp_system_address_get(address)
        self.address = address
        self.procedure_complete(GET_ADDRESS)

    def ble_evt_connection_status(self, connection, flags, address, address_type, conn_interval, timeout, latency, bonding):
        super(BlueGigaModule, self).ble_evt_connection_status(connection, flags, address, address_type, conn_interval, timeout, latency, bonding)
        if flags & connection_status_mask['connection_completed']:
            conn = self.CONNECTION_OBJECT(api=self._api, handle=connection, address=address,
                                          address_type=address_type, interval=conn_interval, timeout=timeout,
                                          latency=latency, bonding=bonding)
            self.connections[connection] = conn
            self.most_recent_connection = conn
            self.procedure_complete(CONNECT)
        if flags & connection_status_mask['connection_parameters_change']:
            self.connections[connection].flags = flags
            self.connections[connection].interval = conn_interval
            self.connections[connection].timeout = timeout
            self.connections[connection].latency = latency
            self.connections[connection].procedure_complete(CONN_PARAM_UPDATE)
        if flags & connection_status_mask['connection_encrypted']:
            self.connections[connection].flags = flags
            self.connections[connection].procedure_complete(START_ENCRYPTION)

    def ble_rsp_system_get_info(self, major, minor, patch, build, ll_version, protocol_version, hw):
        super(BlueGigaModule, self).ble_rsp_system_get_info(major, minor, patch, build, ll_version, protocol_version, hw)
        self._module_info = {"FW Version": "%d.%d.%d.%d" % (major, minor, patch, build),
                             "Link Layer Version": "%d" % ll_version,
                             "Protocol Version": "%d" % protocol_version,
                             "Hardware Version": "%d" % hw}

    def ble_rsp_connection_disconnect(self, connection, result):
        super(BlueGigaModule, self).ble_rsp_connection_disconnect(connection, result)
        if result == 0x0186: # Not Connected
            self.procedure_complete(DISCONNECT, result=result)

    def ble_evt_connection_disconnected(self, connection, reason):
        super(BlueGigaModule, self).ble_evt_connection_disconnected(connection, reason)
        self.procedure_complete(DISCONNECT, result=reason)


class BlueGigaClient(BlueGigaModule):
    def connect_by_adv_data(self, adv_data, scan_timeout=3, conn_interval_min=0x20, conn_interval_max=0x30, connection_timeout=100, latency=0):
        responses = self.scan_all(timeout=scan_timeout)
        for resp in responses:
            if adv_data in resp.data:
                return self.connect(resp, scan_timeout, conn_interval_min, conn_interval_max, connection_timeout, latency)
        else:
            raise BlueGigaModuleException("%s not found in BLE scan!" % (adv_data))

    def scan_limited(self, timeout=20):
        return self._scan(mode=gap_discover_mode['gap_discover_limited'], timeout=timeout)

    def scan_general(self, timeout=20):
        return self._scan(mode=gap_discover_mode['gap_discover_generic'], timeout=timeout)

    def scan_all(self, timeout=20):
        return self._scan(mode=gap_discover_mode['gap_discover_observation'], timeout=timeout)

    def active_scan(self, scan_interval = 0x4B, scan_window = 0x32):
        return self._api.ble_cmd_gap_set_scan_parameters(scan_interval, scan_window, 1)

    def disable_scan(self, scan_interval = 0x4B, scan_window = 0x32):
        return self._api.ble_cmd_gap_set_scan_parameters(scan_interval, scan_window, 0)

    def connect(self, target, timeout=5, conn_interval_min=0x20, conn_interval_max=0x30, connection_timeout=100, latency=0):
        self.start_procedure(CONNECT)
        self._api.ble_cmd_gap_connect_direct(address=target.sender,
                                             addr_type=target.address_type,
                                             conn_interval_min=conn_interval_min,
                                             conn_interval_max=conn_interval_max,
                                             timeout=connection_timeout,
                                             latency=latency)
        if not self.wait_for_procedure(timeout=timeout):
            raise BlueGigaModuleException("Connection attempt unsuccessful! (%s)" % target.get_sender_address())
        return self.most_recent_connection

    def _scan(self, mode, timeout):
        self.scan_responses = None
        now = start = time.time()
        self._api.ble_cmd_gap_discover(mode=mode)
        while now < start + timeout:
            time.sleep(timeout - (now - start))
            now = time.time()
        self._api.ble_cmd_gap_end_procedure()
        return self.scan_responses

    def ble_rsp_attclient_write_command(self, connection, result):
        super(BlueGigaClient, self).ble_rsp_attclient_write_command(connection=connection, result=result)
        self.procedure_complete(PROCEDURE, result=result)
        self.connections[connection].procedure_complete(PROCEDURE, result=result)

    #----------------  Events triggered by incoming data ------------------#

    def ble_evt_gap_scan_response(self, rssi, packet_type, sender, address_type, bond, data):
        super(BlueGigaModule, self).ble_evt_gap_scan_response(rssi, packet_type, sender, address_type, bond, data)
        if not self.scan_responses:
            self.scan_responses = []
        self.scan_responses += [ BLEScanResponse(rssi, packet_type, sender, address_type, bond, data) ]

    def ble_evt_attclient_find_information_found(self, connection, chrhandle, uuid):
        super(BlueGigaModule, self).ble_evt_attclient_find_information_found(connection, chrhandle, uuid)
        self.connections[connection].update_uuid(chrhandle, uuid)

    def ble_evt_attclient_attribute_value(self, connection, atthandle, type, value):
        super(BlueGigaModule, self).ble_evt_attclient_attribute_value(connection, atthandle, type, value)
        if connection in self.connections:
            self.connections[connection].update_handle(atthandle, value)
            self.connections[connection].procedure_complete(READ_ATTRIBUTE)

    def ble_evt_attclient_group_found(self, connection, start, end, uuid):
        super(BlueGigaModule, self).ble_evt_attclient_group_found(connection, start, end, uuid)
        self.connections[connection].update_service(start, end, uuid)

    def ble_evt_attclient_procedure_completed(self, connection, result, chrhandle):
        super(BlueGigaModule, self).ble_evt_attclient_procedure_completed(connection, result, chrhandle)
        self.procedure_complete(PROCEDURE, result=result)
        self.connections[connection].procedure_complete(PROCEDURE, result=result)
        self.connections[connection].procedure_complete(READ_ATTRIBUTE, result=result) # When the attribute read fails


class BlueGigaServer(BlueGigaModule):
    def __init__(self, port, baud=115200, timeout=0.1):
        super(BlueGigaServer, self).__init__(port, baud, timeout)
        self.handle_types = {}
        self.handle_values = {}

    def start_advertisement(self, adv_mode, conn_mode, interval_min=1000, interval_max=1500, channels=0x07):
        self._api.ble_cmd_gap_set_adv_parameters(interval_min, interval_max, channels)
        self._api.ble_cmd_gap_set_mode(discover=adv_mode, connect=conn_mode)

    def advertise_general(self, interval_min=500, interval_max=1000, channels=0x7):
        self.start_advertisement(adv_mode=gap_discoverable_mode['gap_general_discoverable'],
                         conn_mode=gap_connectable_mode['gap_undirected_connectable'],
                         interval_min=interval_min,
                         interval_max=interval_max,
                         channels=channels)

    def setup_ibeacon(self, uuid, major, minor):
        advertisement_data = "020106"       # General discovery, Single Mode Device
        advertisement_data += "1AFF"        # Manufacturer Data
        advertisement_data += "4C000215"    # Preamble
        advertisement_data += uuid.replace('-',"")
        advertisement_data += "%04x%04x" % (major, minor)
        advertisement_data += "DC"          # Measured RSSI at 1m
        advertisement_data = advertisement_data.decode("hex") # LE byte list
        self._api.ble_cmd_gap_set_adv_data(0, adv_data=advertisement_data)

    def setup_physical_web(self, uri):
        encodings = [("http://www.", "\x00"),
                     ("https://www.", "\x01"),
                     ("http://", "\x02"),
                     ("https://", "\x03"),
                     (".com/", '\x00'),
                     (".org/", '\x01'),
                     (".edu/", '\x02'),
                     (".net/", '\x03'),
                     (".info/", '\x04'),
                     (".biz/", '\x05'),
                     (".gov/", '\x06'),
                     (".com", '\x07'),
                     (".org", '\x08'),
                     (".edu", '\x09'),
                     (".net", '\x0A'),
                     (".info", '\x0B'),
                     (".biz", '\x0C'),
                     (".gov", '\x0D'),]
        encoded_uri = uri
        for enc in encodings:
            encoded_uri = encoded_uri.replace(enc[0], enc[1])
        if encoded_uri == uri:
            if not uri.startswith("urn-"):
                raise BlueGigaModuleException("Unable to encode URI:%s" % uri)
            else:
                encoded_uri = uri.replace("urn-", '04')
                encoded_uri = encoded_uri.replace('-', '')
                encoded_uri = encoded_uri.decode("hex")

        #advertisement_data = b"\x02\x01\x06"
        advertisement_data = b"\x03\x03\xD8\xFE"
        advertisement_data += struct.pack('B', 5+len(encoded_uri))
        advertisement_data += b"\x16\xD8\xFE\x00\x08"
        advertisement_data += encoded_uri
        self._api.ble_cmd_gap_set_adv_data(0, adv_data=advertisement_data)

    def stop_advertising(self):
        self._api.ble_cmd_gap_set_mode(discover=gap_discoverable_mode['gap_non_discoverable'],
                                       connect=gap_connectable_mode['gap_undirected_connectable'])

    def write_attribute(self, handle, value, offset=0, timeout=1):
        self.start_procedure(PROCEDURE)
        self._api.ble_cmd_attributes_write(handle=handle, offset=offset, value=value)
        self.wait_for_procedure(timeout=timeout)

    def read_by_handle(self, handle, offset, timeout):
        self.start_procedure(PROCEDURE)
        self._api.ble_cmd_attributes_read(handle, offset)
        if self.wait_for_procedure(timeout=timeout):
            return self.handle_values[handle]

    def read_type(self, handle, timeout=1):
        self.start_procedure(PROCEDURE)
        self._api.ble_cmd_attributes_read_type(handle)
        if self.wait_for_procedure(timeout=timeout):
            return self.handle_types[handle]


    #-------------------- Events triggered by incoming data ------------- #
    def ble_evt_attributes_status(self, handle, flags):
        super(BlueGigaModule, self).ble_evt_attributes_status(handle, flags)

    def ble_rsp_attributes_write(self, result):
        super(BlueGigaServer, self).ble_rsp_attributes_write(result)
        self.procedure_complete(PROCEDURE)

    def ble_evt_attributes_value(self, connection, reason, handle, offset, value):
        super(BlueGigaServer, self).ble_evt_attributes_value(connection, reason, handle, offset, value)
        self.update_attribute_cache(handle, offset, value)

    def ble_rsp_attributes_read_type(self, handle, result, value):
        super(BlueGigaServer, self).ble_rsp_attributes_read_type(handle, result, value)
        self.handle_types[handle] = value
        self.procedure_complete(PROCEDURE)

    def ble_rsp_attributes_read(self, handle, offset, result, value):
        super(BlueGigaServer, self).ble_rsp_attributes_read(handle, offset, result, value)
        self.update_attribute_cache(handle, offset, value)
        self.procedure_complete(PROCEDURE)

    def update_attribute_cache(self, handle, offset, value):
        if handle in self.handle_values and offset > 0:
            self.handle_values[handle] = self.handle_values[handle][:offset] + value
        elif offset > 0:
            self.handle_values[handle] = b"\x00"*offset + value
        else:
            self.handle_values[handle] = value
