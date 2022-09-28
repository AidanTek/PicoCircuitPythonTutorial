import board # board module lets us use the hardware
import neopixel # add the neopixel module

# Update this to match the number of NeoPixel LEDs connected to your board.
num_pixels = 5

# Set up neopixel module with an object called 'pixels'
pixels = neopixel.NeoPixel(board.GP22, num_pixels)

# Set brightness between 0. and 1.
pixels.brightness = 0.5

while True:
    # .fill sets all pixels to an RGB value instantly
    pixels.fill((255, 0, 0))
