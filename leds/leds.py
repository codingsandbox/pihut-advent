from machine import Pin
import time

sleep_duration_ms = 250

green = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
red = Pin(20, Pin.OUT)

leds = [green, amber, red]
for led in leds:
    led.off()

while True:
    for led in leds:
        led.toggle()
        time.sleep_ms(sleep_duration_ms)
        led.toggle()
    for led in reversed(leds):
        led.toggle()
        time.sleep_ms(sleep_duration_ms)
        led.toggle()
