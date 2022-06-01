#!/usr/bin/env python3
import serial
import os

if __name__ == '__main__':
    try:
        ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
        ser.reset_input_buffer()

        while True:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').rstrip()
                print(line)
    except KeyboardInterrupt:
        os.system("/home/pi/MultisensorCropMonitoringPlatform/reset_arduino.sh")
        quit()
