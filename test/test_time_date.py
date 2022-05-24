import time
import datetime

loggerName = "Chenxi"
fieldNumber = "5"
rowNumber = "2"

captureDate = str(time.strftime("%Y-%m-%d", time.localtime(time.time())))
csvFilePrefix = "/home/pi/MultisensorCropMonitoringPlatform/data/lidar"
csvFilePath = "{}/Field{}_{}_Row{}.csv".format(csvFilePrefix, fieldNumber, captureDate, rowNumber)

print(csvFilePath)

print(datetime.datetime.now().time())
