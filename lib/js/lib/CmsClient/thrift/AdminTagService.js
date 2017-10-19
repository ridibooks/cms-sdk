//
// Autogenerated by Thrift Compiler (0.10.0)
//
// DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
//
"use strict";

var thrift = require('thrift');
var Thrift = thrift.Thrift;
var Q = thrift.Q;

var Errors_ttypes = require('./Errors_types');
var AdminMenu_ttypes = require('./AdminMenu_types');


var ttypes = require('./AdminTag_types');
//HELPER FUNCTIONS AND STRUCTURES

var AdminTagService_getAdminIdsFromTags_args = function(args) {
  this.tag_ids = null;
  if (args) {
    if (args.tag_ids !== undefined && args.tag_ids !== null) {
      this.tag_ids = Thrift.copyList(args.tag_ids, [null]);
    }
  }
};
AdminTagService_getAdminIdsFromTags_args.prototype = {};
AdminTagService_getAdminIdsFromTags_args.prototype.read = function(input) {
  input.readStructBegin();
  while (true)
  {
    var ret = input.readFieldBegin();
    var fname = ret.fname;
    var ftype = ret.ftype;
    var fid = ret.fid;
    if (ftype == Thrift.Type.STOP) {
      break;
    }
    switch (fid)
    {
      case 1:
      if (ftype == Thrift.Type.LIST) {
        var _size0 = 0;
        var _rtmp34;
        this.tag_ids = [];
        var _etype3 = 0;
        _rtmp34 = input.readListBegin();
        _etype3 = _rtmp34.etype;
        _size0 = _rtmp34.size;
        for (var _i5 = 0; _i5 < _size0; ++_i5)
        {
          var elem6 = null;
          elem6 = input.readI32();
          this.tag_ids.push(elem6);
        }
        input.readListEnd();
      } else {
        input.skip(ftype);
      }
      break;
      case 0:
        input.skip(ftype);
        break;
      default:
        input.skip(ftype);
    }
    input.readFieldEnd();
  }
  input.readStructEnd();
  return;
};

