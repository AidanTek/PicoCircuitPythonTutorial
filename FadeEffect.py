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
    # a for command will tell the program to repeat something a set number of times
    for fade in range(0,255):
        pixels.fill((0, 0, fade))
        sleep(0.01)
    
    for fade in range(0,255):
        pixels.fill((0, 0, 255-fade))
        sleep(0.01)
        