<?php
namespace Ridibooks\Cms\Thrift\AdminMenu;
/**
 * Autogenerated by Thrift Compiler (1.0.0-dev)
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
use Thrift\Base\TBase;
use Thrift\Type\TType;
use Thrift\Type\TMessageType;
use Thrift\Exception\TException;
use Thrift\Exception\TProtocolException;
use Thrift\Protocol\TProtocol;
use Thrift\Protocol\TBinaryProtocolAccelerated;
use Thrift\Exception\TApplicationException;


class AdminMenuService_getAdminIdsByMenuId_result {
  static $_TSPEC;

  /**
   * @var string[]
   */
  public $success = null;
  /**
   * @var \Ridibooks\Cms\Thrift\Errors\UserException
   */
  public $userException = null;
  /**
   * @var \Ridibooks\Cms\Thrift\Errors\SystemException
   */
  public $systemException = null;

  public function __construct($vals=null) {
    if (!isset(self::$_TSPEC)) {
      self::$_TSPEC = array(
        0 => array(
          'var' => 'success',
          'type' => TType::LST,
          'etype' => TType::STRING,
          'elem' => array(
            'type' => TType::STRING,
            ),
          ),
        1 => array(
          'var' => 'userException',
          'type' => TType::STRUCT,
          'class' => '\Ridibooks\Cms\Thrift\Errors\UserException',
          ),
        2 => array(
          'var' => 'systemException',
          'type' => TType::STRUCT,
          'class' => '\Ridibooks\Cms\Thrift\Errors\SystemException',
          ),
        );
    }
    if (is_array($vals)) {
      if (isset($vals['success'])) {
        $this->success = $vals['success'];
      }
      if (isset($vals['userException'])) {
        $this->userException = $vals['userException'];
      }
      if (isset($vals['systemException'])) {
        $this->systemException = $vals['systemException'];
      }
    }
  }

  public function getName() {
    return 'AdminMenuService_getAdminIdsByMenuId_result';
  }

  public function read($input)
  {
  	$xfer = 0;
    $fname = null;
    $ftype = 0;
    $fid = 0;
    $xfer += $input->readStructBegin($fname);
    while (true)
    {
      $xfer += $input->readFieldBegin($fname, $ftype, $fid);
      if ($ftype == TType::STOP) {
        break;
      }
      switch ($fid)
      {
        case 0:
          if ($ftype == TType::LST) {
            $this->success = array();
            $_size35 = 0;
            $_etype38 = 0;
            $xfer += $input->readListBegin($_etype38, $_size35);
            for ($_i39 = 0; $_i39 < $_size35; ++$_i39)
            {
              $elem40 = null;
              $xfer += $input->readString($elem40);
              $this->success []= $elem40;
            }
            $xfer += $input->readListEnd();
          } else {
            $xfer += $input->skip($ftype);
          }
          break;
        case 1:
          if ($ftype == TType::STRUCT) {
            $this->userException = new \Ridibooks\Cms\Thrift\Errors\UserException();
            $xfer += $this->userException->read($input);
          } else {
            $xfer += $input->skip($ftype);
          }
          break;
        case 2:
          if ($ftype == TType::STRUCT) {
            $this->systemException = new \Ridibooks\Cms\Thrift\Errors\SystemException();
            $xfer += $this->systemException->read($input);
          } else {
            $xfer += $input->skip($ftype);
          }
          break;
        default:
          $xfer += $input->skip($ftype);
          break;
      }
      $xfer += $input->readFieldEnd();
    }
    $xfer += $input->readStructEnd();
    return $xfer;
  }

  public function write($output) {
    $xfer = 0;
    $xfer += $output->writeStructBegin('AdminMenuService_getAdminIdsByMenuId_result');
    if ($this->success !== null) {
      if (!is_array($this->success)) {
        throw new TProtocolException('Bad type in structure.', TProtocolException::INVALID_DATA);
      }
      $xfer += $output->writeFieldBegin('success', TType::LST, 0);
      {
        $output->writeListBegin(TType::STRING, count($this->success));
        {
          foreach ($this->success as $iter41)
          {
            $xfer += $output->writeString($iter41);
          }
        }
        $output->writeListEnd();
      }
      $xfer += $output->writeFieldEnd();
    }
    if ($this->userException !== null) {
      $xfer += $output->writeFieldBegin('userException', TType::STRUCT, 1);
      $xfer += $this->userException->write($output);
      $xfer += $output->writeFieldEnd();
    }
    if ($this->systemException !== null) {
      $xfer += $output->writeFieldBegin('systemException', TType::STRUCT, 2);
      $xfer += $this->systemException->write($output);
      $xfer += $output->writeFieldEnd();
    }
    $xfer += $output->writeFieldStop();
    $xfer += $output->writeStructEnd();
    return $xfer;
  }

}

