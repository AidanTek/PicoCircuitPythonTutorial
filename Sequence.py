import board
import neopixel
from time import sleep

# Update this to match the number of NeoPixel LEDs connected to your board.
num_pixels = 5

pixels = neopixel.NeoPixel(board.GP22, num_pixels)
pixels.brightness = 0.5

while True:
    pixels.fill((0, 0, 0))
    sleep(0.2)
    
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
    
    