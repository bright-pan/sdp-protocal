# ! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Administrator'

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
from google.protobuf.message import DecodeError
import sdp_pb2
import binascii

import ui_demo_main
import ui_req_login, ui_rep_login
import ui_req_logout, ui_rep_logout
import ui_req_keepalive, ui_rep_keepalive
import ui_req_workalarm, ui_rep_workalarm
import ui_req_faultalarm, ui_rep_faultalarm
import ui_req_battery, ui_rep_battery
import ui_req_open, ui_rep_open
import ui_req_phoneadd, ui_rep_phoneadd
import ui_req_phonemodify, ui_rep_phonemodify
import ui_req_phonedelete, ui_rep_phonedelete
import ui_req_keyadd, ui_rep_keyadd
import ui_req_keymodify, ui_rep_keymodify
import ui_req_keydelete, ui_rep_keydelete
import ui_req_accountadd, ui_rep_accountadd
import ui_req_accountmodify, ui_rep_accountmodify
import ui_req_accountdelete, ui_rep_accountdelete
import ui_req_accounttokey, ui_rep_accounttokey
import ui_req_accounttophone, ui_rep_accounttophone
import ui_req_motor, ui_rep_motor
import ui_req_time, ui_rep_time
import ui_req_password, ui_rep_password
import ui_req_accountcheck, ui_rep_accountcheck
import ui_req_accountmapcheck, ui_rep_accountmapcheck
import ui_req_accountmapsync, ui_rep_accountmapsync
import ui_req_keycheck, ui_rep_keycheck
import ui_req_keymapcheck, ui_rep_keymapcheck
import ui_req_keymapsync, ui_rep_keymapsync
import ui_req_phonecheck, ui_rep_phonecheck
import ui_req_phonemapcheck, ui_rep_phonemapcheck
import ui_req_phonemapsync, ui_rep_phonemapsync
import ui_req_logcheck, ui_rep_logcheck
import ui_req_logmapcheck, ui_rep_logmapcheck
import ui_req_logmapsync, ui_rep_logmapsync

name_list = []

dmsg = sdp_pb2.Message()
msg_type_name_list = sdp_pb2.MSG.keys()
msg_type_value_list = sdp_pb2.MSG.values()

class ReqLoginDialog(QDialog, ui_req_login.Ui_Dialog):
    def __init__(self, parent=None):
        super(ReqLoginDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"登录请求")

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.request.login.k0 = str(self.K0lineEdit.text())
        msg.request.login.k1 = str(self.K1lineEdit.text())
        msg.request.login.version = int(self.VERSIONlineEdit.text())
        msg.request.login.id = str(self.IDlineEdit.text())

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.K0lineEdit.setText(msg.request.login.k0)
        self.K1lineEdit.setText(msg.request.login.k1)
        self.IDlineEdit.setText(msg.request.login.id)
        self.VERSIONlineEdit.setText(str(msg.request.login.version))


class RepLoginDialog(QDialog, ui_rep_login.Ui_Dialog):
    def __init__(self, parent=None):
        super(RepLoginDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"登录响应")
        self.status_name_list = sdp_pb2.LOGIN_STATUS_TYPE.keys()
        self.status_value_list = sdp_pb2.LOGIN_STATUS_TYPE.values()
        self.LoginStatusComboBox.insertItems(0, QStringList(self.status_name_list))

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.response.result = True
        msg.response.last_response = True
        msg.response.login.status = self.status_value_list[self.LoginStatusComboBox.currentIndex()]
        msg.response.login.server_time = int(self.TimelineEdit.text())

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.LoginStatusComboBox.setCurrentIndex(self.status_value_list.index(msg.response.login.status))
        self.TimelineEdit.setText(str(msg.response.login.server_time))


class ReqLogoutDialog(QDialog, ui_req_logout.Ui_Dialog):
    def __init__(self, parent=None):
        super(ReqLogoutDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"登出请求")

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))


class RepLogoutDialog(QDialog, ui_rep_logout.Ui_Dialog):
    def __init__(self, parent=None):
        super(RepLogoutDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"登出响应")

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.response.result = True
        msg.response.last_response = True

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))


class ReqKeepAliveDialog(QDialog, ui_req_keepalive.Ui_Dialog):
    def __init__(self, parent=None):
        super(ReqKeepAliveDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"心跳请求")

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))


class RepKeepAliveDialog(QDialog, ui_rep_keepalive.Ui_Dialog):
    def __init__(self, parent=None):
        super(RepKeepAliveDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"心跳响应")

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.response.result = True
        msg.response.last_response = True

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))


class ReqWorkAlarmDialog(QDialog, ui_req_workalarm.Ui_Dialog):
    def __init__(self, parent=None):
        super(ReqWorkAlarmDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"工作告警请求")
        self.work_type_name_list = sdp_pb2.WORK_ALARM_TYPE.keys()
        self.work_type_value_list = sdp_pb2.WORK_ALARM_TYPE.values()
        self.lock_status_name_list = sdp_pb2.LOCK_STATUS_TYPE.keys()
        self.lock_status_value_list = sdp_pb2.LOCK_STATUS_TYPE.values()
        self.TypeComboBox.insertItems(0, QStringList(self.work_type_name_list))
        self.StatusComboBox.insertItems(0, QStringList(self.lock_status_name_list))

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.request.workalarm.type = self.work_type_value_list[self.TypeComboBox.currentIndex()]
        msg.request.workalarm.status = self.lock_status_value_list[self.StatusComboBox.currentIndex()]
        msg.request.workalarm.occurred_time = int(self.OccurredTimelineEdit.text())

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.TypeComboBox.setCurrentIndex(self.work_type_value_list.index(msg.request.workalarm.type))
        self.StatusComboBox.setCurrentIndex(self.lock_status_value_list.index(msg.request.workalarm.status))
        self.OccurredTimelineEdit.setText(str(msg.request.workalarm.occurred_time))


class RepWorkAlarmDialog(QDialog, ui_rep_workalarm.Ui_Dialog):
    def __init__(self, parent=None):
        super(RepWorkAlarmDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"工作告警响应")

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.response.result = True
        msg.response.last_response = True

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))


class ReqFaultAlarmDialog(QDialog, ui_req_faultalarm.Ui_Dialog):
    def __init__(self, parent=None):
        super(ReqFaultAlarmDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"故障告警请求")
        self.type_name_list = sdp_pb2.FAULT_ALARM_TYPE.keys()
        self.type_value_list = sdp_pb2.FAULT_ALARM_TYPE.values()
        self.status_name_list = sdp_pb2.LOCK_STATUS_TYPE.keys()
        self.status_value_list = sdp_pb2.LOCK_STATUS_TYPE.values()
        self.TypeComboBox.insertItems(0, QStringList(self.type_name_list))
        self.StatusComboBox.insertItems(0, QStringList(self.status_name_list))

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.request.workalarm.type = self.type_value_list[self.TypeComboBox.currentIndex()]
        msg.request.workalarm.status = self.status_value_list[self.StatusComboBox.currentIndex()]
        msg.request.workalarm.occurred_time = int(self.OccurredTimelineEdit.text())

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.TypeComboBox.setCurrentIndex(self.type_value_list.index(msg.request.workalarm.type))
        self.StatusComboBox.setCurrentIndex(self.status_value_list.index(msg.request.workalarm.status))
        self.OccurredTimelineEdit.setText(str(msg.request.workalarm.occurred_time))


