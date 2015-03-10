# ! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Administrator'
import a_pb2 as struct_oss_pb_pb2
import binascii

entitydesc=struct_oss_pb_pb2.entity_desc()
entitydesc.entity_id=1
entitydesc.entity_name='haha'
entitydesc.opt_1 = "sadfsdffd"
entitydesc.opt_2 = "sadfsdffd"
#create proto
entityattr=entitydesc.attributes.add() #嵌套message
entityattr.attr_id = 11
entityattr.attribute = '标题'
entityattr.value.append("title adfadf")

entity_attr_str=entityattr.SerializeToString()

print entity_attr_str
print binascii.hexlify(entity_attr_str)
entitydesc_str=entitydesc.SerializeToString()
print entitydesc.ByteSize()
print entitydesc_str
print binascii.hexlify(entitydesc_str)
print '----'
#read
entityattr2 = struct_oss_pb_pb2.entity_attr()
entityattr2.ParseFromString(binascii.unhexlify(binascii.hexlify(entity_attr_str)))
print entityattr2.attr_id
print entityattr2.attribute
for i in entityattr2.value:
    print i
print '----'
entitydesc2=struct_oss_pb_pb2.entity_desc()
entitydesc2.ParseFromString(entitydesc_str)
print entitydesc2.entity_id
print type(entitydesc2.opt_2)
print entitydesc2.opt_1
print entitydesc2.my
#repeated entity_attr attributes，由于是repeated需要遍历
for oneatt in entitydesc2.attributes:
    print oneatt.attr_id
    for i in oneatt.value:
        print i



