from melodies.note import Note, Pitch, Duration, Song

# Adapted from:
# https://github.com/robsoncouto/arduino-songs/blob/master/zeldaslullaby/zeldaslullaby.ino

TEMPO = 144
WHOLE_NOTE = (60000 * 4)/TEMPO

MELODY = [
    Note(Pitch.E5, Duration.QUARTER),  Note(Pitch.B4, Duration.EIGHTH),  Note(Pitch.C5, Duration.EIGHTH),  Note(
        Pitch.D5, Duration.QUARTER),  Note(Pitch.C5, Duration.EIGHTH),  Note(Pitch.B4, Duration.EIGHTH),
    Note(Pitch.A4, Duration.QUARTER),  Note(Pitch.A4, Duration.EIGHTH),  Note(Pitch.C5, Duration.EIGHTH),  Note(
        Pitch.E5, Duration.QUARTER),  Note(Pitch.D5, Duration.EIGHTH),  Note(Pitch.C5, Duration.EIGHTH),
    Note(Pitch.B4, Duration.QUARTER, True),  Note(Pitch.C5, Duration.EIGHTH),  Note(
        Pitch.D5, Duration.QUARTER),  Note(Pitch.E5, Duration.QUARTER),
    Note(Pitch.C5, Duration.QUARTER),  Note(Pitch.A4, Duration.QUARTER),  Note(Pitch.A4, Duration.EIGHTH),  Note(
        Pitch.A4, Duration.QUARTER),  Note(Pitch.B4, Duration.EIGHTH),  Note(Pitch.C5, Duration.EIGHTH),

    Note(Pitch.D5, Duration.QUARTER, True),  Note(Pitch.F5, Duration.EIGHTH),  Note(
        Pitch.A5, Duration.QUARTER),  Note(Pitch.G5, Duration.EIGHTH),  Note(Pitch.F5, Duration.EIGHTH),
    Note(Pitch.E5, Duration.QUARTER, True),  Note(Pitch.C5, Duration.EIGHTH),  Note(
        Pitch.E5, Duration.QUARTER),  Note(Pitch.D5, Duration.EIGHTH),  Note(Pitch.C5, Duration.EIGHTH),
    Note(Pitch.B4, Duration.QUARTER),  Note(Pitch.B4, Duration.EIGHTH),  Note(
        Pitch.C5, Duration.EIGHTH),  Note(Pitch.D5, Duration.QUARTER),  Note(Pitch.E5, Duration.QUARTER),
    Note(Pitch.C5, Duration.QUARTER),  Note(Pitch.A4, Duration.QUARTER),  Note(
        Pitch.A4, Duration.QUARTER), Note(Pitch.REST, Duration.QUARTER),

    Note(Pitch.E5, Duration.QUARTER),  Note(Pitch.B4, Duration.EIGHTH),  Note(Pitch.C5, Duration.EIGHTH),  Note(
        Pitch.D5, Duration.QUARTER),  Note(Pitch.C5, Duration.EIGHTH),  Note(Pitch.B4, Duration.EIGHTH),
    Note(Pitch.A4, Duration.QUARTER),  Note(Pitch.A4, Duration.EIGHTH),  Note(Pitch.C5, Duration.EIGHTH),  Note(
        Pitch.E5, Duration.QUARTER),  Note(Pitch.D5, Duration.EIGHTH),  Note(Pitch.C5, Duration.EIGHTH),
    Note(Pitch.B4, Duration.QUARTER, True),  Note(Pitch.C5, Duration.EIGHTH),  Note(
        Pitch.D5, Duration.QUARTER),  Note(Pitch.E5, Duration.QUARTER),
    Note(Pitch.C5, Duration.QUARTER),  Note(Pitch.A4, Duration.QUARTER),  Note(Pitch.A4, Duration.EIGHTH),  Note(
        Pitch.A4, Duration.QUARTER),  Note(Pitch.B4, Duration.EIGHTH),  Note(Pitch.C5, Duration.EIGHTH),

    Note(Pitch.D5, Duration.QUARTER, True),  Note(Pitch.F5, Duration.EIGHTH),  Note(
        Pitch.A5, Duration.QUARTER),  Note(Pitch.G5, Duration.EIGHTH),  Note(Pitch.F5, Duration.EIGHTH),
    Note(Pitch.E5, Duration.QUARTER, True),  Note(Pitch.C5, Duration.EIGHTH),  Note(
        Pitch.E5, Duration.QUARTER),  Note(Pitch.D5, Duration.EIGHTH),  Note(Pitch.C5, Duration.EIGHTH),
    Note(Pitch.B4, Duration.QUARTER),  Note(Pitch.B4, Duration.EIGHTH),  Note(
        Pitch.C5, Duration.EIGHTH),  Note(Pitch.D5, Duration.QUARTER),  Note(Pitch.E5, Duration.QUARTER),
    Note(Pitch.C5, Duration.QUARTER),  Note(Pitch.A4, Duration.QUARTER),  Note(
        Pitch.A4, Duration.QUARTER), Note(Pitch.REST, Duration.QUARTER),


    Note(Pitch.E5, Duration.HALF),  Note(Pitch.C5, Duration.HALF),
    Note(Pitch.D5, Duration.HALF),   Note(Pitch.B4, Duration.HALF),
    Note(Pitch.C5, Duration.HALF),   Note(Pitch.A4, Duration.HALF),
    Note(Pitch.GS4, Duration.HALF),  Note(Pitch.B4, Duration.QUARTER),  Note(
        Pitch.REST, Duration.EIGHTH),
    Note(Pitch.E5, Duration.HALF),   Note(Pitch.C5, Duration.HALF),
    Note(Pitch.D5, Duration.HALF),   Note(Pitch.B4, Duration.HALF),
    Note(Pitch.C5, Duration.QUARTER),   Note(
        Pitch.E5, Duration.QUARTER),  Note(Pitch.A5, Duration.HALF),
    Note(Pitch.GS5, Duration.HALF),
]

SONG = Song("Tetris", WHOLE_NOTE, MELODY)
