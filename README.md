# CircuitPython on the Raspberry Pi Pico Tutorial

This repository contains supporting material for an introductory class in CircuitPython on the Pico using Neopixels 

### 1. Getting Started

You need the following electronic components for this tutorial:
- Raspberry Pi Pico
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

### 4. NeoPixel Module Setup

NeoPixels are addressable LEDs - this means that you can connect lots of them together in a chain and a tiny brain on each "pixel" allows you to individually address them. Each pixel can be set with an RGB colour and brightness. 

1. [Download the Adafruit CircuitPython Library bundle here](https://circuitpython.org/libraries) Download the version corresponding to your installation of CircuitPython
2. Unzip the downloaded folder and save it somewhere sensible on your computer. Unzipping took a little time on my computer.
3. Locate the file called neopixel.mpy in the bundle folder - it will be near the bottom! Copy it to the *lib* folder on the Pico drive (CIRCUITPY)

### 5. Hardware Setup

Be careful with this step!! Unplug the Pico whilst you are making connections.

1. Look at the NeoPixel PCB (ZipStick), flip it on its back and you will see the connections at the end are labelled GND, DIN and 5VDC.
2. Look underneath the Pico to see how the pins are labelled, note 3v3, GND and GP22 as we will use these.
2. Carefully plug the Pico into the breadboard so that the Micro USB is easily accessible at one end
3. Plug the ZipStick into the breadboard across some empty columns
4. Use the jumper wires to connect:
    - ZipStick GND to Pico GND
    - ZipStick 5VDC to Pico 3v3
    - ZipStick DIN to GP22

[Find a reference for the Raspberry Pi Pico here](https://datasheets.raspberrypi.com/pico/Pico-R3-A4-Pinout.pdf)

You are now ready to test out some of the examples shared in this repository, simply open them and copy and paste the code into Thonny. Press the RUN button to see what they do.