class RepFaultAlarmDialog(QDialog, ui_rep_faultalarm.Ui_Dialog):
    def __init__(self, parent=None):
        super(RepFaultAlarmDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"故障告警响应")

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.response.result = True
        msg.response.last_response = True

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))


class ReqBatteryDialog(QDialog, ui_req_battery.Ui_Dialog):
    def __init__(self, parent=None):
        super(ReqBatteryDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"电池状态请求")
        self.status_name_list = sdp_pb2.BATTERY_STATUS_TYPE.keys()
        self.status_value_list = sdp_pb2.BATTERY_STATUS_TYPE.values()
        self.StatusComboBox.insertItems(0, QStringList(self.status_name_list))

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.request.battery.status = self.status_value_list[self.StatusComboBox.currentIndex()]
        msg.request.battery.capacity = int(self.CapacitylineEdit.text())
        msg.request.battery.occurred_time = int(self.OccurredTimelineEdit.text())

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.StatusComboBox.setCurrentIndex(self.status_value_list.index(msg.request.battery.status))
        self.CapacitylineEdit.setText(str(msg.request.battery.capacity))
        self.OccurredTimelineEdit.setText(str(msg.request.battery.occurred_time))


class RepBatteryDialog(QDialog, ui_rep_battery.Ui_Dialog):
    def __init__(self, parent=None):
        super(RepBatteryDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"电池状态响应")

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.response.result = True
        msg.response.last_response = True

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))


class ReqOpenDialog(QDialog, ui_req_open.Ui_Dialog):
    def __init__(self, parent=None):
        super(ReqOpenDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"开门记录请求")
        self.type_name_list = sdp_pb2.OPEN_PATTERN_TYPE.keys()
        self.type_value_list = sdp_pb2.OPEN_PATTERN_TYPE.values()
        self.status_name_list = sdp_pb2.LOCK_STATUS_TYPE.keys()
        self.status_value_list = sdp_pb2.LOCK_STATUS_TYPE.values()
        self.TypeComboBox.insertItems(0, QStringList(self.type_name_list))
        self.StatusComboBox.insertItems(0, QStringList(self.status_name_list))

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.request.open.type = self.type_value_list[self.TypeComboBox.currentIndex()]
        msg.request.open.account_id = int(self.AccountIDlineEdit.text())
        msg.request.open.key_id = int(self.KeyIDlineEdit.text())
        msg.request.open.status = self.status_value_list[self.StatusComboBox.currentIndex()]
        msg.request.open.occurred_time = int(self.OccurredTimelineEdit.text())

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.TypeComboBox.setCurrentIndex(self.type_value_list.index(msg.request.open.type))
        self.AccountIDlineEdit.setText(str(msg.request.open.account_id))
        self.KeyIDlineEdit.setText(str(msg.request.open.key_id))
        self.StatusComboBox.setCurrentIndex(self.status_value_list.index(msg.request.open.status))
        self.OccurredTimelineEdit.setText(str(msg.request.open.occurred_time))


class RepOpenDialog(QDialog, ui_rep_open.Ui_Dialog):
    def __init__(self, parent=None):
        super(RepOpenDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"开门记录响应")

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.response.result = True
        msg.response.last_response = True

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))


class ReqPhoneAddDialog(QDialog, ui_req_phoneadd.Ui_Dialog):
    def __init__(self, parent=None):
        super(ReqPhoneAddDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"电话增加请求")
        self.type_name_list = sdp_pb2.PHONE_AUTH_TYPE.keys()
        self.type_value_list = sdp_pb2.PHONE_AUTH_TYPE.values()
        self.TypeComboBox.insertItems(0, QStringList(self.type_name_list))

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.request.phone_add.type = self.type_value_list[self.TypeComboBox.currentIndex()]
        msg.request.phone_add.number = str(self.PhoneNumberlineEdit.text())
        msg.request.phone_add.id = int(self.PhoneIDlineEdit.text())
        msg.request.phone_add.occurred_time = int(self.OccurredTimelineEdit.text())

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.TypeComboBox.setCurrentIndex(self.type_value_list.index(msg.request.phone_add.type))
        self.PhoneNumberlineEdit.setText(msg.request.phone_add.number)
        self.PhoneIDlineEdit.setText(str(msg.request.phone_add.id))
        self.OccurredTimelineEdit.setText(str(msg.request.phone_add.occurred_time))


class RepPhoneAddDialog(QDialog, ui_rep_phoneadd.Ui_Dialog):
    def __init__(self, parent=None):
        super(RepPhoneAddDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"电话增加响应")
        self.status_name_list = sdp_pb2.PHONE_STATUS_TYPE.keys()
        self.status_value_list = sdp_pb2.PHONE_STATUS_TYPE.values()
        self.StatusComboBox.insertItems(0, QStringList(self.status_name_list))

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.response.result = True
        msg.response.last_response = True
        msg.response.phone_add.status = self.status_value_list[self.StatusComboBox.currentIndex()]

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.StatusComboBox.setCurrentIndex(self.status_value_list.index(msg.response.phone_add.status))


class ReqPhoneModifyDialog(QDialog, ui_req_phonemodify.Ui_Dialog):
    def __init__(self, parent=None):
        super(ReqPhoneModifyDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"电话修改请求")
        self.type_name_list = sdp_pb2.PHONE_AUTH_TYPE.keys()
        self.type_value_list = sdp_pb2.PHONE_AUTH_TYPE.values()
        self.TypeComboBox.insertItems(0, QStringList(self.type_name_list))

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.request.phone_modify.type = self.type_value_list[self.TypeComboBox.currentIndex()]
        msg.request.phone_modify.number = str(self.PhoneNumberlineEdit.text())
        msg.request.phone_modify.id = int(self.PhoneIDlineEdit.text())
        msg.request.phone_modify.occurred_time = int(self.OccurredTimelineEdit.text())

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.TypeComboBox.setCurrentIndex(self.type_value_list.index(msg.request.phone_modify.type))
        self.PhoneNumberlineEdit.setText(msg.request.phone_modify.number)
        self.PhoneIDlineEdit.setText(str(msg.request.phone_modify.id))
        self.OccurredTimelineEdit.setText(str(msg.request.phone_modify.occurred_time))


