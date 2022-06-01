#!/bin/sh

arduino-cli compile --fqbn arduino:avr:mega /home/pi/MultisensorCropMonitoringPlatform/tof/tof_get_distance/tof_get_distance.ino

arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:mega /home/pi/MultisensorCropMonitoringPlatform/tof/tof_get_distance/tof_get_distance.ino
echo "Finish uploading sketch tof_get_distance"

python3 /home/pi/MultisensorCropMonitoringPlatform/test/test_arduino_pi_comm.py
