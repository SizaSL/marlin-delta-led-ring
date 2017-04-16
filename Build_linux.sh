mkdir platformio-build
chmod 666 /dev/ttyACM0
platformio ci --verbose --board pro16MHzatmega328 --project-option="lib_extra_dirs=C:\Program Files (x86)\Arduino\libraries" --project-option="targets=upload" --project-option="upload_port=/dev/ttyUSB0" --build-dir=platformio-build --keep-build-dir led-ring
