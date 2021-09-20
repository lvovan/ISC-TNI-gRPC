# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: calc.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='calc.proto',
  package='calc',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\ncalc.proto\x12\x04\x63\x61lc\")\n\x11\x41rithmeticRequest\x12\t\n\x01\x61\x18\x01 \x01(\x05\x12\t\n\x01\x62\x18\x02 \x01(\x05\"$\n\x12\x41rithmeticResponse\x12\x0e\n\x06result\x18\x01 \x01(\x05\x32\x83\x01\n\x04\x43\x61lc\x12:\n\x03\x41\x64\x64\x12\x17.calc.ArithmeticRequest\x1a\x18.calc.ArithmeticResponse\"\x00\x12?\n\x08Multiply\x12\x17.calc.ArithmeticRequest\x1a\x18.calc.ArithmeticResponse\"\x00\x62\x06proto3'
)




_ARITHMETICREQUEST = _descriptor.Descriptor(
  name='ArithmeticRequest',
  full_name='calc.ArithmeticRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='calc.ArithmeticRequest.a', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='b', full_name='calc.ArithmeticRequest.b', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=61,
)


_ARITHMETICRESPONSE = _descriptor.Descriptor(
  name='ArithmeticResponse',
  full_name='calc.ArithmeticResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='calc.ArithmeticResponse.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=63,
  serialized_end=99,
)

DESCRIPTOR.message_types_by_name['ArithmeticRequest'] = _ARITHMETICREQUEST
DESCRIPTOR.message_types_by_name['ArithmeticResponse'] = _ARITHMETICRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ArithmeticRequest = _reflection.GeneratedProtocolMessageType('ArithmeticRequest', (_message.Message,), {
  'DESCRIPTOR' : _ARITHMETICREQUEST,
  '__module__' : 'calc_pb2'
  # @@protoc_insertion_point(class_scope:calc.ArithmeticRequest)
  })
_sym_db.RegisterMessage(ArithmeticRequest)

ArithmeticResponse = _reflection.GeneratedProtocolMessageType('ArithmeticResponse', (_message.Message,), {
  'DESCRIPTOR' : _ARITHMETICRESPONSE,
  '__module__' : 'calc_pb2'
  # @@protoc_insertion_point(class_scope:calc.ArithmeticResponse)
  })
_sym_db.RegisterMessage(ArithmeticResponse)



_CALC = _descriptor.ServiceDescriptor(
  name='Calc',
  full_name='calc.Calc',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=102,
  serialized_end=233,
  methods=[
  _descriptor.MethodDescriptor(
    name='Add',
    full_name='calc.Calc.Add',
    index=0,
    containing_service=None,
    input_type=_ARITHMETICREQUEST,
    output_type=_ARITHMETICRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Multiply',
    full_name='calc.Calc.Multiply',
    index=1,
    containing_service=None,
    input_type=_ARITHMETICREQUEST,
    output_type=_ARITHMETICRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CALC)

DESCRIPTOR.services_by_name['Calc'] = _CALC

# @@protoc_insertion_point(module_scope)