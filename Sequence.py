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
    # use .fill to clear the pixels
    pixels.fill((0, 0, 0))
    sleep(0.2)
    
    # Switch on pixels one at a time, note use of .show()
    pixels[0] = (0, 255, 0)
    pixels.show()
    sleep(0.2)
    
    pixels[1] = (0, 255, 0)
    pixels.show()
    sleep(0.2)
    
    pixels[2] = (0, 255, 0)
    pixels.show()
    sleep(0.2)
    
    pixels[3] = (0, 255, 0)
    pixels.show()
    sleep(0.2)
    
    pixels[4] = (0, 255, 0)
    pixels.show()
    sleep(0.2)
    
    