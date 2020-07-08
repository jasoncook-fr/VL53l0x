from machine import I2C, Pin
from time import sleep
from vl53l0x import VL53L0X

# construct a software I2C bus
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
sensor = VL53L0X(i2c, address = 0x29)

while True:
    sleep(.01)
    print(sensor.read())
