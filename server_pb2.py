# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: server.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cserver.proto\x12\x07\x63olbert\".\n\x05Query\x12\r\n\x05query\x18\x01 \x01(\t\x12\x0b\n\x03qid\x18\x02 \x01(\x05\x12\t\n\x01k\x18\x03 \x01(\x05\"6\n\nTopkResult\x12\x0b\n\x03pid\x18\x01 \x01(\x05\x12\x0c\n\x04rank\x18\x02 \x01(\x05\x12\r\n\x05score\x18\x03 \x01(\x02\"=\n\x0bQueryResult\x12\x0b\n\x03qid\x18\x01 \x01(\x05\x12!\n\x04topk\x18\x02 \x03(\x0b\x32\x13.colbert.TopkResult2l\n\x06Server\x12\x30\n\x06Search\x12\x0e.colbert.Query\x1a\x14.colbert.QueryResult\"\x00\x12\x30\n\x06Rerank\x12\x0e.colbert.Query\x1a\x14.colbert.QueryResult\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'server_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _QUERY._serialized_start=25
  _QUERY._serialized_end=71
  _TOPKRESULT._serialized_start=73
  _TOPKRESULT._serialized_end=127
  _QUERYRESULT._serialized_start=129
  _QUERYRESULT._serialized_end=190
  _SERVER._serialized_start=192
  _SERVER._serialized_end=300
# @@protoc_insertion_point(module_scope)
