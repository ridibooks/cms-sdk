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
import logging
from .ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport


class Iface(object):
    def getAdminIdsFromTags(self, tag_ids):
        """
        Parameters:
         - tag_ids
        """
        pass

    def getAdminTagMenus(self, tag_id):
        """
        Parameters:
         - tag_id
        """
        pass

    def getMappedAdminMenuHashes(self, check_url, tag_id):
        """
        Parameters:
         - check_url
         - tag_id
        """
        pass


class Client(Iface):
    def __init__(self, iprot, oprot=None):
        self._iprot = self._oprot = iprot
        if oprot is not None:
            self._oprot = oprot
        self._seqid = 0

    def getAdminIdsFromTags(self, tag_ids):
        """
        Parameters:
         - tag_ids
        """
        self.send_getAdminIdsFromTags(tag_ids)
        return self.recv_getAdminIdsFromTags()

    def send_getAdminIdsFromTags(self, tag_ids):
        self._oprot.writeMessageBegin('getAdminIdsFromTags', TMessageType.CALL, self._seqid)
        args = getAdminIdsFromTags_args()
        args.tag_ids = tag_ids
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getAdminIdsFromTags(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getAdminIdsFromTags_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.userException is not None:
            raise result.userException
        if result.systemException is not None:
            raise result.systemException
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getAdminIdsFromTags failed: unknown result")

    def getAdminTagMenus(self, tag_id):
        """
        Parameters:
         - tag_id
        """
        self.send_getAdminTagMenus(tag_id)
        return self.recv_getAdminTagMenus()

    def send_getAdminTagMenus(self, tag_id):
        self._oprot.writeMessageBegin('getAdminTagMenus', TMessageType.CALL, self._seqid)
        args = getAdminTagMenus_args()
        args.tag_id = tag_id
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getAdminTagMenus(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getAdminTagMenus_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.userException is not None:
            raise result.userException
        if result.systemException is not None:
            raise result.systemException
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getAdminTagMenus failed: unknown result")

    def getMappedAdminMenuHashes(self, check_url, tag_id):
        """
        Parameters:
         - check_url
         - tag_id
        """
        self.send_getMappedAdminMenuHashes(check_url, tag_id)
        return self.recv_getMappedAdminMenuHashes()

    def send_getMappedAdminMenuHashes(self, check_url, tag_id):
        self._oprot.writeMessageBegin('getMappedAdminMenuHashes', TMessageType.CALL, self._seqid)
        args = getMappedAdminMenuHashes_args()
        args.check_url = check_url
        args.tag_id = tag_id
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getMappedAdminMenuHashes(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getMappedAdminMenuHashes_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.userException is not None:
            raise result.userException
        if result.systemException is not None:
            raise result.systemException
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getMappedAdminMenuHashes failed: unknown result")


class Processor(Iface, TProcessor):
    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap["getAdminIdsFromTags"] = Processor.process_getAdminIdsFromTags
        self._processMap["getAdminTagMenus"] = Processor.process_getAdminTagMenus
        self._processMap["getMappedAdminMenuHashes"] = Processor.process_getMappedAdminMenuHashes

    def process(self, iprot, oprot):
        (name, type, seqid) = iprot.readMessageBegin()
        if name not in self._processMap:
            iprot.skip(TType.STRUCT)
            iprot.readMessageEnd()
            x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
            oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
            x.write(oprot)
            oprot.writeMessageEnd()
            oprot.trans.flush()
            return
        else:
            self._processMap[name](self, seqid, iprot, oprot)
        return True

    def process_getAdminIdsFromTags(self, seqid, iprot, oprot):
        args = getAdminIdsFromTags_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getAdminIdsFromTags_result()
        try:
            result.success = self._handler.getAdminIdsFromTags(args.tag_ids)
            msg_type = TMessageType.REPLY
        except (TTransport.TTransportException, KeyboardInterrupt, SystemExit):
            raise
        except ridi.cms.thrift.Errors.ttypes.UserException as userException:
            msg_type = TMessageType.REPLY
            result.userException = userException
        except ridi.cms.thrift.Errors.ttypes.SystemException as systemException:
            msg_type = TMessageType.REPLY
            result.systemException = systemException
        except Exception as ex:
            msg_type = TMessageType.EXCEPTION
            logging.exception(ex)
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getAdminIdsFromTags", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getAdminTagMenus(self, seqid, iprot, oprot):
        args = getAdminTagMenus_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getAdminTagMenus_result()
        try:
            result.success = self._handler.getAdminTagMenus(args.tag_id)
            msg_type = TMessageType.REPLY
        except (TTransport.TTransportException, KeyboardInterrupt, SystemExit):
            raise
        except ridi.cms.thrift.Errors.ttypes.UserException as userException:
            msg_type = TMessageType.REPLY
            result.userException = userException
        except ridi.cms.thrift.Errors.ttypes.SystemException as systemException:
            msg_type = TMessageType.REPLY
            result.systemException = systemException
        except Exception as ex:
            msg_type = TMessageType.EXCEPTION
            logging.exception(ex)
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getAdminTagMenus", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getMappedAdminMenuHashes(self, seqid, iprot, oprot):
        args = getMappedAdminMenuHashes_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getMappedAdminMenuHashes_result()
        try:
            result.success = self._handler.getMappedAdminMenuHashes(args.check_url, args.tag_id)
            msg_type = TMessageType.REPLY
        except (TTransport.TTransportException, KeyboardInterrupt, SystemExit):
            raise
        except ridi.cms.thrift.Errors.ttypes.UserException as userException:
            msg_type = TMessageType.REPLY
            result.userException = userException
        except ridi.cms.thrift.Errors.ttypes.SystemException as systemException:
            msg_type = TMessageType.REPLY
            result.systemException = systemException
        except Exception as ex:
            msg_type = TMessageType.EXCEPTION
            logging.exception(ex)
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getMappedAdminMenuHashes", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

# HELPER FUNCTIONS AND STRUCTURES


class getAdminIdsFromTags_args(object):
    """
    Attributes:
     - tag_ids
    """

    thrift_spec = (
        None,  # 0
        (1, TType.LIST, 'tag_ids', (TType.I32, None, False), None, ),  # 1
    )

    def __init__(self, tag_ids=None,):
        self.tag_ids = tag_ids

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
                if ftype == TType.LIST:
                    self.tag_ids = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = iprot.readI32()
                        self.tag_ids.append(_elem5)
                    iprot.readListEnd()
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
        oprot.writeStructBegin('getAdminIdsFromTags_args')
        if self.tag_ids is not None:
            oprot.writeFieldBegin('tag_ids', TType.LIST, 1)
            oprot.writeListBegin(TType.I32, len(self.tag_ids))
            for iter6 in self.tag_ids:
                oprot.writeI32(iter6)
            oprot.writeListEnd()
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


class getAdminIdsFromTags_result(object):
    """
    Attributes:
     - success
     - userException
     - systemException
    """

    thrift_spec = (
        (0, TType.LIST, 'success', (TType.STRING, 'UTF8', False), None, ),  # 0
        (1, TType.STRUCT, 'userException', (ridi.cms.thrift.Errors.ttypes.UserException, ridi.cms.thrift.Errors.ttypes.UserException.thrift_spec), None, ),  # 1
        (2, TType.STRUCT, 'systemException', (ridi.cms.thrift.Errors.ttypes.SystemException, ridi.cms.thrift.Errors.ttypes.SystemException.thrift_spec), None, ),  # 2
    )

    def __init__(self, success=None, userException=None, systemException=None,):
        self.success = success
        self.userException = userException
        self.systemException = systemException

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.LIST:
                    self.success = []
                    (_etype10, _size7) = iprot.readListBegin()
                    for _i11 in range(_size7):
                        _elem12 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.success.append(_elem12)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.userException = ridi.cms.thrift.Errors.ttypes.UserException()
                    self.userException.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.systemException = ridi.cms.thrift.Errors.ttypes.SystemException()
                    self.systemException.read(iprot)
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
        oprot.writeStructBegin('getAdminIdsFromTags_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRING, len(self.success))
            for iter13 in self.success:
                oprot.writeString(iter13.encode('utf-8') if sys.version_info[0] == 2 else iter13)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.userException is not None:
            oprot.writeFieldBegin('userException', TType.STRUCT, 1)
            self.userException.write(oprot)
            oprot.writeFieldEnd()
        if self.systemException is not None:
            oprot.writeFieldBegin('systemException', TType.STRUCT, 2)
            self.systemException.write(oprot)
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


class getAdminTagMenus_args(object):
    """
    Attributes:
     - tag_id
    """

    thrift_spec = (
        None,  # 0
        (1, TType.I32, 'tag_id', None, None, ),  # 1
    )

    def __init__(self, tag_id=None,):
        self.tag_id = tag_id

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
                if ftype == TType.I32:
                    self.tag_id = iprot.readI32()
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
        oprot.writeStructBegin('getAdminTagMenus_args')
        if self.tag_id is not None:
            oprot.writeFieldBegin('tag_id', TType.I32, 1)
            oprot.writeI32(self.tag_id)
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


class getAdminTagMenus_result(object):
    """
    Attributes:
     - success
     - userException
     - systemException
    """

    thrift_spec = (
        (0, TType.LIST, 'success', (TType.I32, None, False), None, ),  # 0
        (1, TType.STRUCT, 'userException', (ridi.cms.thrift.Errors.ttypes.UserException, ridi.cms.thrift.Errors.ttypes.UserException.thrift_spec), None, ),  # 1
        (2, TType.STRUCT, 'systemException', (ridi.cms.thrift.Errors.ttypes.SystemException, ridi.cms.thrift.Errors.ttypes.SystemException.thrift_spec), None, ),  # 2
    )

    def __init__(self, success=None, userException=None, systemException=None,):
        self.success = success
        self.userException = userException
        self.systemException = systemException

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.LIST:
                    self.success = []
                    (_etype17, _size14) = iprot.readListBegin()
                    for _i18 in range(_size14):
                        _elem19 = iprot.readI32()
                        self.success.append(_elem19)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.userException = ridi.cms.thrift.Errors.ttypes.UserException()
                    self.userException.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.systemException = ridi.cms.thrift.Errors.ttypes.SystemException()
                    self.systemException.read(iprot)
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
        oprot.writeStructBegin('getAdminTagMenus_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.I32, len(self.success))
            for iter20 in self.success:
                oprot.writeI32(iter20)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.userException is not None:
            oprot.writeFieldBegin('userException', TType.STRUCT, 1)
            self.userException.write(oprot)
            oprot.writeFieldEnd()
        if self.systemException is not None:
            oprot.writeFieldBegin('systemException', TType.STRUCT, 2)
            self.systemException.write(oprot)
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


class getMappedAdminMenuHashes_args(object):
    """
    Attributes:
     - check_url
     - tag_id
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'check_url', 'UTF8', None, ),  # 1
        (2, TType.I32, 'tag_id', None, None, ),  # 2
    )

    def __init__(self, check_url=None, tag_id=None,):
        self.check_url = check_url
        self.tag_id = tag_id

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
                    self.check_url = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.tag_id = iprot.readI32()
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
        oprot.writeStructBegin('getMappedAdminMenuHashes_args')
        if self.check_url is not None:
            oprot.writeFieldBegin('check_url', TType.STRING, 1)
            oprot.writeString(self.check_url.encode('utf-8') if sys.version_info[0] == 2 else self.check_url)
            oprot.writeFieldEnd()
        if self.tag_id is not None:
            oprot.writeFieldBegin('tag_id', TType.I32, 2)
            oprot.writeI32(self.tag_id)
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


class getMappedAdminMenuHashes_result(object):
    """
    Attributes:
     - success
     - userException
     - systemException
    """

    thrift_spec = (
        (0, TType.LIST, 'success', (TType.STRING, 'UTF8', False), None, ),  # 0
        (1, TType.STRUCT, 'userException', (ridi.cms.thrift.Errors.ttypes.UserException, ridi.cms.thrift.Errors.ttypes.UserException.thrift_spec), None, ),  # 1
        (2, TType.STRUCT, 'systemException', (ridi.cms.thrift.Errors.ttypes.SystemException, ridi.cms.thrift.Errors.ttypes.SystemException.thrift_spec), None, ),  # 2
    )

    def __init__(self, success=None, userException=None, systemException=None,):
        self.success = success
        self.userException = userException
        self.systemException = systemException

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.LIST:
                    self.success = []
                    (_etype24, _size21) = iprot.readListBegin()
                    for _i25 in range(_size21):
                        _elem26 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.success.append(_elem26)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.userException = ridi.cms.thrift.Errors.ttypes.UserException()
                    self.userException.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.systemException = ridi.cms.thrift.Errors.ttypes.SystemException()
                    self.systemException.read(iprot)
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
        oprot.writeStructBegin('getMappedAdminMenuHashes_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRING, len(self.success))
            for iter27 in self.success:
                oprot.writeString(iter27.encode('utf-8') if sys.version_info[0] == 2 else iter27)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.userException is not None:
            oprot.writeFieldBegin('userException', TType.STRUCT, 1)
            self.userException.write(oprot)
            oprot.writeFieldEnd()
        if self.systemException is not None:
            oprot.writeFieldBegin('systemException', TType.STRUCT, 2)
            self.systemException.write(oprot)
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
