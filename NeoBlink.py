import board
import neopixel
from time import sleep

# Update this to match the number of NeoPixel LEDs connected to your board.
num_pixels = 5

pixels = neopixel.NeoPixel(board.GP22, num_pixels)
pixels.brightness = 0.5

while True:
    pixels.fill((255, 0, 0))
    sleep(1)
    pixels.fill((0, 0, 0))
    sleep(1)