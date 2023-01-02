from machine import Pin, PWM
import uasyncio

class Buzzer:
    """
    Not thread safe. Probably needs some mutex or something.
    """
    VOLUME_OFF = 0

    def __init__(self, gpio: int):
        self.buzzer = PWM(Pin(gpio))
        self.buzzer.duty_u16(Buzzer.VOLUME_OFF)
        self.volume = Buzzer.VOLUME_OFF
        self.mutex = uasyncio.Lock()

    def set_volume(self, volume: int):
        self.volume = volume

    def speak(self, frequency: int):
        if frequency >= 10:
            self.buzzer.duty_u16(int(self.volume))
            self.buzzer.freq(frequency)

    def off(self):
        self.buzzer.duty_u16(Buzzer.VOLUME_OFF)

    def _is_speaking(self):
        return self.buzzer.duty_u16() != Buzzer.VOLUME_OFF
