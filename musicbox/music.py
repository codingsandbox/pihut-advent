import uasyncio


class Track:
    def __init__(self, speaker):
        self.speaker = speaker

    async def play(self, song):
        print(song)
        try:
            self.speaker.set_volume(100)
            note_idx = 0
            while True:
                note = song.melody[note_idx]
                self.speaker.speak(note.pitch)
                await uasyncio.sleep_ms(note.calculate_duration(
                    song.whole_note))
                self.speaker.off()
                note_idx = (note_idx + 1) % len(song.melody)
                print("playing")
        except uasyncio.CancelledError:
            print("cancelled")
            self.speaker.off()
        print("done play")


class Player:
    def __init__(self, speaker, songs):
        self.current_song = 0
        self.songs = songs
        self.track = Track(speaker)
        self.session = None

    def play(self):
        if self.is_playing():
            self.stop()

        print("start playing...")
        self.session = uasyncio.create_task(
            self.track.play(self.songs[self.current_song]))

    def stop(self):
        print("stop")
        self.session.cancel()
        self.session = None

    def is_playing(self):
        return self.session is not None

    def next(self):
        self.current_song = (self.current_song + 1) % len(self.songs)
        self.play()

    def previous(self):
        self.current_song = (self.current_song - 1) % len(self.songs)
        self.play()
