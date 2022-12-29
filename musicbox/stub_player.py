from melodies.note import Note
import time


class Player:
    def __init__(self):
        pass

    def play(note: Note, whole_note: int):
        print(note.pitch)
        time.sleep(note.calculate_duration(whole_note)/1000)
