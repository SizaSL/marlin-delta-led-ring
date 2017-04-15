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
        #time.sleep(1)
        serial_port.close()
        time.sleep(5)
        port_name = '-P' + mega_serial_port.device
        call(['tools/avrdude_win', '-V', '-Ctools/avrdude.conf', '-v', '-r', '-patmega328p', '-carduino', port_name, '-b57600', '-Uflash:w:platformio-build/.pioenvs/pro16MHzatmega328/firmware.hex:i'])
except StopIteration:
        print("No Arduino Mega device connected")