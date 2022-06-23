#!/bin/sh

arduino-cli compile --fqbn arduino:avr:mega /home/pi/MultisensorCropMonitoringPlatform/spectro/spectro_get_info/spectro_get_info.ino

arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:mega /home/pi/MultisensorCropMonitoringPlatform/spectro/spectro_get_info/spectro_get_info.ino
echo "Finish uploading sketch spectro_get_info"

python3 /home/pi/MultisensorCropMonitoringPlatform/spectro/spectro_data_logging.py
