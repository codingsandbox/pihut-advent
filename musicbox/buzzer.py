from machine import Pin, PWM


class Buzzer:
    VOLUME_OFF = 0

    def __init__(self, gpio: int):
        self.buzzer = PWM(Pin(gpio))
        self.buzzer.duty_u16(Buzzer.VOLUME_OFF)
        self.volume = Buzzer.VOLUME_OFF

    def set_volume(self, volume: int):
        self.volume = volume
        self.buzzer.duty_u16(volume)

    def speak(self, frequency: int):
        if frequency >= 10:
            self.buzzer.duty_u16(self.volume)
            self.buzzer.freq(frequency)

    def off(self):
        self.buzzer.duty_u16(Buzzer.VOLUME_OFF)