class RepPhoneModifyDialog(QDialog, ui_rep_phonemodify.Ui_Dialog):
    def __init__(self, parent=None):
        super(RepPhoneModifyDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"电话修改响应")
        self.status_name_list = sdp_pb2.PHONE_STATUS_TYPE.keys()
        self.status_value_list = sdp_pb2.PHONE_STATUS_TYPE.values()
        self.StatusComboBox.insertItems(0, QStringList(self.status_name_list))

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.response.result = True
        msg.response.last_response = True
        msg.response.phone_modify.status = self.status_value_list[self.StatusComboBox.currentIndex()]

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.StatusComboBox.setCurrentIndex(self.status_value_list.index(msg.response.phone_modify.status))


class ReqPhoneDeleteDialog(QDialog, ui_req_phonedelete.Ui_Dialog):
    def __init__(self, parent=None):
        super(ReqPhoneDeleteDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"电话删除请求")

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.request.phone_delete.id = int(self.PhoneIDlineEdit.text())
        msg.request.phone_delete.occurred_time = int(self.OccurredTimelineEdit.text())

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.PhoneIDlineEdit.setText(str(msg.request.phone_delete.id))
        self.OccurredTimelineEdit.setText(str(msg.request.phone_delete.occurred_time))


class RepPhoneDeleteDialog(QDialog, ui_rep_phonedelete.Ui_Dialog):
    def __init__(self, parent=None):
        super(RepPhoneDeleteDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"电话删除响应")
        self.status_name_list = sdp_pb2.PHONE_STATUS_TYPE.keys()
        self.status_value_list = sdp_pb2.PHONE_STATUS_TYPE.values()
        self.StatusComboBox.insertItems(0, QStringList(self.status_name_list))

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.response.result = True
        msg.response.last_response = True
        msg.response.phone_delete.status = self.status_value_list[self.StatusComboBox.currentIndex()]

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.StatusComboBox.setCurrentIndex(self.status_value_list.index(msg.response.phone_delete.status))


class ReqKeyAddDialog(QDialog, ui_req_keyadd.Ui_Dialog):
    def __init__(self, parent=None):
        super(ReqKeyAddDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"钥匙增加请求")
        self.auth_type_name_list = sdp_pb2.KEY_AUTH_TYPE.keys()
        self.auth_type_value_list = sdp_pb2.KEY_AUTH_TYPE.values()
        self.AuthTypeComboBox.insertItems(0, QStringList(self.auth_type_name_list))
        self.key_type_name_list = sdp_pb2.KEY_TYPE.keys()
        self.key_type_value_list = sdp_pb2.KEY_TYPE.values()
        self.KeyTypeComboBox.insertItems(0, QStringList(self.key_type_name_list))

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.request.key_add.key_type = self.key_type_value_list[self.KeyTypeComboBox.currentIndex()]
        msg.request.key_add.auth_type = self.auth_type_value_list[self.AuthTypeComboBox.currentIndex()]
        msg.request.key_add.id = int(self.KeyIDlineEdit.text())
        msg.request.key_add.code = str(self.KeyCodelineEdit.text())
        msg.request.key_add.weekly = str(self.WeeklylineEdit.text())
        msg.request.key_add.start_time = int(self.StartTimelineEdit.text())
        msg.request.key_add.end_time = int(self.EndTimelineEdit.text())
        msg.request.key_add.occurred_time = int(self.OccurredTimelineEdit.text())

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.AuthTypeComboBox.setCurrentIndex(self.auth_type_value_list.index(msg.request.key_add.auth_type))
        self.KeyTypeComboBox.setCurrentIndex(self.key_type_value_list.index(msg.request.key_add.key_type))
        self.KeyIDlineEdit.setText(str(msg.request.key_add.id))
        self.KeyCodelineEdit.setText(msg.request.key_add.code)
        self.WeeklylineEdit.setText(msg.request.key_add.weekly)
        self.StartTimelineEdit.setText(str(msg.request.key_add.start_time))
        self.EndTimelineEdit.setText(str(msg.request.key_add.end_time))
        self.OccurredTimelineEdit.setText(str(msg.request.key_add.occurred_time))


class RepKeyAddDialog(QDialog, ui_rep_keyadd.Ui_Dialog):
    def __init__(self, parent=None):
        super(RepKeyAddDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"钥匙增加响应")
        self.status_name_list = sdp_pb2.KEY_STATUS_TYPE.keys()
        self.status_value_list = sdp_pb2.KEY_STATUS_TYPE.values()
        self.StatusComboBox.insertItems(0, QStringList(self.status_name_list))

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.response.result = True
        msg.response.last_response = True
        msg.response.key_add.status = self.status_value_list[self.StatusComboBox.currentIndex()]

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.StatusComboBox.setCurrentIndex(self.status_value_list.index(msg.response.key_add.status))

class ReqKeyModifyDialog(QDialog, ui_req_keymodify.Ui_Dialog):
    def __init__(self, parent=None):
        super(ReqKeyModifyDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"钥匙修改请求")
        self.auth_type_name_list = sdp_pb2.KEY_AUTH_TYPE.keys()
        self.auth_type_value_list = sdp_pb2.KEY_AUTH_TYPE.values()
        self.AuthTypeComboBox.insertItems(0, QStringList(self.auth_type_name_list))
        self.key_type_name_list = sdp_pb2.KEY_TYPE.keys()
        self.key_type_value_list = sdp_pb2.KEY_TYPE.values()
        self.KeyTypeComboBox.insertItems(0, QStringList(self.key_type_name_list))

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.request.key_modify.key_type = self.key_type_value_list[self.KeyTypeComboBox.currentIndex()]
        msg.request.key_modify.auth_type = self.auth_type_value_list[self.AuthTypeComboBox.currentIndex()]
        msg.request.key_modify.id = int(self.KeyIDlineEdit.text())
        msg.request.key_modify.code = str(self.KeyCodelineEdit.text())
        msg.request.key_modify.weekly = str(self.WeeklylineEdit.text())
        msg.request.key_modify.start_time = int(self.StartTimelineEdit.text())
        msg.request.key_modify.end_time = int(self.EndTimelineEdit.text())
        msg.request.key_modify.occurred_time = int(self.OccurredTimelineEdit.text())

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.AuthTypeComboBox.setCurrentIndex(self.auth_type_value_list.index(msg.request.key_modify.auth_type))
        self.KeyTypeComboBox.setCurrentIndex(self.key_type_value_list.index(msg.request.key_modify.key_type))
        self.KeyIDlineEdit.setText(str(msg.request.key_modify.id))
        self.KeyCodelineEdit.setText(msg.request.key_modify.code)
        self.WeeklylineEdit.setText(msg.request.key_modify.weekly)
        self.StartTimelineEdit.setText(str(msg.request.key_modify.start_time))
        self.EndTimelineEdit.setText(str(msg.request.key_modify.end_time))
        self.OccurredTimelineEdit.setText(str(msg.request.key_modify.occurred_time))

