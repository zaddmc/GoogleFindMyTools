import binascii
import sys

from NovaApi.ExecuteAction.LocateTracker.location_request import (
    get_location_data_for_device,
)
from NovaApi.ListDevices.nbe_list_devices import request_device_list
from NovaApi.nova_request import nova_request
from NovaApi.scopes import NOVA_LIST_DEVICS_API_SCOPE
from NovaApi.util import generate_random_uuid
from ProtoDecoders import DeviceUpdate_pb2
from ProtoDecoders.decoder import get_canonic_ids, parse_device_list_protobuf
from SpotApi.CreateBleDevice.create_ble_device import register_esp32
from SpotApi.UploadPrecomputedPublicKeyIds.upload_precomputed_public_key_ids import (
    refresh_custom_trackers,
)

result_hex = request_device_list()

device_list = parse_device_list_protobuf(result_hex)

refresh_custom_trackers(device_list)
canonic_ids = get_canonic_ids(device_list)


selected_idx = int(sys.argv[1]) - 1

selected_device_name = canonic_ids[selected_idx][0]
selected_canonic_id = canonic_ids[selected_idx][1]


get_location_data_for_device(selected_canonic_id, selected_device_name)
