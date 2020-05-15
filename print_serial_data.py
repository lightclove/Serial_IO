# -*- coding: UTF-8 -*-
# !/usr/bin/env python2
import serial
 
ser = serial.Serial("/dev/ttyS1")
ser.baudrate = 57600
 
while True :
  line = ser.readline()
  print line