class RepKeyModifyDialog(QDialog, ui_rep_keymodify.Ui_Dialog):
    def __init__(self, parent=None):
        super(RepKeyModifyDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"钥匙修改响应")
        self.status_name_list = sdp_pb2.KEY_STATUS_TYPE.keys()
        self.status_value_list = sdp_pb2.KEY_STATUS_TYPE.values()
        self.StatusComboBox.insertItems(0, QStringList(self.status_name_list))

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.response.result = True
        msg.response.last_response = True
        msg.response.key_modify.status = self.status_value_list[self.StatusComboBox.currentIndex()]

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.StatusComboBox.setCurrentIndex(self.status_value_list.index(msg.response.key_modify.status))

class ReqKeyDeleteDialog(QDialog, ui_req_keydelete.Ui_Dialog):
    def __init__(self, parent=None):
        super(ReqKeyDeleteDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"钥匙删除请求")

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.request.key_delete.id = int(self.KeyIDlineEdit.text())
        msg.request.key_delete.occurred_time = int(self.OccurredTimelineEdit.text())

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.KeyIDlineEdit.setText(str(msg.request.key_delete.id))
        self.OccurredTimelineEdit.setText(str(msg.request.key_delete.occurred_time))


class RepKeyDeleteDialog(QDialog, ui_rep_keydelete.Ui_Dialog):
    def __init__(self, parent=None):
        super(RepKeyDeleteDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"钥匙删除响应")
        self.status_name_list = sdp_pb2.KEY_STATUS_TYPE.keys()
        self.status_value_list = sdp_pb2.KEY_STATUS_TYPE.values()
        self.StatusComboBox.insertItems(0, QStringList(self.status_name_list))

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.response.result = True
        msg.response.last_response = True
        msg.response.key_delete.status = self.status_value_list[self.StatusComboBox.currentIndex()]

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.StatusComboBox.setCurrentIndex(self.status_value_list.index(msg.response.key_delete.status))


class ReqAccountAddDialog(QDialog, ui_req_accountadd.Ui_Dialog):
    def __init__(self, parent=None):
        super(ReqAccountAddDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"账户增加请求")

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.request.account_add.id = int(self.AccountIDlineEdit.text())
        msg.request.account_add.name = str(self.AccountNamelineEdit.text())
        msg.request.account_add.occurred_time = int(self.OccurredTimelineEdit.text())

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.AccountIDlineEdit.setText(str(msg.request.account_add.id))
        self.AccountNamelineEdit.setText(msg.request.account_add.name)
        self.OccurredTimelineEdit.setText(str(msg.request.account_add.occurred_time))

class RepAccountAddDialog(QDialog, ui_rep_accountadd.Ui_Dialog):
    def __init__(self, parent=None):
        super(RepAccountAddDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"账户增加响应")
        self.status_name_list = sdp_pb2.ACCOUNT_STATUS_TYPE.keys()
        self.status_value_list = sdp_pb2.ACCOUNT_STATUS_TYPE.values()
        self.StatusComboBox.insertItems(0, QStringList(self.status_name_list))

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.response.result = True
        msg.response.last_response = True
        msg.response.account_add.status = self.status_value_list[self.StatusComboBox.currentIndex()]
        msg.response.account_add.id = int(self.IDlineEdit.text())
    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.StatusComboBox.setCurrentIndex(self.status_value_list.index(msg.response.account_add.status))
        self.IDlineEdit.setText(str(msg.response.account_add.id))


class ReqAccountModifyDialog(QDialog, ui_req_accountmodify.Ui_Dialog):
    def __init__(self, parent=None):
        super(ReqAccountModifyDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"账户修改请求")

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.request.account_modify.id = int(self.AccountIDlineEdit.text())
        msg.request.account_modify.name = str(self.AccountNamelineEdit.text())
        msg.request.account_modify.occurred_time = int(self.OccurredTimelineEdit.text())

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.AccountIDlineEdit.setText(str(msg.request.account_modify.id))
        self.AccountNamelineEdit.setText(msg.request.account_modify.name)
        self.OccurredTimelineEdit.setText(str(msg.request.account_modify.occurred_time))


class RepAccountModifyDialog(QDialog, ui_rep_accountmodify.Ui_Dialog):
    def __init__(self, parent=None):
        super(RepAccountModifyDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"钥匙修改响应")
        self.status_name_list = sdp_pb2.ACCOUNT_STATUS_TYPE.keys()
        self.status_value_list = sdp_pb2.ACCOUNT_STATUS_TYPE.values()
        self.StatusComboBox.insertItems(0, QStringList(self.status_name_list))

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.response.result = True
        msg.response.last_response = True
        msg.response.account_modify.status = self.status_value_list[self.StatusComboBox.currentIndex()]
        msg.response.account_modify.id = int(self.IDlineEdit.text())

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.StatusComboBox.setCurrentIndex(self.status_value_list.index(msg.response.account_modify.status))
        self.IDlineEdit.setText(str(msg.response.account_modify.id))


class ReqAccountDeleteDialog(QDialog, ui_req_accountdelete.Ui_Dialog):
    def __init__(self, parent=None):
        super(ReqAccountDeleteDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"账户删除请求")

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.request.account_delete.id = int(self.AccountIDlineEdit.text())
        msg.request.account_delete.occurred_time = int(self.OccurredTimelineEdit.text())

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.AccountIDlineEdit.setText(str(msg.request.account_delete.id))
        self.OccurredTimelineEdit.setText(str(msg.request.account_delete.occurred_time))


class RepAccountDeleteDialog(QDialog, ui_rep_accountdelete.Ui_Dialog):
    def __init__(self, parent=None):
        super(RepAccountDeleteDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"钥匙删除响应")
        self.status_name_list = sdp_pb2.ACCOUNT_STATUS_TYPE.keys()
        self.status_value_list = sdp_pb2.ACCOUNT_STATUS_TYPE.values()
        self.StatusComboBox.insertItems(0, QStringList(self.status_name_list))

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.response.result = True
        msg.response.last_response = True
        msg.response.account_delete.status = self.status_value_list[self.StatusComboBox.currentIndex()]
        msg.response.account_delete.id = int(self.IDlineEdit.text())
    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.StatusComboBox.setCurrentIndex(self.status_value_list.index(msg.response.account_delete.status))
        self.IDlineEdit.setText(str(msg.response.account_delete.id))

