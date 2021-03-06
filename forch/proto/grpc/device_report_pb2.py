# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: forch/proto/grpc/device_report.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from forch.proto import devices_state_pb2 as forch_dot_proto_dot_devices__state__pb2
from forch.proto import shared_constants_pb2 as forch_dot_proto_dot_shared__constants__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='forch/proto/grpc/device_report.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n$forch/proto/grpc/device_report.proto\x1a\x1f\x66orch/proto/devices_state.proto\x1a\"forch/proto/shared_constants.proto2=\n\x0c\x44\x65viceReport\x12-\n\x12ReportDevicesState\x12\r.DevicesState\x1a\x06.Empty\"\x00\x62\x06proto3'
  ,
  dependencies=[forch_dot_proto_dot_devices__state__pb2.DESCRIPTOR,forch_dot_proto_dot_shared__constants__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_DEVICEREPORT = _descriptor.ServiceDescriptor(
  name='DeviceReport',
  full_name='DeviceReport',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=109,
  serialized_end=170,
  methods=[
  _descriptor.MethodDescriptor(
    name='ReportDevicesState',
    full_name='DeviceReport.ReportDevicesState',
    index=0,
    containing_service=None,
    input_type=forch_dot_proto_dot_devices__state__pb2._DEVICESSTATE,
    output_type=forch_dot_proto_dot_shared__constants__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DEVICEREPORT)

DESCRIPTOR.services_by_name['DeviceReport'] = _DEVICEREPORT

# @@protoc_insertion_point(module_scope)
