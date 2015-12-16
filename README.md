# Cloud Generator
This is a python port of a cloud/noise generator for use with the FadeCandy controller to drive LED outputs. 
I wanted to use the provided perlin noise example code as a mode in an installation, but couldn't run processing on a headless Raspberry Pi.
Putting it in public in case anyone finds it useful. 

## Requirements

* This should work on Windows, Linux, OSX. I have used it on Win10, Win8, OSX, and Raspbian (Raspberry Pi)

* the included opc.py file has been modified for use with Python3. If you wish to use python 2.7, replace the opc.py file with the  file provided in the fadecandy example code. Incidentally, if you use Touch Designer, this opc.py file can be used to communicate with fadecandy server in Touch Designer. 

* You'll need to have the fadecandy server configured and running. There are several tutorials on how to get that started. I've linked one below. 

## fadecandy info
Thanks to Micah Scott for creating the FadeCandy controller and providing helpful examples!
* https://github.com/scanlime/fadecandy

## Tutorial

* Got my project started with the following tutorial: https://learn.adafruit.com/1500-neopixel-led-curtain-with-raspberry-pi-fadecandy/overview

## enjoy!


