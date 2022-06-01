#!/bin/sh

arduino-cli compile --fqbn arduino:avr:mega /home/pi/MultisensorCropMonitoringPlatform/example/example_tof_get_distance/example_tof_get_distance.ino

arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:mega /home/pi/MultisensorCropMonitoringPlatform/example/example_tof_get_distance/example_tof_get_distance.ino
echo "Finish uploading sketch lidar_get_distance"

python3 /home/pi/MultisensorCropMonitoringPlatform/test/test_arduino_pi_comm.py
