#!/usr/bin/env python3

import serial
import time
import csv


debugMode = True
loggerName = "Undefined"
fieldNumber = "Undefined"
rowNumber = "Undefined"

DATETIMESTYLE = "%Y-%m-%d_%H:%M:%S"


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
    csvFilePath = "{}/Field{}_Row{}_{}.csv".format(csvFilePrefix, fieldNumber, rowNumber, captureDate)
    print("Writing data to {}".format(csvFilePath))
    time.sleep(3)

    # Write header info to .cvs file
    with open(csvFilePath, "a", newline="", ) as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(["Logger", loggerName, "Field #", fieldNumber, "Row #", rowNumber])

    ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
    ser.reset_input_buffer()

    while True:
        with open(csvFilePath, "a", newline="", ) as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            if ser.in_waiting > 0:
                captureTime = str(time.strftime(DATETIMESTYLE, time.localtime(time.time())))
                distance = ser.readline().decode('utf-8').rstrip()
                print("{} {} cm".format(captureTime, distance))
                spamwriter.writerow([captureTime, distance, "cm"])


if __name__ == '__main__':
    try:
        dataLogging()
    except KeyboardInterrupt:
        quit()
