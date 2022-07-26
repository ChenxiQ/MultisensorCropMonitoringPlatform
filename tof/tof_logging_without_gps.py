#!/usr/bin/env python3

import serial
import time
import datetime
import csv
import os


debugMode = True
loggerName = "debugLogger"
fieldNumber = "debugField"
rowNumber = "debugRow"
baseDistance = 0

DATETIMESTYLE = "%Y-%m-%d_%H:%M:%S"


def dataLogging():
    global loggerName, fieldNumber, rowNumber, baseDistance

    if not debugMode:
        # Ask user enter and confirm logging information
        startRecording = False
        while startRecording == False:
            print("================================")
            print("====  Welcome to CornBuggy  ====")
            print("================================")
            loggerName = input("Please enter the logger's name: ")
            fieldNumber = input("Please enter the filed number: ")
            rowNumber = input("Please enter the row number: ")
            baseDistance = input("Please enter the base distance: ")
            print("=============VERIFY=============")
            print("Logger's name: {}".format(loggerName))
            print("Field Number: {}".format(fieldNumber))
            print("Row Number: {}".format(rowNumber))
            print("Base Distance: {}".format(baseDistance))
            print("Press \"y\" to continue.")
            print("Press \"n\" to restart.")
            print("================================")
            startRecording = True if input() == "y" else False

    print("================================")
    print("    Logging crop height data    ")
    print("      Press Ctrl+C to exit      ")
    print("================================")

    # Initialize .csv file
    captureDate = str(time.strftime(DATETIMESTYLE, time.localtime(time.time())))
    if debugMode:
        csvFilePrefix = "/home/pi/MultisensorCropMonitoringPlatform/data/tof/debug"
    else:
        csvFilePrefix = "/home/pi/MultisensorCropMonitoringPlatform/data/tof"
    csvFilePath = "{}/Field{}_Row{}_{}_{}_{}cm_raw.csv".format(csvFilePrefix, fieldNumber, rowNumber, captureDate, loggerName, baseDistance)
    print("Writing data to {}".format(csvFilePath))
    time.sleep(1)

    # Write header info to .cvs file
    with open(csvFilePath, "a", newline="", ) as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        spamwriter.writerow(["Sensor Time", "ToF Height (cm)", "Crop height (cm)"])

    arduinoSerial = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
    arduinoSerial.reset_input_buffer()

    cnt = 0

    while True:
        with open(csvFilePath, "a", newline="", ) as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',')
            if arduinoSerial.in_waiting > 0:
                timeStamp = datetime.datetime.now().time()
                try:
                    tofDistance = arduinoSerial.readline().decode('utf-8').rstrip()
                except ValueError:
                    continue

                if cnt > 20:
                    tofDistance = tofDistance // 10
                    cropHeight = baseDistance - tofDistance
                    print("{} \t tofDistance: {}cm \t cropHeight: {}cm".format(timeStamp, tofDistance, cropHeight))
                    spamwriter.writerow([timeStamp, tofDistance, cropHeight])
                
                cnt += 1


if __name__ == '__main__':
    try:
        dataLogging()
    except KeyboardInterrupt:
        os.system("/home/pi/MultisensorCropMonitoringPlatform/reset_arduino.sh")
        quit()
