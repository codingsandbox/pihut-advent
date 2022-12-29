from machine import Pin
import time

sleep_duration_ms = 250

green = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
red = Pin(20, Pin.OUT)

leds = [green, amber, red]

button1 = Pin(3, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(8, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(13, Pin.IN, Pin.PULL_DOWN)

buttons = [button1, button2, button3]

for led in leds:
    led.off()

while True:
    # Debounce.
    time.sleep_ms(200)

    for i, button in enumerate(buttons):
        if button.value() == 1:
            leds[i].toggle()
