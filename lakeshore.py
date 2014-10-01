#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial
import struct
import time
import datetime
import os
import sys


class LakeShoreError(Exception):
    def __init__(self, message):
        self.msg = "LakeShore Error: %s" % str(message)
    def __str__(self):
        return self.msg

class LakeShore(object):
    def __init__(self, devfile):
        self.ser = serial.Serial(devfile,
                                 baudrate=9600,
                                 bytesize=serial.SEVENBITS,
                                 parity=serial.PARITY_ODD,
                                 timeout=0,
                                 writeTimeout=1,
                                 stopbits=serial.STOPBITS_ONE)
        time.sleep(1)
        if self.ser == None: raise LakeShoreError("open error")

    def __del__(self):
        self.ser.close()
        del self

    def write(self, command):
        self.ser.write(command)

    def read(self):
        return self.ser.readline()

    def readclear(self):
        while len(self.ser.readline()) != 0: pass

    def get_temps(self):
        self.readclear()
        self.write("KRDG?0\r\n")
        time.sleep(1)
        return self.read()

if __name__ == '__main__':
    # l = LakeShore('/dev/serial/by-path/pci-0000\:00\:1d.2-usb-0\:1\:1.0-port0')
    l = LakeShore('/dev/ttyUSB0')
    print '#'
    print '# LakeShore 218 Temperature Monitor'
    print '# Date: %s' % time.strftime("%Y-%m-%d %H:%M:%S")
    print '#'
    print '# UTC+9  Unixtime  ch 0  ch 1  ch 2  ch 3  ch 4  ch 5  ch 6  ch 7'
    while True:
        try:
            ut = int(time.time())
            t  = time.strftime("%Y-%m-%d-%H:%M:%S")
            d  = l.get_temps()
            sys.stdout.write('%s  ' % t)
            sys.stdout.write('%s' % ut)
            print '  %.2f'*8 % tuple([float(x) for x in d.split(',')])
            sys.stdout.flush()
        except KeyboardInterrupt: break
