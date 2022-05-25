#!/usr/bin/env python3

import serial
import time
import datetime
import csv
import os
import threading


debugMode = True
loggerName = "Undefined"
fieldNumber = "Undefined"
rowNumber = "Undefined"

DATETIMESTYLE = "%Y-%m-%d_%H:%M:%S"

gps_serial = serial.Serial("/dev/ttyUSB0", 19200)
gpsData = None


def getGPSInfo():
    global gpsData

    while True:
        tmpGPSData = gps_serial.readline().decode("utf-8")

        if tmpGPSData.startswith('$GPGGA,'):
            gpsData = tmpGPSData


def dataLogging():
    # Ask user enter and confirm logging information
    startRecording = False
    while startRecording == False:
        print("================================")
        print("====  Welcome to CornBuggy  ====")
        print("================================")
        loggerName = input("Please enter the logger's name: ")
        fieldNumber = input("Please enter the filed number: ")
        rowNumber = input("Please enter the row number: ")
        print("=============VERIFY=============")
        print("Logger's name: {}".format(loggerName))
        print("Field Number: {}".format(fieldNumber))
        print("Row Number: {}".format(rowNumber))
        print("Press \"y\" to continue.")
        print("Press \"n\" to restart.")
        print("================================")
        startRecording = True if input() == "y" else False

    print("================================")
    print(" Logging crop height data in 3s ")
    print("      Press Ctrl+C to exit      ")
    print("================================")

    # Initialize .csv file
    captureDate = str(time.strftime(DATETIMESTYLE, time.localtime(time.time())))
    if debugMode:
        csvFilePrefix = "/home/pi/MultisensorCropMonitoringPlatform/data/lidar/debug"
    else:
        csvFilePrefix = "/home/pi/MultisensorCropMonitoringPlatform/data/lidar"
    csvFilePath = "{}/Field{}_Row{}_{}_{}_raw.csv".format(csvFilePrefix, fieldNumber, rowNumber, captureDate, loggerName)
    print("Writing data to {}".format(csvFilePath))
    time.sleep(3)

    # Write header info to .cvs file
    with open(csvFilePath, "a", newline="", ) as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        # spamwriter.writerow(["Logger", loggerName, "Field #", fieldNumber, "Row #", rowNumber, "cm"])
        spamwriter.writerow(["Lidar Time", "Height (cm)", "Log Format", "GPS UTC Time", "Latitude", "Latitude Direction", "Longitude", "Longitude Direction", "GPS Quality Indicator", "# sats", "hdop", "alt", "a-units", "undulation", "u-units", "age", "stn ID & Check Sum"])

    ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
    ser.reset_input_buffer()

    while True:
        with open(csvFilePath, "a", newline="", ) as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',')
            if ser.in_waiting > 0:
                # captureTime = str(time.strftime(DATETIMESTYLE, time.localtime(time.time())))
                timeStamp = datetime.datetime.now().time()
                distance = ser.readline().decode('utf-8').rstrip()
                print("{} {} cm".format(timeStamp, distance))
                spamwriter.writerow([timeStamp, distance] + gpsData[:-2].split(","))
                print(gpsData[:-2])
                print()


if __name__ == '__main__':
    try:
        getGPSInfoThread = threading.Thread(target=getGPSInfo, daemon=True)
        getGPSInfoThread.start()
        time.sleep(2)
        dataLogging()
    except KeyboardInterrupt:
        # os.system("/home/pi/MultisensorCropMonitoringPlatform/reset_arduino.sh")
        quit()
