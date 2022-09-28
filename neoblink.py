import board # board module lets us use the hardware
import neopixel # add the neopixel module
from time import sleep # add the sleep module

# Update this to match the number of NeoPixel LEDs connected to your board.
num_pixels = 5

# Set up neopixel module with an object called 'pixels'
pixels = neopixel.NeoPixel(board.GP22, num_pixels)

# Set brightness between 0. and 1.
pixels.brightness = 0.5

while True:
    pixels.fill((255, 0, 0))
    sleep(1)
    pixels.fill((0, 0, 0))
    sleep(1)
