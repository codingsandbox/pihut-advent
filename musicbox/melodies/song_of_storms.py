from melodies.note import Note, Pitch, Duration, Song

# Adapted from:
# https://github.com/robsoncouto/arduino-songs/blob/master/zeldaslullaby/zeldaslullaby.ino

TEMPO = 108
WHOLE_NOTE = (60000 * 4)/TEMPO

MELODY = [
    Note(Pitch.D4, Duration.QUARTER), Note(
        Pitch.A4, Duration.QUARTER), Note(Pitch.A4, Duration.QUARTER),
    Note(Pitch.REST, Duration.EIGHTH), Note(
        Pitch.E4, Duration.EIGHTH), Note(Pitch.B4, Duration.HALF),
    Note(Pitch.F4, Duration.QUARTER), Note(
        Pitch.C5, Duration.QUARTER), Note(Pitch.C5, Duration.QUARTER),
    Note(Pitch.REST, Duration.EIGHTH), Note(
        Pitch.E4, Duration.EIGHTH), Note(Pitch.B4, Duration.HALF),
    Note(Pitch.D4, Duration.QUARTER), Note(
        Pitch.A4, Duration.QUARTER), Note(Pitch.A4, Duration.QUARTER),
    Note(Pitch.REST, Duration.EIGHTH), Note(
        Pitch.E4, Duration.EIGHTH), Note(Pitch.B4, Duration.HALF),
    Note(Pitch.F4, Duration.QUARTER), Note(
        Pitch.C5, Duration.QUARTER), Note(Pitch.C5, Duration.QUARTER),
    Note(Pitch.REST, Duration.EIGHTH), Note(
        Pitch.E4, Duration.EIGHTH), Note(Pitch.B4, Duration.HALF),
    Note(Pitch.D4, Duration.EIGHTH), Note(
        Pitch.F4, Duration.EIGHTH), Note(Pitch.D5, Duration.HALF),

    Note(Pitch.D4, Duration.EIGHTH), Note(
        Pitch.F4, Duration.EIGHTH), Note(Pitch.D5, Duration.HALF),
    Note(Pitch.E5, Duration.QUARTER, True), Note(Pitch.F5, Duration.EIGHTH), Note(Pitch.E5,
                                                                                  Duration.EIGHTH), Note(Pitch.E5, Duration.EIGHTH),
    Note(Pitch.E5, Duration.EIGHTH), Note(
        Pitch.C5, Duration.EIGHTH), Note(Pitch.A4, Duration.HALF),
    Note(Pitch.A4, Duration.QUARTER), Note(
        Pitch.D4, Duration.QUARTER), Note(Pitch.F4, Duration.EIGHTH), Note(Pitch.G4, Duration.EIGHTH),
    Note(Pitch.A4, Duration.HALF, True),
    Note(Pitch.A4, Duration.QUARTER), Note(
        Pitch.D4, Duration.QUARTER), Note(Pitch.F4, Duration.EIGHTH), Note(Pitch.G4, Duration.EIGHTH),
    Note(Pitch.E4, Duration.HALF, True),
    Note(Pitch.D4, Duration.EIGHTH), Note(
        Pitch.F4, Duration.EIGHTH), Note(Pitch.D5, Duration.HALF),
    Note(Pitch.D4, Duration.EIGHTH), Note(
        Pitch.F4, Duration.EIGHTH), Note(Pitch.D5, Duration.HALF),

    Note(Pitch.E5, Duration.QUARTER, True), Note(Pitch.F5, Duration.EIGHTH), Note(Pitch.E5,
                                                                                  Duration.EIGHTH), Note(Pitch.E5, Duration.EIGHTH),
    Note(Pitch.E5, Duration.EIGHTH), Note(
        Pitch.C5, Duration.EIGHTH), Note(Pitch.A4, Duration.HALF),
    Note(Pitch.A4, Duration.QUARTER), Note(
        Pitch.D4, Duration.QUARTER), Note(Pitch.F4, Duration.EIGHTH), Note(Pitch.G4, Duration.EIGHTH),
    Note(Pitch.A4, Duration.HALF), Note(Pitch.A4, Duration.QUARTER),
    Note(Pitch.D4, Duration.WHOLE),
]

SONG = Song(WHOLE_NOTE, MELODY)
