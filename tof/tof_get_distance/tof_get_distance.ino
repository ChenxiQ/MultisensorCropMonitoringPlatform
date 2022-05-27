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

    Serial.print("Distance(mm): ");
    Serial.print(distance);
    Serial.println();

    delay(100);
}
