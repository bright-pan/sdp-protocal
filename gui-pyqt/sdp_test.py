# ! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Administrator'

import sdp_pb2
import binascii

msg = sdp_pb2.Message()
print sdp_pb2.MSG.items()
print sdp_pb2.MSG.values()

msg.msg_type = sdp_pb2.MSG_REQ_LOGIN
msg.sequence = 1;
#msg.request.login.id = "asdfasdf"
#msg.request.login.k0 = "afasdfasdf"
#msg.request.login.k1 = "asdfasdfasfd"
msg.request.login.version = 2

msg_str = msg.SerializeToString()

print binascii.hexlify(msg_str), msg.ByteSize()
msg1 = sdp_pb2.Message()
msg1.ParseFromString(msg_str)
print msg1.request.login.version