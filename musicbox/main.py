from machine import Pin, ADC, I2C
import time
import buzzer
import music
from melodies import zeldas_lullaby, harry_potter, imperial_march, song_of_storms, super_mario, tetris
import uasyncio
from ssd1306 import SSD1306_I2C
from analogue import Analogue

green = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
red = Pin(20, Pin.OUT)

play = Pin(3, Pin.IN, Pin.PULL_DOWN)
previous = Pin(8, Pin.IN, Pin.PULL_DOWN)
next = Pin(13, Pin.IN, Pin.PULL_DOWN)

volume = Analogue(ADC(Pin(27)))

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
display = SSD1306_I2C(128, 32, i2c)


def on_play(player):
    green.off()
    red.off()
    if player.is_playing():
        red.on()
        player.stop()
    else:
        green.on()
        player.play()


def refresh_display(display, player):
    display.fill(0)
    display.text(player.song(), 0, 0)
    display.show()


async def main():
    songs = [zeldas_lullaby.SONG, harry_potter.SONG,
             imperial_march.SONG, song_of_storms.SONG, super_mario.SONG, tetris.SONG]
    speaker = buzzer.Buzzer(5)
    player = music.Player(speaker, songs)

    speaker.set_volume(0)

    for led in [green, amber, red]:
        led.off()

    red.on()

    refresh_display(display, player)

    while True:
        # Debounce.
        await uasyncio.sleep_ms(200)
        speaker.set_volume(volume.read())

        amber.off()

        if play.value() == 1:
            on_play(player)
            amber.on()

        if previous.value() == 1:
            player.previous()
            refresh_display(display, player)
            amber.on()

        if next.value() == 1:
            player.next()
            refresh_display(display, player)
            amber.on()

uasyncio.run(main())
