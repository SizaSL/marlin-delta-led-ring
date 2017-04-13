#!/usr/bin/env python

import serial, sys, time
from serial.tools import list_ports

try:
	mega_serial_port = next(list_ports.grep("Arduino Mega 2560"))
	
	serial_port = serial.Serial(port=mega_serial_port.device,
								baudrate=57600,
								parity=serial.PARITY_NONE,
								stopbits=serial.STOPBITS_ONE,
								bytesize=serial.EIGHTBITS)
	serial_port.isOpen()
	serial_port.close()	
	time.sleep(3)
except StopIteration:
	print("No Arduino Mega device connected")