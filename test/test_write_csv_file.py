import csv
import time

with open("/home/pi/MultisensorCropMonitoringPlatform/test/test_write_csv_file.csv", "w", newline="", ) as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    while True:
        spamwriter.writerow(["20220523", "130", "cm"])
        spamwriter.writerow(["20220523", "150", "cm"])
        spamwriter.writerow(["20220523", "30", "cm"])
        time.sleep(1)
