# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: customer_state.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x63ustomer_state.proto\x12\x0e\x63ustomer_state\x1a\x1bgoogle/protobuf/empty.proto\"y\n\rCustomerState\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x14\n\x0c\x63reated_date\x18\x02 \x01(\t\x12\x14\n\x0cupdated_date\x18\x03 \x01(\t\x12\x0f\n\x07\x63onfirm\x18\x04 \x01(\x08\x12\x10\n\x08\x63ustomer\x18\x05 \x01(\x03\x12\r\n\x05state\x18\x06 \x01(\x03\"\x1a\n\x18\x43ustomerStateListRequest\"*\n\x1c\x43ustomerStateRetrieveRequest\x12\n\n\x02id\x18\x01 \x01(\x03\x32\xa1\x03\n\x17\x43ustomerStateController\x12S\n\x04List\x12(.customer_state.CustomerStateListRequest\x1a\x1d.customer_state.CustomerState\"\x00\x30\x01\x12H\n\x06\x43reate\x12\x1d.customer_state.CustomerState\x1a\x1d.customer_state.CustomerState\"\x00\x12Y\n\x08Retrieve\x12,.customer_state.CustomerStateRetrieveRequest\x1a\x1d.customer_state.CustomerState\"\x00\x12H\n\x06Update\x12\x1d.customer_state.CustomerState\x1a\x1d.customer_state.CustomerState\"\x00\x12\x42\n\x07\x44\x65stroy\x12\x1d.customer_state.CustomerState\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3')



_CUSTOMERSTATE = DESCRIPTOR.message_types_by_name['CustomerState']
_CUSTOMERSTATELISTREQUEST = DESCRIPTOR.message_types_by_name['CustomerStateListRequest']
_CUSTOMERSTATERETRIEVEREQUEST = DESCRIPTOR.message_types_by_name['CustomerStateRetrieveRequest']
CustomerState = _reflection.GeneratedProtocolMessageType('CustomerState', (_message.Message,), {
  'DESCRIPTOR' : _CUSTOMERSTATE,
  '__module__' : 'customer_state_pb2'
  # @@protoc_insertion_point(class_scope:customer_state.CustomerState)
  })
_sym_db.RegisterMessage(CustomerState)

CustomerStateListRequest = _reflection.GeneratedProtocolMessageType('CustomerStateListRequest', (_message.Message,), {
  'DESCRIPTOR' : _CUSTOMERSTATELISTREQUEST,
  '__module__' : 'customer_state_pb2'
  # @@protoc_insertion_point(class_scope:customer_state.CustomerStateListRequest)
  })
_sym_db.RegisterMessage(CustomerStateListRequest)

CustomerStateRetrieveRequest = _reflection.GeneratedProtocolMessageType('CustomerStateRetrieveRequest', (_message.Message,), {
  'DESCRIPTOR' : _CUSTOMERSTATERETRIEVEREQUEST,
  '__module__' : 'customer_state_pb2'
  # @@protoc_insertion_point(class_scope:customer_state.CustomerStateRetrieveRequest)
  })
_sym_db.RegisterMessage(CustomerStateRetrieveRequest)

_CUSTOMERSTATECONTROLLER = DESCRIPTOR.services_by_name['CustomerStateController']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CUSTOMERSTATE._serialized_start=69
  _CUSTOMERSTATE._serialized_end=190
  _CUSTOMERSTATELISTREQUEST._serialized_start=192
  _CUSTOMERSTATELISTREQUEST._serialized_end=218
  _CUSTOMERSTATERETRIEVEREQUEST._serialized_start=220
  _CUSTOMERSTATERETRIEVEREQUEST._serialized_end=262
  _CUSTOMERSTATECONTROLLER._serialized_start=265
  _CUSTOMERSTATECONTROLLER._serialized_end=682
# @@protoc_insertion_point(module_scope)