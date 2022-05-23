#!/usr/bin/env python3
import serial
import time

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
    ser.reset_input_buffer()

    while True:
        if ser.in_waiting > 0:
            style = "%Y-%m-%d_%H:%M:%S"
            captureTime = str(time.strftime(style, time.localtime(time.time())))
            distance = ser.readline().decode('utf-8').rstrip()
            print("{} {}".format(captureTime, distance))
