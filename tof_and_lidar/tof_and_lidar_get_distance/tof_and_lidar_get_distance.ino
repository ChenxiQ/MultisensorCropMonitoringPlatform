#include <stdint.h>
#include <Wire.h>
#include "LIDARLite_v4LED.h"
#include "SparkFun_VL53L1X.h"

LIDARLite_v4LED myLidarLite;
SFEVL53L1X distanceSensor;

int distance;

void setup() {
    // Initialize Arduino serial port (for display of ASCII output to PC)
    Serial.begin(115200);

    // Initialize Arduino I2C (for communication to LidarLite)
    Wire.begin();
    digitalWrite(SCL, LOW);
    digitalWrite(SDA, LOW);

    // Initialize Garmin Lidar
    myLidarLite.configure(0);

    // Initialize ToF distance sensor
    distanceSensor.setDistanceModeShort();
    // Begin returns 0 on a good init
    if (distanceSensor.begin() != 0) {
        Serial.println("Sensor failed to begin. Please check wiring. Freezing...");
        while (1)
            ;
    }
    Serial.println("ToF sensor online!");
}

void loop() {
    // Garmin Lidar get distance
    if (myLidarLite.getBusyFlag() == 0) {
        myLidarLite.takeRange();
        distance = myLidarLite.readDistance();
        // Serial.print("Lidar distance: ");
        Serial.print(distance);
    }
    delay(10);

    Serial.print(" ");

    // ToF distance sensor get distance
    // Write configuration bytes to initiate measurement
    distanceSensor.startRanging();
    while (!distanceSensor.checkForDataReady()) {
        delay(1);
    }
    // Get the result of the measurement from the sensor
    int distance = distanceSensor.getDistance();
    distanceSensor.clearInterrupt();
    distanceSensor.stopRanging();
    // Serial.print("ToF distance: ");
    Serial.println(distance/10);

    delay(1000);
}
