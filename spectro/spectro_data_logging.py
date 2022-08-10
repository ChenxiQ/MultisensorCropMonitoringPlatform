#!/usr/bin/env python3

import serial
import time
import csv
import os


sampleName = "Undefined"

DATETIMESTYLE = "%Y-%m-%d_%H:%M:%S"
CVSHEADER = ["410", "435", "460", "485", "510", "535", "560", "585", "610", "645", "680", "705", "730", "760", "810", "860", "900", "940"]


def dataLogging():
    # Ask user enter and confirm logging information
    startRecording = False
    while startRecording == False:
        print("================================")
        print("====  Welcome to CornBuggy  ====")
        print("================================")
        sampleName = input("Please enter the sample name: ")
        print("=============VERIFY=============")
        print("Sample Name: {}".format(sampleName))
        print("Press \"y\" to continue.")
        print("Press \"n\" to restart.")
        print("================================")
        startRecording = True if input() == "y" else False

    print("================================")
    print("      Logging spectro data      ")
    print("      Press Ctrl+C to exit      ")
    print("================================")

    # Initialize .csv file
    captureDate = str(time.strftime(DATETIMESTYLE, time.localtime(time.time())))
    csvFilePrefix = "/home/pi/MultisensorCropMonitoringPlatform/data/spectro"
    csvFilePath = "{}/{}_{}.csv".format(csvFilePrefix, sampleName, captureDate)
    print("Writing data to {}".format(csvFilePath))
    time.sleep(1)

    # Write header info to .cvs file
    with open(csvFilePath, "a", newline="", ) as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        spamwriter.writerow(CVSHEADER)

    arduinoSerial = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
    arduinoSerial.reset_input_buffer()

    cnt = 0

    while True:
        with open(csvFilePath, "a", newline="", ) as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',')
            if arduinoSerial.in_waiting > 0:
                try:
                    line = arduinoSerial.readline().decode('utf-8').rstrip().split(",")
                except ValueError:
                    continue
                
                if cnt < 5:
                    pass
                elif 5 <= cnt < 15:
                    print(line)
                    spamwriter.writerow(line)
                else:
                    quitProgram()
                
                cnt += 1


def quitProgram():
    os.system("/home/pi/MultisensorCropMonitoringPlatform/reset_arduino.sh")
    quit()


if __name__ == '__main__':
    try:
        dataLogging()
    except KeyboardInterrupt:
        os.system("/home/pi/MultisensorCropMonitoringPlatform/reset_arduino.sh")
        quit()
