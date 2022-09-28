import board # board module lets us use the hardware
import neopixel # add the neopixel module
from time import sleep # add the sleep module
from random import randint # add the randint module

# Update this to match the number of NeoPixel LEDs connected to your board.
num_pixels = 5

# Set up neopixel module with an object called 'pixels'
pixels = neopixel.NeoPixel(board.GP22, num_pixels)

# Set brightness between 0. and 1.
pixels.brightness = 0.2

while True:
    # randint generates a random number in a set range:
    R = randint(0,255)
    G = randint(0,127)
    x = randint(0,4)
    
    # Note how variables are used below:
    pixels[x] = (R, G, 0)
    pixels.show()
    
    sleep(0.03)
