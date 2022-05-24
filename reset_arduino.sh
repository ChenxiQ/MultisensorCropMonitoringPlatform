#!/bin/sh

echo "Start reseting Arduino ..."

fuser -k /dev/ttyACM0
sleep 1

echo "Start compiling sketch bareMinimum..."
arduino-cli compile --fqbn arduino:avr:mega /home/pi/MultisensorCropMonitoringPlatform/bareMinimum/bareMinimum.ino
echo "Finish compiling sketch bareMinimum..."

arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:mega /home/pi/MultisensorCropMonitoringPlatform/bareMinimum/bareMinimum.ino
echo "Finish uploading sketch bareMinimum..."

sleep 2
fuser -k /dev/ttyACM0

echo "Finish reseting Arduino"
