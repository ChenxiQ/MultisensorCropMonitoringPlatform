#!/bin/sh

arduino-cli compile --fqbn arduino:avr:mega /home/pi/MultisensorCropMonitoringPlatform/tof/tof_get_distance/tof_get_distance.ino

arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:mega /home/pi/MultisensorCropMonitoringPlatform/tof/tof_get_distance/tof_get_distance.ino
echo "Finish uploading sketch lidar_get_distance"

python3 /home/pi/MultisensorCropMonitoringPlatform/tof/tof_logging_without_gps.py
