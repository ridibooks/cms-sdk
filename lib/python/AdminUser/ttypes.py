# -*- coding: utf-8 -*-
#
# Autogenerated by Thrift Compiler (0.10.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:coding=utf-8
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
import sys
import Errors.ttypes
import AdminTag.ttypes
import AdminMenu.ttypes

from thrift.transport import TTransport


class AdminUser(object):
    """
    AdminUser 엔티티

    Attributes:
     - id
     - name
     - passwd
     - team
     - is_use
     - reg_date
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'id', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'name', 'UTF8', None, ),  # 2
        (3, TType.STRING, 'passwd', 'UTF8', None, ),  # 3
        (4, TType.STRING, 'team', 'UTF8', None, ),  # 4
        (5, TType.BOOL, 'is_use', None, None, ),  # 5
        (6, TType.STRING, 'reg_date', 'UTF8', None, ),  # 6
    )

    def __init__(self, id=None, name=None, passwd=None, team=None, is_use=None, reg_date=None,):
        self.id = id
        self.name = name
        self.passwd = passwd
        self.team = team
        self.is_use = is_use
        self.reg_date = reg_date

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.id = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.name = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.passwd = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.team = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.BOOL:
                    self.is_use = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.reg_date = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('AdminUser')
        if self.id is not None:
            oprot.writeFieldBegin('id', TType.STRING, 1)
            oprot.writeString(self.id.encode('utf-8') if sys.version_info[0] == 2 else self.id)
            oprot.writeFieldEnd()
        if self.name is not None:
            oprot.writeFieldBegin('name', TType.STRING, 2)
            oprot.writeString(self.name.encode('utf-8') if sys.version_info[0] == 2 else self.name)
            oprot.writeFieldEnd()
        if self.passwd is not None:
            oprot.writeFieldBegin('passwd', TType.STRING, 3)
            oprot.writeString(self.passwd.encode('utf-8') if sys.version_info[0] == 2 else self.passwd)
            oprot.writeFieldEnd()
        if self.team is not None:
            oprot.writeFieldBegin('team', TType.STRING, 4)
            oprot.writeString(self.team.encode('utf-8') if sys.version_info[0] == 2 else self.team)
            oprot.writeFieldEnd()
        if self.is_use is not None:
            oprot.writeFieldBegin('is_use', TType.BOOL, 5)
            oprot.writeBool(self.is_use)
            oprot.writeFieldEnd()
        if self.reg_date is not None:
            oprot.writeFieldBegin('reg_date', TType.STRING, 6)
            oprot.writeString(self.reg_date.encode('utf-8') if sys.version_info[0] == 2 else self.reg_date)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
