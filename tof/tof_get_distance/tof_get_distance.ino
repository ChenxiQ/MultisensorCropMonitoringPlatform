/*
    Modified from sparkfun
*/

#include <Wire.h>
#include "SparkFun_VL53L1X.h"

SFEVL53L1X distanceSensor;

void setup(void) {
    Wire.begin();
    Serial.begin(115200);
    distanceSensor.setDistanceModeShort();

    // Begin returns 0 on a good init
    if (distanceSensor.begin() != 0) {
        Serial.println("Sensor failed to begin. Please check wiring. Freezing...");
        while (1)
            ;
    }
    Serial.println("Sensor online!");
}

void loop(void) {
    // Write configuration bytes to initiate measurement
    distanceSensor.startRanging();
    while (!distanceSensor.checkForDataReady()) {
        delay(1);
    }
    
    // Get the result of the measurement from the sensor
    int distance = distanceSensor.getDistance();
    distanceSensor.clearInterrupt();
    distanceSensor.stopRanging();

    // Serial.print("Distance(mm): ");
    Serial.println(distance);

    delay(1000);
}