class ReqAccountToKeyDialog(QDialog, ui_req_accounttokey.Ui_Dialog):
    def __init__(self, parent=None):
        super(ReqAccountToKeyDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"账户绑定钥匙请求")

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.request.account_to_key.account_id = int(self.AccountIDlineEdit.text())
        msg.request.account_to_key.key_id = int(self.KeyIDlineEdit.text())
        msg.request.account_to_key.occurred_time = int(self.OccurredTimelineEdit.text())

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.AccountIDlineEdit.setText(str(msg.request.account_to_key.account_id))
        self.KeyIDlineEdit.setText(str(msg.request.account_to_key.key_id))
        self.OccurredTimelineEdit.setText(str(msg.request.account_to_key.occurred_time))


class RepAccountToKeyDialog(QDialog, ui_rep_accounttokey.Ui_Dialog):
    def __init__(self, parent=None):
        super(RepAccountToKeyDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"钥匙绑定钥匙响应")
        self.status_name_list = sdp_pb2.ACCOUNT_STATUS_TYPE.keys()
        self.status_value_list = sdp_pb2.ACCOUNT_STATUS_TYPE.values()
        self.StatusComboBox.insertItems(0, QStringList(self.status_name_list))

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.response.result = True
        msg.response.last_response = True
        msg.response.account_to_key.status = self.status_value_list[self.StatusComboBox.currentIndex()]
        msg.response.account_to_key.id = int(self.IDlineEdit.text())
    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.StatusComboBox.setCurrentIndex(self.status_value_list.index(msg.response.account_to_key.status))
        self.IDlineEdit.setText(str(msg.response.account_to_key.id))

class ReqAccountToPhoneDialog(QDialog, ui_req_accounttophone.Ui_Dialog):
    def __init__(self, parent=None):
        super(ReqAccountToPhoneDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"账户绑定电话请求")

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.request.account_to_phone.account_id = int(self.AccountIDlineEdit.text())
        msg.request.account_to_phone.phone_id = int(self.PhoneIDlineEdit.text())
        msg.request.account_to_phone.occurred_time = int(self.OccurredTimelineEdit.text())

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.AccountIDlineEdit.setText(str(msg.request.account_to_phone.account_id))
        self.PhoneIDlineEdit.setText(str(msg.request.account_to_phone.phone_id))
        self.OccurredTimelineEdit.setText(str(msg.request.account_to_phone.occurred_time))


class RepAccountToPhoneDialog(QDialog, ui_rep_accounttophone.Ui_Dialog):
    def __init__(self, parent=None):
        super(RepAccountToPhoneDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"钥匙绑定电话响应")
        self.status_name_list = sdp_pb2.ACCOUNT_STATUS_TYPE.keys()
        self.status_value_list = sdp_pb2.ACCOUNT_STATUS_TYPE.values()
        self.StatusComboBox.insertItems(0, QStringList(self.status_name_list))

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.response.result = True
        msg.response.last_response = True
        msg.response.account_to_key.status = self.status_value_list[self.StatusComboBox.currentIndex()]
        msg.response.account_to_key.id = int(self.IDlineEdit.text())
    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.StatusComboBox.setCurrentIndex(self.status_value_list.index(msg.response.account_to_key.status))
        self.IDlineEdit.setText(str(msg.response.account_to_key.id))


class ReqMotorDialog(QDialog, ui_req_motor.Ui_Dialog):
    def __init__(self, parent=None):
        super(ReqMotorDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"电机状态请求")
        self.status_name_list = sdp_pb2.MOTOR_STATUS_TYPE.keys()
        self.status_value_list = sdp_pb2.MOTOR_STATUS_TYPE.values()
        self.StatusComboBox.insertItems(0, QStringList(self.status_name_list))

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.request.motor.status = self.status_value_list[self.StatusComboBox.currentIndex()]

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.StatusComboBox.setCurrentIndex(self.status_value_list.index(msg.request.motor.status))

class RepMotorDialog(QDialog, ui_rep_motor.Ui_Dialog):
    def __init__(self, parent=None):
        super(RepMotorDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"电机状态响应")
        self.status_name_list = sdp_pb2.MOTOR_STATUS_TYPE.keys()
        self.status_value_list = sdp_pb2.MOTOR_STATUS_TYPE.values()
        self.StatusComboBox.insertItems(0, QStringList(self.status_name_list))

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.response.result = True
        msg.response.last_response = True
        msg.request.motor.status = self.status_value_list[self.StatusComboBox.currentIndex()]

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.StatusComboBox.setCurrentIndex(self.status_value_list.index(msg.request.motor.status))

class ReqTimeDialog(QDialog, ui_req_time.Ui_Dialog):
    def __init__(self, parent=None):
        super(ReqTimeDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"时间请求")

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.request.time.time = int(self.TimelineEdit.text())

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.TimelineEdit.setText(str(msg.request.time.time))

class RepTimeDialog(QDialog, ui_rep_time.Ui_Dialog):
    def __init__(self, parent=None):
        super(RepTimeDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"时间响应")

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.response.result = True
        msg.response.last_response = True
        msg.request.time.time = int(self.TimelineEdit.text())

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.TimelineEdit.setText(str(msg.request.time.time))
class ReqPasswordDialog(QDialog, ui_req_password.Ui_Dialog):
    def __init__(self, parent=None):
        super(ReqPasswordDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"密码请求")

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.request.password.k0 = str(self.K0lineEdit.text())

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.K0lineEdit.setText(msg.request.password.k0)

class RepPasswordDialog(QDialog, ui_rep_password.Ui_Dialog):
    def __init__(self, parent=None):
        super(RepPasswordDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"密码响应")

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.response.result = True
        msg.response.last_response = True

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))


class ReqAccountCheckDialog(QDialog, ui_req_accountcheck.Ui_Dialog):
    def __init__(self, parent=None):
        super(ReqAccountCheckDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"账户校验请求")

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.request.account_check.id = int(self.IDlineEdit.text())
        msg.request.account_check.time = int(self.TimelineEdit.text())

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.IDlineEdit.setText(str(msg.request.account_check.id))
        self.TimelineEdit.setText(str(msg.request.account_check.time))


class RepAccountCheckDialog(QDialog, ui_rep_accountcheck.Ui_Dialog):
    def __init__(self, parent=None):
        super(RepAccountCheckDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"账户校验响应")
        self.status_name_list = sdp_pb2.ACCOUNT_MAP_STATUS_TYPE.keys()
        self.status_value_list = sdp_pb2.ACCOUNT_MAP_STATUS_TYPE.values()
        self.StatusComboBox.insertItems(0, QStringList(self.status_name_list))

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.response.result = True
        msg.response.last_response = True
        msg.response.account_check.status = self.status_value_list[self.StatusComboBox.currentIndex()]

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.StatusComboBox.setCurrentIndex(self.status_value_list.index(msg.response.account_check.status))

class ReqAccountMapCheckDialog(QDialog, ui_req_accountmapcheck.Ui_Dialog):
    def __init__(self, parent=None):
        super(ReqAccountMapCheckDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"账户映射域校验请求")

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.request.account_map_check.time = int(self.TimelineEdit.text())

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.TimelineEdit.setText(str(msg.request.account_map_check.time))


