# -*- coding: UTF-8 -*-
# !/usr/bin/env python2
 
import serial
 
found = False
 
for i in range(64) :
  try :
    #port = "/dev/ttyS%d" % i
    #port = "/dev/ttyUSB%d" % i
    port = "COM%d" % i
    ser = serial.Serial(port)
    ser.close()
    print "Serial Port Found: ", port
    found = True
  except serial.serialutil.SerialException :
    pass
 
if not found :
  print "No serial ports detected"