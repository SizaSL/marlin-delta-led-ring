#!/usr/bin/env python

import serial, sys, time
from serial.tools import list_ports
from subprocess import call

try:
	mega_serial_port = next(list_ports.grep("Arduino Mega 2560"))
	
	serial_port = serial.Serial(port=mega_serial_port.device,
								baudrate=57600,
								parity=serial.PARITY_NONE,
								stopbits=serial.STOPBITS_ONE,
								bytesize=serial.EIGHTBITS)
	serial_port.isOpen()
	call(['sudo', './tools/avrdude_linux', '-V -C./tools/avrdude.conf -v -patmega328p -carduino -P/dev/ttyACM0 -U -Uflash:w:platformio-build/.pioenvs/pro16MHzatmega328/firmware.hex:i'])
	serial_port.close()	
except StopIteration:
	print("No Arduino Mega device connected")