class RepAccountMapCheckDialog(QDialog, ui_rep_accountmapcheck.Ui_Dialog):
    def __init__(self, parent=None):
        super(RepAccountMapCheckDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"账户映射域校验响应")
        self.status_name_list = sdp_pb2.ACCOUNT_MAP_STATUS_TYPE.keys()
        self.status_value_list = sdp_pb2.ACCOUNT_MAP_STATUS_TYPE.values()
        self.StatusComboBox.insertItems(0, QStringList(self.status_name_list))

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.response.result = True
        msg.response.last_response = True
        msg.response.account_map_check.status = self.status_value_list[self.StatusComboBox.currentIndex()]

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.StatusComboBox.setCurrentIndex(self.status_value_list.index(msg.response.account_map_check.status))

class ReqAccountMapSyncDialog(QDialog, ui_req_accountmapsync.Ui_Dialog):
    def __init__(self, parent=None):
        super(ReqAccountMapSyncDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"账户映射域同步请求")

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.request.account_map_sync.map = str(self.MapTextEdit.toPlainText())
        msg.request.account_map_sync.time = int(self.TimelineEdit.text())

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.MapTextEdit.setText(str(msg.request.account_map_sync.map))
        self.TimelineEdit.setText(str(msg.request.account_map_sync.time))


class RepAccountMapSyncDialog(QDialog, ui_rep_accountmapsync.Ui_Dialog):
    def __init__(self, parent=None):
        super(RepAccountMapSyncDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"账户映射域同步响应")
        self.status_name_list = sdp_pb2.ACCOUNT_MAP_STATUS_TYPE.keys()
        self.status_value_list = sdp_pb2.ACCOUNT_MAP_STATUS_TYPE.values()
        self.StatusComboBox.insertItems(0, QStringList(self.status_name_list))

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.response.result = True
        msg.response.last_response = True
        msg.response.account_map_sync.status = self.status_value_list[self.StatusComboBox.currentIndex()]

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.StatusComboBox.setCurrentIndex(self.status_value_list.index(msg.response.account_map_sync.status))

class ReqKeyCheckDialog(QDialog, ui_req_keycheck.Ui_Dialog):
    def __init__(self, parent=None):
        super(ReqKeyCheckDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"钥匙校验请求")

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.request.key_check.id = int(self.IDlineEdit.text())
        msg.request.key_check.time = int(self.TimelineEdit.text())

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.IDlineEdit.setText(str(msg.request.key_check.id))
        self.TimelineEdit.setText(str(msg.request.key_check.time))


class RepKeyCheckDialog(QDialog, ui_rep_keycheck.Ui_Dialog):
    def __init__(self, parent=None):
        super(RepKeyCheckDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"钥匙校验响应")
        self.status_name_list = sdp_pb2.KEY_MAP_STATUS_TYPE.keys()
        self.status_value_list = sdp_pb2.KEY_MAP_STATUS_TYPE.values()
        self.StatusComboBox.insertItems(0, QStringList(self.status_name_list))

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.response.result = True
        msg.response.last_response = True
        msg.response.key_check.status = self.status_value_list[self.StatusComboBox.currentIndex()]

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.StatusComboBox.setCurrentIndex(self.status_value_list.index(msg.response.key_check.status))

class ReqKeyMapCheckDialog(QDialog, ui_req_keymapcheck.Ui_Dialog):
    def __init__(self, parent=None):
        super(ReqKeyMapCheckDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"钥匙映射域校验请求")

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.request.key_map_check.time = int(self.TimelineEdit.text())

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.TimelineEdit.setText(str(msg.request.key_map_check.time))


class RepKeyMapCheckDialog(QDialog, ui_rep_keymapcheck.Ui_Dialog):
    def __init__(self, parent=None):
        super(RepKeyMapCheckDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"钥匙映射域校验响应")
        self.status_name_list = sdp_pb2.KEY_MAP_STATUS_TYPE.keys()
        self.status_value_list = sdp_pb2.KEY_MAP_STATUS_TYPE.values()
        self.StatusComboBox.insertItems(0, QStringList(self.status_name_list))

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.response.result = True
        msg.response.last_response = True
        msg.response.key_map_check.status = self.status_value_list[self.StatusComboBox.currentIndex()]

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.StatusComboBox.setCurrentIndex(self.status_value_list.index(msg.response.key_map_check.status))

class ReqKeyMapSyncDialog(QDialog, ui_req_keymapsync.Ui_Dialog):
    def __init__(self, parent=None):
        super(ReqKeyMapSyncDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"钥匙映射域同步请求")

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.request.key_map_sync.map = str(self.MapTextEdit.toPlainText())
        msg.request.key_map_sync.time = int(self.TimelineEdit.text())

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.MapTextEdit.setText(str(msg.request.key_map_sync.map))
        self.TimelineEdit.setText(str(msg.request.key_map_sync.time))


class RepKeyMapSyncDialog(QDialog, ui_rep_keymapsync.Ui_Dialog):
    def __init__(self, parent=None):
        super(RepKeyMapSyncDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"钥匙映射域同步响应")
        self.status_name_list = sdp_pb2.KEY_MAP_STATUS_TYPE.keys()
        self.status_value_list = sdp_pb2.KEY_MAP_STATUS_TYPE.values()
        self.StatusComboBox.insertItems(0, QStringList(self.status_name_list))

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.response.result = True
        msg.response.last_response = True
        msg.response.key_map_sync.status = self.status_value_list[self.StatusComboBox.currentIndex()]

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.StatusComboBox.setCurrentIndex(self.status_value_list.index(msg.response.key_map_sync.status))

class ReqPhoneCheckDialog(QDialog, ui_req_phonecheck.Ui_Dialog):
    def __init__(self, parent=None):
        super(ReqPhoneCheckDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"电话校验请求")

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.request.phone_check.id = int(self.IDlineEdit.text())
        msg.request.phone_check.time = int(self.TimelineEdit.text())

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.IDlineEdit.setText(str(msg.request.phone_check.id))
        self.TimelineEdit.setText(str(msg.request.phone_check.time))


class RepPhoneCheckDialog(QDialog, ui_rep_phonecheck.Ui_Dialog):
    def __init__(self, parent=None):
        super(RepPhoneCheckDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"电话校验响应")
        self.status_name_list = sdp_pb2.PHONE_MAP_STATUS_TYPE.keys()
        self.status_value_list = sdp_pb2.PHONE_MAP_STATUS_TYPE.values()
        self.StatusComboBox.insertItems(0, QStringList(self.status_name_list))

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.response.result = True
        msg.response.last_response = True
        msg.response.phone_check.status = self.status_value_list[self.StatusComboBox.currentIndex()]

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.StatusComboBox.setCurrentIndex(self.status_value_list.index(msg.response.phone_check.status))

