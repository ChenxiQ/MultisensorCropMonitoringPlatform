/*------------------------------------------------------------------------------

    Modified from
    LIDARLite Arduino Library
    v4LED/v4LED

    Connections:
    LIDAR-Lite 5 VDC   (pin 1) to Arduino 5V
    LIDAR-Lite Ground  (pin 2) to Arduino GND
    LIDAR-Lite I2C SDA (pin 3) to Arduino SDA
    LIDAR-Lite I2C SCL (pin 4) to Arduino SCL

------------------------------------------------------------------------------*/

#include <stdint.h>
#include <Wire.h>
#include "LIDARLite_v4LED.h"

LIDARLite_v4LED myLidarLite;
int distance;

void setup() {
    // Initialize Arduino serial port (for display of ASCII output to PC)
    Serial.begin(115200);

    // Initialize Arduino I2C (for communication to LidarLite)
    Wire.begin();
    digitalWrite(SCL, LOW);
    digitalWrite(SDA, LOW);

    myLidarLite.configure(0);
}

void loop() {
    if (myLidarLite.getBusyFlag() == 0) {
        myLidarLite.takeRange();
        distance = myLidarLite.readDistance();
        // Serial.print("Sensor distance: ");
        Serial.println(distance);
        // Serial.println(" cm.");
    }
    delay(10);
}
