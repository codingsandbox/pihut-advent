from melodies.note import Note, Pitch, Duration, Song

# Adapted from:
# https://github.com/robsoncouto/arduino-songs/blob/master/zeldaslullaby/zeldaslullaby.ino

TEMPO = 108
WHOLE_NOTE = (60000 * 4)/TEMPO

MELODY = [
    Note(Pitch.E4, Duration.HALF), Note(Pitch.G4, Duration.QUARTER),
    Note(Pitch.D4, Duration.HALF), Note(
        Pitch.C4, Duration.EIGHTH), Note(Pitch.D4, Duration.EIGHTH),
    Note(Pitch.E4, Duration.HALF), Note(Pitch.G4, Duration.QUARTER),
    Note(Pitch.D4, Duration.HALF, True),
    Note(Pitch.E4, Duration.HALF), Note(Pitch.G4, Duration.QUARTER),
    Note(Pitch.D5, Duration.HALF), Note(Pitch.C5, Duration.QUARTER),
    Note(Pitch.G4, Duration.HALF), Note(
        Pitch.F4, Duration.EIGHTH), Note(Pitch.E4, Duration.EIGHTH),
    Note(Pitch.D4, Duration.HALF, True),
    Note(Pitch.E4, Duration.HALF), Note(Pitch.G4, Duration.QUARTER),
    Note(Pitch.D4, Duration.HALF), Note(
        Pitch.C4, Duration.EIGHTH), Note(Pitch.D4, Duration.EIGHTH),
    Note(Pitch.E4, Duration.HALF), Note(Pitch.G4, Duration.QUARTER),
    Note(Pitch.D4, Duration.HALF, True),
    Note(Pitch.E4, Duration.HALF), Note(Pitch.G4, Duration.QUARTER),

    Note(Pitch.D5, Duration.HALF), Note(Pitch.C5, Duration.QUARTER),
    Note(Pitch.G4, Duration.HALF), Note(
        Pitch.F4, Duration.EIGHTH), Note(Pitch.E4, Duration.EIGHTH),
    Note(Pitch.F4, Duration.EIGHTH), Note(
        Pitch.E4, Duration.EIGHTH), Note(Pitch.C4, Duration.HALF),
    Note(Pitch.F4, Duration.HALF), Note(
        Pitch.E4, Duration.EIGHTH), Note(Pitch.D4, Duration.EIGHTH),
    Note(Pitch.E4, Duration.EIGHTH), Note(
        Pitch.D4, Duration.EIGHTH), Note(Pitch.A3, Duration.HALF),
    Note(Pitch.G4, Duration.HALF), Note(
        Pitch.F4, Duration.EIGHTH), Note(Pitch.E4, Duration.EIGHTH),
    Note(Pitch.F4, Duration.EIGHTH), Note(Pitch.E4, Duration.EIGHTH), Note(
        Pitch.C4, Duration.QUARTER), Note(Pitch.F4, Duration.QUARTER),
    Note(Pitch.C5, Duration.HALF, True),
]

SONG = Song("Zelda's Lullaby", WHOLE_NOTE, MELODY)