class ReqPhoneMapCheckDialog(QDialog, ui_req_phonemapcheck.Ui_Dialog):
    def __init__(self, parent=None):
        super(ReqPhoneMapCheckDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"电话映射域校验请求")

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.request.phone_map_check.time = int(self.TimelineEdit.text())

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.TimelineEdit.setText(str(msg.request.phone_map_check.time))


class RepPhoneMapCheckDialog(QDialog, ui_rep_phonemapcheck.Ui_Dialog):
    def __init__(self, parent=None):
        super(RepPhoneMapCheckDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"电话映射域校验响应")
        self.status_name_list = sdp_pb2.PHONE_MAP_STATUS_TYPE.keys()
        self.status_value_list = sdp_pb2.PHONE_MAP_STATUS_TYPE.values()
        self.StatusComboBox.insertItems(0, QStringList(self.status_name_list))

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.response.result = True
        msg.response.last_response = True
        msg.response.phone_map_check.status = self.status_value_list[self.StatusComboBox.currentIndex()]

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.StatusComboBox.setCurrentIndex(self.status_value_list.index(msg.response.phone_map_check.status))

class ReqPhoneMapSyncDialog(QDialog, ui_req_phonemapsync.Ui_Dialog):
    def __init__(self, parent=None):
        super(ReqPhoneMapSyncDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"电话映射域同步请求")

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.request.phone_map_sync.map = str(self.MapTextEdit.toPlainText())
        msg.request.phone_map_sync.time = int(self.TimelineEdit.text())

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.MapTextEdit.setText(str(msg.request.phone_map_sync.map))
        self.TimelineEdit.setText(str(msg.request.phone_map_sync.time))


class RepPhoneMapSyncDialog(QDialog, ui_rep_phonemapsync.Ui_Dialog):
    def __init__(self, parent=None):
        super(RepPhoneMapSyncDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"电话映射域同步响应")
        self.status_name_list = sdp_pb2.PHONE_MAP_STATUS_TYPE.keys()
        self.status_value_list = sdp_pb2.PHONE_MAP_STATUS_TYPE.values()
        self.StatusComboBox.insertItems(0, QStringList(self.status_name_list))

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.response.result = True
        msg.response.last_response = True
        msg.response.phone_map_sync.status = self.status_value_list[self.StatusComboBox.currentIndex()]

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.StatusComboBox.setCurrentIndex(self.status_value_list.index(msg.response.phone_map_sync.status))


class ReqLogCheckDialog(QDialog, ui_req_logcheck.Ui_Dialog):
    def __init__(self, parent=None):
        super(ReqLogCheckDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"记录校验请求")

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.request.log_check.id = int(self.IDlineEdit.text())
        msg.request.log_check.time = int(self.TimelineEdit.text())

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.IDlineEdit.setText(str(msg.request.log_check.id))
        self.TimelineEdit.setText(str(msg.request.log_check.time))


class RepLogCheckDialog(QDialog, ui_rep_logcheck.Ui_Dialog):
    def __init__(self, parent=None):
        super(RepLogCheckDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"记录校验响应")
        self.status_name_list = sdp_pb2.LOG_MAP_STATUS_TYPE.keys()
        self.status_value_list = sdp_pb2.LOG_MAP_STATUS_TYPE.values()
        self.StatusComboBox.insertItems(0, QStringList(self.status_name_list))

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.response.result = True
        msg.response.last_response = True
        msg.response.log_check.status = self.status_value_list[self.StatusComboBox.currentIndex()]

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.StatusComboBox.setCurrentIndex(self.status_value_list.index(msg.response.log_check.status))

class ReqLogMapCheckDialog(QDialog, ui_req_logmapcheck.Ui_Dialog):
    def __init__(self, parent=None):
        super(ReqLogMapCheckDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"记录映射域校验请求")

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.request.log_map_check.time = int(self.TimelineEdit.text())

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.TimelineEdit.setText(str(msg.request.log_map_check.time))


class RepLogMapCheckDialog(QDialog, ui_rep_logmapcheck.Ui_Dialog):
    def __init__(self, parent=None):
        super(RepLogMapCheckDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"记录映射域校验响应")
        self.status_name_list = sdp_pb2.LOG_MAP_STATUS_TYPE.keys()
        self.status_value_list = sdp_pb2.LOG_MAP_STATUS_TYPE.values()
        self.StatusComboBox.insertItems(0, QStringList(self.status_name_list))

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.response.result = True
        msg.response.last_response = True
        msg.response.log_map_check.status = self.status_value_list[self.StatusComboBox.currentIndex()]

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.StatusComboBox.setCurrentIndex(self.status_value_list.index(msg.response.log_map_check.status))

class ReqLogMapSyncDialog(QDialog, ui_req_logmapsync.Ui_Dialog):
    def __init__(self, parent=None):
        super(ReqLogMapSyncDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"记录映射域同步请求")

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.request.log_map_sync.map = str(self.MapTextEdit.toPlainText())
        msg.request.log_map_sync.time = int(self.TimelineEdit.text())

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.MapTextEdit.setText(str(msg.request.log_map_sync.map))
        self.TimelineEdit.setText(str(msg.request.log_map_sync.time))


class RepLogMapSyncDialog(QDialog, ui_rep_logmapsync.Ui_Dialog):
    def __init__(self, parent=None):
        super(RepLogMapSyncDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u"记录映射域同步响应")
        self.status_name_list = sdp_pb2.LOG_MAP_STATUS_TYPE.keys()
        self.status_value_list = sdp_pb2.LOG_MAP_STATUS_TYPE.values()
        self.StatusComboBox.insertItems(0, QStringList(self.status_name_list))

    def pack(self, msg):
        msg.sequence = int(self.SequencelineEdit.text())
        msg.response.result = True
        msg.response.last_response = True
        msg.response.log_map_sync.status = self.status_value_list[self.StatusComboBox.currentIndex()]

    def unpack(self, msg):
        self.SequencelineEdit.setText(str(msg.sequence))
        self.StatusComboBox.setCurrentIndex(self.status_value_list.index(msg.response.log_map_sync.status))


