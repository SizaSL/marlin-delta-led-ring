#!/usr/bin/env python

import serial, sys, time
from serial.tools import list_ports
from subprocess import call

try:
	#mega_serial_port = next(list_ports.grep("Arduino Pro"))
	serial_port = serial.Serial(port="/dev/LedRing",
								baudrate=115200,
								parity=serial.PARITY_NONE,
								stopbits=serial.STOPBITS_ONE,
								bytesize=serial.EIGHTBITS)
	serial_port.isOpen()
	time.sleep(3)
	serial_port.write("asdf")
	time.sleep(6)
	serial_port.close()
except StopIteration:
	print("No Arduino device connected")