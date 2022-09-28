# CircuitPython on the Raspberry Pi Pico Tutorial

This repository contains supporting material for an introductory class in CircuitPython on the Pico using Neopixels 

### 1. Getting Started

You need the following electronic components for this tutorial:
- Raspberry Pi Pico (Pico W is ok as well)
- USB Micro lead to program the Pico
- Half size breadboard
- Neopixels (5 is a good number)
- Jumper wires to connect things

Identify and gather these items now

### 2. Install CircuitPython on the Pico

CircuitPython by Adafruit is not installed on the Pico when it is shipped - but it is easy to install.

1. [Download CircuitPython here](https://circuitpython.org/board/raspberry_pi_pico/)
2. Plug the Raspberry Pi Pico into your computer using the USB lead, while holding down the BOOTSEL button. This will make it appear as a USB drive.
3. Drag and drop the downloaded CircuitPython file onto the Pico drive. This will make it reboot and it will now appear like a USB drive called CIRCUITPY.

Done!

### 3. Install Thonny and setup for CircuitPython

Thonny is a free text editor with lots of helpful features for creating Python programs

1. [Download Thonny here](https://thonny.org/)
2. Once downloaded, open Thonny. It should launch a window
3. Click in the very bottom right corner where it lists the Python version (e.g. Python 3.7.9) and select CircuitPython
4. You may need to do this step, at the top of the Thonny window, click the "Run" menu and select Stop/Restart backend
5. If you can see >>> in the Shell window at the bottom of the screen, you are good to go!

### 4. Neopixel connections