AdminTagService_getAdminIdsFromTags_args.prototype.write = function(output) {
  output.writeStructBegin('AdminTagService_getAdminIdsFromTags_args');
  if (this.tag_ids !== null && this.tag_ids !== undefined) {
    output.writeFieldBegin('tag_ids', Thrift.Type.LIST, 1);
    output.writeListBegin(Thrift.Type.I32, this.tag_ids.length);
    for (var iter7 in this.tag_ids)
    {
      if (this.tag_ids.hasOwnProperty(iter7))
      {
        iter7 = this.tag_ids[iter7];
        output.writeI32(iter7);
      }
    }
    output.writeListEnd();
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

var AdminTagService_getAdminIdsFromTags_result = function(args) {
  this.success = null;
  this.userException = null;
  this.systemException = null;
  if (args instanceof Errors_ttypes.UserException) {
    this.userException = args;
    return;
  }
  if (args instanceof Errors_ttypes.SystemException) {
    this.systemException = args;
    return;
  }
  if (args) {
    if (args.success !== undefined && args.success !== null) {
      this.success = Thrift.copyList(args.success, [null]);
    }
    if (args.userException !== undefined && args.userException !== null) {
      this.userException = args.userException;
    }
    if (args.systemException !== undefined && args.systemException !== null) {
      this.systemException = args.systemException;
    }
  }
};
AdminTagService_getAdminIdsFromTags_result.prototype = {};
AdminTagService_getAdminIdsFromTags_result.prototype.read = function(input) {
  input.readStructBegin();
  while (true)
  {
    var ret = input.readFieldBegin();
    var fname = ret.fname;
    var ftype = ret.ftype;
    var fid = ret.fid;
    if (ftype == Thrift.Type.STOP) {
      break;
    }
    switch (fid)
    {
      case 0:
      if (ftype == Thrift.Type.LIST) {
        var _size8 = 0;
        var _rtmp312;
        this.success = [];
        var _etype11 = 0;
        _rtmp312 = input.readListBegin();
        _etype11 = _rtmp312.etype;
        _size8 = _rtmp312.size;
        for (var _i13 = 0; _i13 < _size8; ++_i13)
        {
          var elem14 = null;
          elem14 = input.readString();
          this.success.push(elem14);
        }
        input.readListEnd();
      } else {
        input.skip(ftype);
      }
      break;
      case 1:
      if (ftype == Thrift.Type.STRUCT) {
        this.userException = new Errors_ttypes.UserException();
        this.userException.read(input);
      } else {
        input.skip(ftype);
      }
      break;
      case 2:
      if (ftype == Thrift.Type.STRUCT) {
        this.systemException = new Errors_ttypes.SystemException();
        this.systemException.read(input);
      } else {
        input.skip(ftype);
      }
      break;
      default:
        input.skip(ftype);
    }
    input.readFieldEnd();
  }
  input.readStructEnd();
  return;
};

AdminTagService_getAdminIdsFromTags_result.prototype.write = function(output) {
  output.writeStructBegin('AdminTagService_getAdminIdsFromTags_result');
  if (this.success !== null && this.success !== undefined) {
    output.writeFieldBegin('success', Thrift.Type.LIST, 0);
    output.writeListBegin(Thrift.Type.STRING, this.success.length);
    for (var iter15 in this.success)
    {
      if (this.success.hasOwnProperty(iter15))
      {
        iter15 = this.success[iter15];
        output.writeString(iter15);
      }
    }
    output.writeListEnd();
    output.writeFieldEnd();
  }
  if (this.userException !== null && this.userException !== undefined) {
    output.writeFieldBegin('userException', Thrift.Type.STRUCT, 1);
    this.userException.write(output);
    output.writeFieldEnd();
  }
  if (this.systemException !== null && this.systemException !== undefined) {
    output.writeFieldBegin('systemException', Thrift.Type.STRUCT, 2);
    this.systemException.write(output);
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

var AdminTagService_getAdminTagMenus_args = function(args) {
  this.tag_id = null;
  if (args) {
    if (args.tag_id !== undefined && args.tag_id !== null) {
      this.tag_id = args.tag_id;
    }
  }
};
AdminTagService_getAdminTagMenus_args.prototype = {};
AdminTagService_getAdminTagMenus_args.prototype.read = function(input) {
  input.readStructBegin();
  while (true)
  {
    var ret = input.readFieldBegin();
    var fname = ret.fname;
    var ftype = ret.ftype;
    var fid = ret.fid;
    if (ftype == Thrift.Type.STOP) {
      break;
    }
    switch (fid)
    {
      case 1:
      if (ftype == Thrift.Type.I32) {
        this.tag_id = input.readI32();
      } else {
        input.skip(ftype);
      }
      break;
      case 0:
        input.skip(ftype);
        break;
      default:
        input.skip(ftype);
    }
    input.readFieldEnd();
  }
  input.readStructEnd();
  return;
};

AdminTagService_getAdminTagMenus_args.prototype.write = function(output) {
  output.writeStructBegin('AdminTagService_getAdminTagMenus_args');
  if (this.tag_id !== null && this.tag_id !== undefined) {
    output.writeFieldBegin('tag_id', Thrift.Type.I32, 1);
    output.writeI32(this.tag_id);
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

var AdminTagService_getAdminTagMenus_result = function(args) {
  this.success = null;
  this.userException = null;
  this.systemException = null;
  if (args instanceof Errors_ttypes.UserException) {
    this.userException = args;
    return;
  }
  if (args instanceof Errors_ttypes.SystemException) {
    this.systemException = args;
    return;
  }
  if (args) {
    if (args.success !== undefined && args.success !== null) {
      this.success = Thrift.copyList(args.success, [null]);
    }
    if (args.userException !== undefined && args.userException !== null) {
      this.userException = args.userException;
    }
    if (args.systemException !== undefined && args.systemException !== null) {
      this.systemException = args.systemException;
    }
  }
};
AdminTagService_getAdminTagMenus_result.prototype = {};
AdminTagService_getAdminTagMenus_result.prototype.read = function(input) {
  input.readStructBegin();
  while (true)
  {
    var ret = input.readFieldBegin();
    var fname = ret.fname;
    var ftype = ret.ftype;
    var fid = ret.fid;
    if (ftype == Thrift.Type.STOP) {
      break;
    }
    switch (fid)
    {
      case 0:
      if (ftype == Thrift.Type.LIST) {
        var _size16 = 0;
        var _rtmp320;
        this.success = [];
        var _etype19 = 0;
        _rtmp320 = input.readListBegin();
        _etype19 = _rtmp320.etype;
        _size16 = _rtmp320.size;
        for (var _i21 = 0; _i21 < _size16; ++_i21)
        {
          var elem22 = null;
          elem22 = input.readI32();
          this.success.push(elem22);
        }
        input.readListEnd();
      } else {
        input.skip(ftype);
      }
      break;
      case 1:
      if (ftype == Thrift.Type.STRUCT) {
        this.userException = new Errors_ttypes.UserException();
        this.userException.read(input);
      } else {
        input.skip(ftype);
      }
      break;
      case 2:
      if (ftype == Thrift.Type.STRUCT) {
        this.systemException = new Errors_ttypes.SystemException();
        this.systemException.read(input);
      } else {
        input.skip(ftype);
      }
      break;
      default:
        input.skip(ftype);
    }
    input.readFieldEnd();
  }
  input.readStructEnd();
  return;
};

AdminTagService_getAdminTagMenus_result.prototype.write = function(output) {
  output.writeStructBegin('AdminTagService_getAdminTagMenus_result');
  if (this.success !== null && this.success !== undefined) {
    output.writeFieldBegin('success', Thrift.Type.LIST, 0);
    output.writeListBegin(Thrift.Type.I32, this.success.length);
    for (var iter23 in this.success)
    {
      if (this.success.hasOwnProperty(iter23))
      {
        iter23 = this.success[iter23];
        output.writeI32(iter23);
      }
    }
    output.writeListEnd();
    output.writeFieldEnd();
  }
  if (this.userException !== null && this.userException !== undefined) {
    output.writeFieldBegin('userException', Thrift.Type.STRUCT, 1);
    this.userException.write(output);
    output.writeFieldEnd();
  }
  if (this.systemException !== null && this.systemException !== undefined) {
    output.writeFieldBegin('systemException', Thrift.Type.STRUCT, 2);
    this.systemException.write(output);
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

var AdminTagService_getMappedAdminMenuHashes_args = function(args) {
  this.check_url = null;
  this.tag_id = null;
  if (args) {
    if (args.check_url !== undefined && args.check_url !== null) {
      this.check_url = args.check_url;
    }
    if (args.tag_id !== undefined && args.tag_id !== null) {
      this.tag_id = args.tag_id;
    }
  }
};
AdminTagService_getMappedAdminMenuHashes_args.prototype = {};
AdminTagService_getMappedAdminMenuHashes_args.prototype.read = function(input) {
  input.readStructBegin();
  while (true)
  {
    var ret = input.readFieldBegin();
    var fname = ret.fname;
    var ftype = ret.ftype;
    var fid = ret.fid;
    if (ftype == Thrift.Type.STOP) {
      break;
    }
    switch (fid)
    {
      case 1:
      if (ftype == Thrift.Type.STRING) {
        this.check_url = input.readString();
      } else {
        input.skip(ftype);
      }
      break;
      case 2:
      if (ftype == Thrift.Type.I32) {
        this.tag_id = input.readI32();
      } else {
        input.skip(ftype);
      }
      break;
      default:
        input.skip(ftype);
    }
    input.readFieldEnd();
  }
  input.readStructEnd();
  return;
};

AdminTagService_getMappedAdminMenuHashes_args.prototype.write = function(output) {
  output.writeStructBegin('AdminTagService_getMappedAdminMenuHashes_args');
  if (this.check_url !== null && this.check_url !== undefined) {
    output.writeFieldBegin('check_url', Thrift.Type.STRING, 1);
    output.writeString(this.check_url);
    output.writeFieldEnd();
  }
  if (this.tag_id !== null && this.tag_id !== undefined) {
    output.writeFieldBegin('tag_id', Thrift.Type.I32, 2);
    output.writeI32(this.tag_id);
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

var AdminTagService_getMappedAdminMenuHashes_result = function(args) {
  this.success = null;
  this.userException = null;
  this.systemException = null;
  if (args instanceof Errors_ttypes.UserException) {
    this.userException = args;
    return;
  }
  if (args instanceof Errors_ttypes.SystemException) {
    this.systemException = args;
    return;
  }
  if (args) {
    if (args.success !== undefined && args.success !== null) {
      this.success = Thrift.copyList(args.success, [null]);
    }
    if (args.userException !== undefined && args.userException !== null) {
      this.userException = args.userException;
    }
    if (args.systemException !== undefined && args.systemException !== null) {
      this.systemException = args.systemException;
    }
  }
};
AdminTagService_getMappedAdminMenuHashes_result.prototype = {};
AdminTagService_getMappedAdminMenuHashes_result.prototype.read = function(input) {
  input.readStructBegin();
  while (true)
  {
    var ret = input.readFieldBegin();
    var fname = ret.fname;
    var ftype = ret.ftype;
    var fid = ret.fid;
    if (ftype == Thrift.Type.STOP) {
      break;
    }
    switch (fid)
    {
      case 0:
      if (ftype == Thrift.Type.LIST) {
        var _size24 = 0;
        var _rtmp328;
        this.success = [];
        var _etype27 = 0;
        _rtmp328 = input.readListBegin();
        _etype27 = _rtmp328.etype;
        _size24 = _rtmp328.size;
        for (var _i29 = 0; _i29 < _size24; ++_i29)
        {
          var elem30 = null;
          elem30 = input.readString();
          this.success.push(elem30);
        }
        input.readListEnd();
      } else {
        input.skip(ftype);
      }
      break;
      case 1:
      if (ftype == Thrift.Type.STRUCT) {
        this.userException = new Errors_ttypes.UserException();
        this.userException.read(input);
      } else {
        input.skip(ftype);
      }
      break;
      case 2:
      if (ftype == Thrift.Type.STRUCT) {
        this.systemException = new Errors_ttypes.SystemException();
        this.systemException.read(input);
      } else {
        input.skip(ftype);
      }
      break;
      default:
        input.skip(ftype);
    }
    input.readFieldEnd();
  }
  input.readStructEnd();
  return;
};

AdminTagService_getMappedAdminMenuHashes_result.prototype.write = function(output) {
  output.writeStructBegin('AdminTagService_getMappedAdminMenuHashes_result');
  if (this.success !== null && this.success !== undefined) {
    output.writeFieldBegin('success', Thrift.Type.LIST, 0);
    output.writeListBegin(Thrift.Type.STRING, this.success.length);
    for (var iter31 in this.success)
    {
      if (this.success.hasOwnProperty(iter31))
      {
        iter31 = this.success[iter31];
        output.writeString(iter31);
      }
    }
    output.writeListEnd();
    output.writeFieldEnd();
  }
  if (this.userException !== null && this.userException !== undefined) {
    output.writeFieldBegin('userException', Thrift.Type.STRUCT, 1);
    this.userException.write(output);
    output.writeFieldEnd();
  }
  if (this.systemException !== null && this.systemException !== undefined) {
    output.writeFieldBegin('systemException', Thrift.Type.STRUCT, 2);
    this.systemException.write(output);
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

var AdminTagServiceClient = exports.Client = function(output, pClass) {
    this.output = output;
    this.pClass = pClass;
    this._seqid = 0;
    this._reqs = {};
};
AdminTagServiceClient.prototype = {};
AdminTagServiceClient.prototype.seqid = function() { return this._seqid; };
AdminTagServiceClient.prototype.new_seqid = function() { return this._seqid += 1; };
AdminTagServiceClient.prototype.getAdminIdsFromTags = function(tag_ids, callback) {
  this._seqid = this.new_seqid();
  if (callback === undefined) {
    var _defer = Q.defer();
    this._reqs[this.seqid()] = function(error, result) {
      if (error) {
        _defer.reject(error);
      } else {
        _defer.resolve(result);
      }
    };
    this.send_getAdminIdsFromTags(tag_ids);
    return _defer.promise;
  } else {
    this._reqs[this.seqid()] = callback;
    this.send_getAdminIdsFromTags(tag_ids);
  }
};

AdminTagServiceClient.prototype.send_getAdminIdsFromTags = function(tag_ids) {
  var output = new this.pClass(this.output);
  output.writeMessageBegin('getAdminIdsFromTags', Thrift.MessageType.CALL, this.seqid());
  var args = new AdminTagService_getAdminIdsFromTags_args();
  args.tag_ids = tag_ids;
  args.write(output);
  output.writeMessageEnd();
  return this.output.flush();
};

AdminTagServiceClient.prototype.recv_getAdminIdsFromTags = function(input,mtype,rseqid) {
  var callback = this._reqs[rseqid] || function() {};
  delete this._reqs[rseqid];
  if (mtype == Thrift.MessageType.EXCEPTION) {
    var x = new Thrift.TApplicationException();
    x.read(input);
    input.readMessageEnd();
    return callback(x);
  }
  var result = new AdminTagService_getAdminIdsFromTags_result();
  result.read(input);
  input.readMessageEnd();

  if (null !== result.userException) {
    return callback(result.userException);
  }
  if (null !== result.systemException) {
    return callback(result.systemException);
  }
  if (null !== result.success) {
    return callback(null, result.success);
  }
  return callback('getAdminIdsFromTags failed: unknown result');
};
AdminTagServiceClient.prototype.getAdminTagMenus = function(tag_id, callback) {
  this._seqid = this.new_seqid();
  if (callback === undefined) {
    var _defer = Q.defer();
    this._reqs[this.seqid()] = function(error, result) {
      if (error) {
        _defer.reject(error);
      } else {
        _defer.resolve(result);
      }
    };
    this.send_getAdminTagMenus(tag_id);
    return _defer.promise;
  } else {
    this._reqs[this.seqid()] = callback;
    this.send_getAdminTagMenus(tag_id);
  }
};

AdminTagServiceClient.prototype.send_getAdminTagMenus = function(tag_id) {
  var output = new this.pClass(this.output);
  output.writeMessageBegin('getAdminTagMenus', Thrift.MessageType.CALL, this.seqid());
  var args = new AdminTagService_getAdminTagMenus_args();
  args.tag_id = tag_id;
  args.write(output);
  output.writeMessageEnd();
  return this.output.flush();
};

AdminTagServiceClient.prototype.recv_getAdminTagMenus = function(input,mtype,rseqid) {
  var callback = this._reqs[rseqid] || function() {};
  delete this._reqs[rseqid];
  if (mtype == Thrift.MessageType.EXCEPTION) {
    var x = new Thrift.TApplicationException();
    x.read(input);
    input.readMessageEnd();
    return callback(x);
  }
  var result = new AdminTagService_getAdminTagMenus_result();
  result.read(input);
  input.readMessageEnd();

  if (null !== result.userException) {
    return callback(result.userException);
  }
  if (null !== result.systemException) {
    return callback(result.systemException);
  }
  if (null !== result.success) {
    return callback(null, result.success);
  }
  return callback('getAdminTagMenus failed: unknown result');
};
AdminTagServiceClient.prototype.getMappedAdminMenuHashes = function(check_url, tag_id, callback) {
  this._seqid = this.new_seqid();
  if (callback === undefined) {
    var _defer = Q.defer();
    this._reqs[this.seqid()] = function(error, result) {
      if (error) {
        _defer.reject(error);
      } else {
        _defer.resolve(result);
      }
    };
    this.send_getMappedAdminMenuHashes(check_url, tag_id);
    return _defer.promise;
  } else {
    this._reqs[this.seqid()] = callback;
    this.send_getMappedAdminMenuHashes(check_url, tag_id);
  }
};

AdminTagServiceClient.prototype.send_getMappedAdminMenuHashes = function(check_url, tag_id) {
  var output = new this.pClass(this.output);
  output.writeMessageBegin('getMappedAdminMenuHashes', Thrift.MessageType.CALL, this.seqid());
  var args = new AdminTagService_getMappedAdminMenuHashes_args();
  args.check_url = check_url;
  args.tag_id = tag_id;
  args.write(output);
  output.writeMessageEnd();
  return this.output.flush();
};

AdminTagServiceClient.prototype.recv_getMappedAdminMenuHashes = function(input,mtype,rseqid) {
  var callback = this._reqs[rseqid] || function() {};
  delete this._reqs[rseqid];
  if (mtype == Thrift.MessageType.EXCEPTION) {
    var x = new Thrift.TApplicationException();
    x.read(input);
    input.readMessageEnd();
    return callback(x);
  }
  var result = new AdminTagService_getMappedAdminMenuHashes_result();
  result.read(input);
  input.readMessageEnd();

  if (null !== result.userException) {
    return callback(result.userException);
  }
  if (null !== result.systemException) {
    return callback(result.systemException);
  }
  if (null !== result.success) {
    return callback(null, result.success);
  }
  return callback('getMappedAdminMenuHashes failed: unknown result');
};
var AdminTagServiceProcessor = exports.Processor = function(handler) {
  this._handler = handler;
}
;
AdminTagServiceProcessor.prototype.process = function(input, output) {
  var r = input.readMessageBegin();
  if (this['process_' + r.fname]) {
    return this['process_' + r.fname].call(this, r.rseqid, input, output);
  } else {
    input.skip(Thrift.Type.STRUCT);
    input.readMessageEnd();
    var x = new Thrift.TApplicationException(Thrift.TApplicationExceptionType.UNKNOWN_METHOD, 'Unknown function ' + r.fname);
    output.writeMessageBegin(r.fname, Thrift.MessageType.EXCEPTION, r.rseqid);
    x.write(output);
    output.writeMessageEnd();
    output.flush();
  }
}
;
AdminTagServiceProcessor.prototype.process_getAdminIdsFromTags = function(seqid, input, output) {
  var args = new AdminTagService_getAdminIdsFromTags_args();
  args.read(input);
  input.readMessageEnd();
  if (this._handler.getAdminIdsFromTags.length === 1) {
    Q.fcall(this._handler.getAdminIdsFromTags, args.tag_ids)
      .then(function(result) {
        var result_obj = new AdminTagService_getAdminIdsFromTags_result({success: result});
        output.writeMessageBegin("getAdminIdsFromTags", Thrift.MessageType.REPLY, seqid);
        result_obj.write(output);
        output.writeMessageEnd();
        output.flush();
      }, function (err) {
        var result;
        if (err instanceof Errors_ttypes.UserException || err instanceof Errors_ttypes.SystemException) {
          result = new AdminTagService_getAdminIdsFromTags_result(err);
          output.writeMessageBegin("getAdminIdsFromTags", Thrift.MessageType.REPLY, seqid);
        } else {
          result = new Thrift.TApplicationException(Thrift.TApplicationExceptionType.UNKNOWN, err.message);
          output.writeMessageBegin("getAdminIdsFromTags", Thrift.MessageType.EXCEPTION, seqid);
        }
        result.write(output);
        output.writeMessageEnd();
        output.flush();
      });
  } else {
    this._handler.getAdminIdsFromTags(args.tag_ids, function (err, result) {
      var result_obj;
      if ((err === null || typeof err === 'undefined') || err instanceof Errors_ttypes.UserException || err instanceof Errors_ttypes.SystemException) {
        result_obj = new AdminTagService_getAdminIdsFromTags_result((err !== null || typeof err === 'undefined') ? err : {success: result});
        output.writeMessageBegin("getAdminIdsFromTags", Thrift.MessageType.REPLY, seqid);
      } else {
        result_obj = new Thrift.TApplicationException(Thrift.TApplicationExceptionType.UNKNOWN, err.message);
        output.writeMessageBegin("getAdminIdsFromTags", Thrift.MessageType.EXCEPTION, seqid);
      }
      result_obj.write(output);
      output.writeMessageEnd();
      output.flush();
    });
  }
};
AdminTagServiceProcessor.prototype.process_getAdminTagMenus = function(seqid, input, output) {
  var args = new AdminTagService_getAdminTagMenus_args();
  args.read(input);
  input.readMessageEnd();
  if (this._handler.getAdminTagMenus.length === 1) {
    Q.fcall(this._handler.getAdminTagMenus, args.tag_id)
      .then(function(result) {
        var result_obj = new AdminTagService_getAdminTagMenus_result({success: result});
        output.writeMessageBegin("getAdminTagMenus", Thrift.MessageType.REPLY, seqid);
        result_obj.write(output);
        output.writeMessageEnd();
        output.flush();
      }, function (err) {
        var result;
        if (err instanceof Errors_ttypes.UserException || err instanceof Errors_ttypes.SystemException) {
          result = new AdminTagService_getAdminTagMenus_result(err);
          output.writeMessageBegin("getAdminTagMenus", Thrift.MessageType.REPLY, seqid);
        } else {
          result = new Thrift.TApplicationException(Thrift.TApplicationExceptionType.UNKNOWN, err.message);
          output.writeMessageBegin("getAdminTagMenus", Thrift.MessageType.EXCEPTION, seqid);
        }
        result.write(output);
        output.writeMessageEnd();
        output.flush();
      });
  } else {
    this._handler.getAdminTagMenus(args.tag_id, function (err, result) {
      var result_obj;
      if ((err === null || typeof err === 'undefined') || err instanceof Errors_ttypes.UserException || err instanceof Errors_ttypes.SystemException) {
        result_obj = new AdminTagService_getAdminTagMenus_result((err !== null || typeof err === 'undefined') ? err : {success: result});
        output.writeMessageBegin("getAdminTagMenus", Thrift.MessageType.REPLY, seqid);
      } else {
        result_obj = new Thrift.TApplicationException(Thrift.TApplicationExceptionType.UNKNOWN, err.message);
        output.writeMessageBegin("getAdminTagMenus", Thrift.MessageType.EXCEPTION, seqid);
      }
      result_obj.write(output);
      output.writeMessageEnd();
      output.flush();
    });
  }
};
AdminTagServiceProcessor.prototype.process_getMappedAdminMenuHashes = function(seqid, input, output) {
  var args = new AdminTagService_getMappedAdminMenuHashes_args();
  args.read(input);
  input.readMessageEnd();
  if (this._handler.getMappedAdminMenuHashes.length === 2) {
    Q.fcall(this._handler.getMappedAdminMenuHashes, args.check_url, args.tag_id)
      .then(function(result) {
        var result_obj = new AdminTagService_getMappedAdminMenuHashes_result({success: result});
        output.writeMessageBegin("getMappedAdminMenuHashes", Thrift.MessageType.REPLY, seqid);
        result_obj.write(output);
        output.writeMessageEnd();
        output.flush();
      }, function (err) {
        var result;
        if (err instanceof Errors_ttypes.UserException || err instanceof Errors_ttypes.SystemException) {
          result = new AdminTagService_getMappedAdminMenuHashes_result(err);
          output.writeMessageBegin("getMappedAdminMenuHashes", Thrift.MessageType.REPLY, seqid);
        } else {
          result = new Thrift.TApplicationException(Thrift.TApplicationExceptionType.UNKNOWN, err.message);
          output.writeMessageBegin("getMappedAdminMenuHashes", Thrift.MessageType.EXCEPTION, seqid);
        }
        result.write(output);
        output.writeMessageEnd();
        output.flush();
      });
  } else {
    this._handler.getMappedAdminMenuHashes(args.check_url, args.tag_id, function (err, result) {
      var result_obj;
      if ((err === null || typeof err === 'undefined') || err instanceof Errors_ttypes.UserException || err instanceof Errors_ttypes.SystemException) {
        result_obj = new AdminTagService_getMappedAdminMenuHashes_result((err !== null || typeof err === 'undefined') ? err : {success: result});
        output.writeMessageBegin("getMappedAdminMenuHashes", Thrift.MessageType.REPLY, seqid);
      } else {
        result_obj = new Thrift.TApplicationException(Thrift.TApplicationExceptionType.UNKNOWN, err.message);
        output.writeMessageBegin("getMappedAdminMenuHashes", Thrift.MessageType.EXCEPTION, seqid);
      }
      result_obj.write(output);
      output.writeMessageEnd();
      output.flush();
    });
  }
};