dlg_dict = {
    "MSG_REQ_LOGIN": ReqLoginDialog,
    "MSG_REP_LOGIN": RepLoginDialog,
    "MSG_REQ_LOGOUT": ReqLogoutDialog,
    "MSG_REP_LOGOUT": RepLogoutDialog,
    "MSG_REQ_KEEP_ALIVE": ReqKeepAliveDialog,
    "MSG_REP_KEEP_ALIVE": RepKeepAliveDialog,
    "MSG_REQ_WORK_ALARM": ReqWorkAlarmDialog,
    "MSG_REP_WORK_ALARM": RepWorkAlarmDialog,
    "MSG_REQ_FAULT_ALARM": ReqFaultAlarmDialog,
    "MSG_REP_FAULT_ALARM": RepFaultAlarmDialog,
    "MSG_REQ_BATTERY": ReqBatteryDialog,
    "MSG_REP_BATTERY": RepBatteryDialog,
    "MSG_REQ_OPEN": ReqOpenDialog,
    "MSG_REP_OPEN": RepOpenDialog,
    "MSG_REQ_PHONE_ADD": ReqPhoneAddDialog,
    "MSG_REP_PHONE_ADD": RepPhoneAddDialog,
    "MSG_REQ_PHONE_MODIFY": ReqPhoneModifyDialog,
    "MSG_REP_PHONE_MODIFY": RepPhoneModifyDialog,
    "MSG_REQ_PHONE_DELETE": ReqPhoneDeleteDialog,
    "MSG_REP_PHONE_DELETE": RepPhoneDeleteDialog,
    "MSG_REQ_KEY_ADD": ReqKeyAddDialog,
    "MSG_REP_KEY_ADD": RepKeyAddDialog,
    "MSG_REQ_KEY_MODIFY": ReqKeyModifyDialog,
    "MSG_REP_KEY_MODIFY": RepKeyModifyDialog,
    "MSG_REQ_KEY_DELETE": ReqKeyDeleteDialog,
    "MSG_REP_KEY_DELETE": RepKeyDeleteDialog,

    "MSG_REQ_ACCOUNT_ADD": ReqAccountAddDialog,
    "MSG_REP_ACCOUNT_ADD": RepAccountAddDialog,
    "MSG_REQ_ACCOUNT_MODIFY": ReqAccountModifyDialog,
    "MSG_REP_ACCOUNT_MODIFY": RepAccountModifyDialog,
    "MSG_REQ_ACCOUNT_DELETE": ReqAccountDeleteDialog,
    "MSG_REP_ACCOUNT_DELETE": RepAccountDeleteDialog,

    "MSG_REQ_ACCOUNT_TO_KEY": ReqAccountToKeyDialog,
    "MSG_REP_ACCOUNT_TO_KEY": RepAccountToKeyDialog,
    "MSG_REQ_ACCOUNT_TO_PHONE": ReqAccountToPhoneDialog,
    "MSG_REP_ACCOUNT_TO_PHONE": RepAccountToPhoneDialog,
    "MSG_REQ_MOTOR" : ReqMotorDialog,
    "MSG_REP_MOTOR" : RepMotorDialog,
    "MSG_REQ_TIME": ReqTimeDialog,
    "MSG_REP_TIME": RepTimeDialog,
    "MSG_REQ_PASSWORD": ReqPasswordDialog,
    "MSG_REP_PASSWORD": RepPasswordDialog,
    "MSG_REQ_ACCOUNT_CHECK": ReqAccountCheckDialog,
    "MSG_REP_ACCOUNT_CHECK": RepAccountCheckDialog,
    "MSG_REQ_ACCOUNT_MAP_CHECK": ReqAccountMapCheckDialog,
    "MSG_REP_ACCOUNT_MAP_CHECK": RepAccountMapCheckDialog,
    "MSG_REQ_ACCOUNT_MAP_SYNC": ReqAccountMapSyncDialog,
    "MSG_REP_ACCOUNT_MAP_SYNC": RepAccountMapSyncDialog,
    "MSG_REQ_KEY_CHECK": ReqKeyCheckDialog,
    "MSG_REP_KEY_CHECK": RepKeyCheckDialog,
    "MSG_REQ_KEY_MAP_CHECK": ReqKeyMapCheckDialog,
    "MSG_REP_KEY_MAP_CHECK": RepKeyMapCheckDialog,
    "MSG_REQ_KEY_MAP_SYNC": ReqKeyMapSyncDialog,
    "MSG_REP_KEY_MAP_SYNC": RepKeyMapSyncDialog,

    "MSG_REQ_PHONE_CHECK": ReqPhoneCheckDialog,
    "MSG_REP_PHONE_CHECK": RepPhoneCheckDialog,
    "MSG_REQ_PHONE_MAP_CHECK": ReqPhoneMapCheckDialog,
    "MSG_REP_PHONE_MAP_CHECK": RepPhoneMapCheckDialog,
    "MSG_REQ_PHONE_MAP_SYNC": ReqPhoneMapSyncDialog,
    "MSG_REP_PHONE_MAP_SYNC": RepPhoneMapSyncDialog,

    "MSG_REQ_LOG_CHECK": ReqLogCheckDialog,
    "MSG_REP_LOG_CHECK": RepLogCheckDialog,
    "MSG_REQ_LOG_MAP_CHECK": ReqLogMapCheckDialog,
    "MSG_REP_LOG_MAP_CHECK": RepLogMapCheckDialog,
    "MSG_REQ_LOG_MAP_SYNC": ReqLogMapSyncDialog,
    "MSG_REP_LOG_MAP_SYNC": RepLogMapSyncDialog,
}



class MyMainWindow(QMainWindow, ui_demo_main.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.comboBox.clear()
        self.comboBox.insertItems(0, QStringList(name_list))
        self.epushButton.clicked.connect(self.encode)
        self.dpushButton.clicked.connect(self.decode)

    def decode(self):
        try:
            dmsg.ParseFromString(binascii.unhexlify(str(self.textEdit.toPlainText())))
        except DecodeError or TypeError, error:
            QMessageBox.information(None, u"解码错误", str(error), QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            return
        index = msg_type_value_list.index(dmsg.msg_type)
        dlg = None
        try:
            dlg = (dlg_dict.get(msg_type_name_list[index], None))()
        except IndexError and TypeError:
            dlg == None

        if dlg:
            dlg.unpack(dmsg)
            dlg.exec_()

    def encode(self):
        dmsg.Clear()
        index = self.comboBox.currentIndex()
        dlg = None
        try:
            dlg = (dlg_dict.get(msg_type_name_list[index], None))()
        except IndexError and TypeError:
            dlg == None

        if dlg:
            if dlg.exec_():
                self.textEdit.clear()
                dmsg.msg_type = msg_type_value_list[index]
                dlg.pack(dmsg)
                self.textEdit.setText(binascii.hexlify(dmsg.SerializeToString()))
        else:
            dmsg.msg_type = msg_type_value_list[index]
            self.textEdit.setText(binascii.hexlify(dmsg.SerializeToString()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    print len(dlg_dict.keys())

    for i,v in enumerate(msg_type_name_list):
        dlg = None
        try:
            dlg = dlg_dict.get(v, None)()
        except TypeError:
            name_list.append(v + u'/未实现')
            continue
        name_list.append(v + '/' + dlg.windowTitle())
    print name_list
    mydlg = MyMainWindow()
    mydlg.show()

    sys.exit(app.exec_())