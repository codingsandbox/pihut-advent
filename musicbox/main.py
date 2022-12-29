from machine import Pin
import time
import buzzer
import music
from melodies import zeldas_lullaby, harry_potter, imperial_march, song_of_storms, super_mario, tetris
import uasyncio

green = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
red = Pin(20, Pin.OUT)

play = Pin(3, Pin.IN, Pin.PULL_DOWN)
previous = Pin(8, Pin.IN, Pin.PULL_DOWN)
next = Pin(13, Pin.IN, Pin.PULL_DOWN)


def on_play(player):
    green.off()
    red.off()
    if player.is_playing():
        red.on()
        player.stop()
    else:
        green.on()
        player.play()


async def main():
    songs = [zeldas_lullaby.SONG, harry_potter.SONG,
             imperial_march.SONG, song_of_storms.SONG, super_mario.SONG, tetris.SONG]
    speaker = buzzer.Buzzer(5)
    player = music.Player(speaker, songs)

    speaker.set_volume(0)

    for led in [green, amber, red]:
        led.off()

    red.on()

    while True:
        # Debounce.
        await uasyncio.sleep_ms(200)
        amber.off()

        if play.value() == 1:
            on_play(player)
            amber.on()

        if previous.value() == 1:
            player.previous()
            amber.on()

        if next.value() == 1:
            player.next()
            amber.on()

uasyncio.run(main())
