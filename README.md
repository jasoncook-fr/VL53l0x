### ESP32 i2c communication with laser distance sensor VL53L0X

Micropython is used. Code is a very basic startup test to get up and running. [Here] (https://www.makershop.de/sensoren/distanz/vl53l0x-breakout/) is the sensor used.
3.3v works fine. If results are unsatisfied try a quick i2c.scan() to make sure your device sees the sensor. File vl53lox.py is the essential driver, courtesy of Radomir Dopieralski. Found it [here](https://bitbucket.org/thesheep/micropython-vl53l0x/src/9077f84e25409532b7ef220fa068605c971ba967/vl53l0x.py?at=default&fileviewer=file-view-default)
