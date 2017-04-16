mkdir platformio-build
platformio ci --verbose --board pro16MHzatmega328 --project-option="targets=upload" --project-option="upload_port=/dev/LedRing" --build-dir=platformio-build --keep-build-dir led-ring
