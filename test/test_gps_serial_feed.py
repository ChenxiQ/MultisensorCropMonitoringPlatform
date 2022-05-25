import serial
import threading
import time

gps_serial = serial.Serial("/dev/ttyUSB0", 19200)
gpsData = None


def getGPSInfo():
    global gpsData

    while True:
        tmpGPSData = str(gps_serial.readline().decode("utf-8"))

        if tmpGPSData.startswith('$GPGGA,'):
            gpsData = tmpGPSData


def logGPSInfo():
    global gpsData

    for _ in range(10):
        print(gpsData[:-2])


if __name__ == '__main__':
    try:
        getGPSInfoThread = threading.Thread(target=getGPSInfo, daemon=True)
        getGPSInfoThread.start()

        time.sleep(2)
        logGPSInfo()
    except KeyboardInterrupt:
        quit()
