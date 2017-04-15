mkdir platformio-build
platformio ci --verbose --board pro16MHzatmega328 --project-option="lib_extra_dirs=C:\Program Files (x86)\Arduino\libraries" --build-dir=platformio-build --keep-build-dir led-ring
chmod 700 tools/mega_serial_start_win.py tools/avrdude_win.exe
python tools/mega_serial_start_win.py