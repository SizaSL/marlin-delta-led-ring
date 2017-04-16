mkdir platformio-build
platformio ci --verbose --board pro16MHzatmega328 --project-option="lib_extra_dirs=C:\Program Files (x86)\Arduino\libraries:upload_port=/dev/ttyAMA0" --build-dir=platformio-build --keep-build-dir led-ring
