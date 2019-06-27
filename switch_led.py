# -*- coding: utf-8 -*-
from pyduino import *
from flask import Flask, render_template, url_for
import time

app = Flask(__name__)  # 实例化app对象

# The following line is for serial over GPIO
port = 'COM3'  # note I'm using Mac OS-X

ard = serial.Serial(port, 9600)
time.sleep(2)  # wait for Arduino

i = 0

while i < 4:
    # Serial write section

    setTempCar1 = "1"
    setTempCar2 = 37
    ard.flush()
    setTemp1 = setTempCar1 + str(i) + "#"  # 10, 11, 12, 13
    setTemp2 = str(setTempCar2)
    print("Python value sent: ")
    print(setTemp1)
    ard.write(str.encode(setTemp1))
    time.sleep(1)
    # I shortened this to match the new value in your Arduino code

    # Serial read section
    msg = ard.read(ard.inWaiting())  # read all characters in buffer
    print("Message from arduino: ")
    print(bytes.decode(msg))
    i = i + 1
else:
    print("Exiting")
exit()
