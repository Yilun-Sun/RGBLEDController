# -*- coding: utf-8 -*-
from pyduino import *
from flask import Flask, render_template, url_for
import time

app = Flask(__name__)

# The following line is for serial over GPIO
port = 'COM3'  # note I'm using Mac OS-X

ard = serial.Serial(port, 9600)
time.sleep(2)  # wait for Arduino


@app.route('/')
def index():
    return render_template('index.html')


current_state = 0
# rgb_intensity = "200000000"


@app.route('/set_rgb/<rgb_intensity>')
def set_rgb(rgb_intensity):
    print("Python value sent: " + rgb_intensity)
    ard.write(str.encode(rgb_intensity + "#"))
    return render_template('index.html')


@app.route('/led_switch')
def led_switch():
    global current_state
    if current_state == 0:
        print("Python value sent: HIGH")
        ard.write(str.encode("200200200#"))
        current_state = 1
    elif current_state == 1:
        print("Python value sent: LOW")
        ard.write(str.encode("050050050#"))
        current_state = 0

    return render_template('index.html')


if __name__ == '__main__':
    app.run()
