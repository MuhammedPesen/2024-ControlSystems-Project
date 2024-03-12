#include "MPU9255.h"

MPU9255 mpu; // Compatible with MPU9255 as well

void setup() {
    Serial.begin(115200);
    Wire.begin();
    delay(2000); // Wait for sensor to stabilize

    // Attempt to initialize MPU9250
    if (!mpu.setup(0x68)) { // Change to your own address
        Serial.println("MPU9250 initialization failed!");
        while (1); // Halt if failed to initialize
    }
}

void loop() {
    if (mpu.update()) {
        Serial.print(mpu.getYaw()); Serial.print(", ");
        Serial.print(mpu.getPitch()); Serial.print(", ");
        Serial.println(mpu.getRoll());
    } else {
        // If update failed, print an error message
        Serial.println("Failed to read from MPU9250");
    }

    delay(100); // Adjust based on your needs
}
