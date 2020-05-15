#! /usr/bin/env python
# coding: utf-8
 
import serial
 
found = False
 
for i in range(64) :
  try :
    port = "/dev/ttyS%d" % i
    ser = serial.Serial(port)
    ser.close()
    print "Serial port FOUND: ", port
    found = True
  except serial.serialutil.SerialException :
    pass
 
if not found :
  print "Serials not found !"
