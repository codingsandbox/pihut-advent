from melodies.note import Note, Pitch, Duration, Song

# Adapted from:
# https://github.com/robsoncouto/arduino-songs/blob/master/zeldaslullaby/zeldaslullaby.ino

TEMPO = 108
WHOLE_NOTE = (60000 * 4)/TEMPO

MELODY = [
    Note(Pitch.AS4, Duration.EIGHTH), Note(
        Pitch.AS4, Duration.EIGHTH), Note(Pitch.AS4, Duration.EIGHTH),
    Note(Pitch.F5, Duration.HALF), Note(Pitch.C6, Duration.HALF),
    Note(Pitch.AS5, Duration.EIGHTH), Note(Pitch.A5, Duration.EIGHTH), Note(
        Pitch.G5, Duration.EIGHTH), Note(Pitch.F6, Duration.HALF), Note(Pitch.C6, Duration.QUARTER),
    Note(Pitch.AS5, Duration.EIGHTH), Note(Pitch.A5, Duration.EIGHTH), Note(
        Pitch.G5, Duration.EIGHTH), Note(Pitch.F6, Duration.HALF), Note(Pitch.C6, Duration.QUARTER),
    Note(Pitch.AS5, Duration.EIGHTH), Note(Pitch.A5, Duration.EIGHTH), Note(Pitch.AS5, Duration.EIGHTH), Note(
        Pitch.G5, Duration.HALF), Note(Pitch.C5, Duration.EIGHTH), Note(Pitch.C5, Duration.EIGHTH), Note(Pitch.C5, Duration.EIGHTH),
    Note(Pitch.F5, Duration.HALF), Note(Pitch.C6, Duration.HALF),
    Note(Pitch.AS5, Duration.EIGHTH), Note(Pitch.A5, Duration.EIGHTH), Note(
        Pitch.G5, Duration.EIGHTH), Note(Pitch.F6, Duration.HALF), Note(Pitch.C6, Duration.QUARTER),

    Note(Pitch.AS5, Duration.EIGHTH), Note(Pitch.A5, Duration.EIGHTH), Note(Pitch.G5,
                                                                            Duration.EIGHTH), Note(Pitch.F6, Duration.HALF), Note(Pitch.C6, Duration.QUARTER),
    Note(Pitch.AS5, Duration.EIGHTH), Note(Pitch.A5, Duration.EIGHTH), Note(Pitch.AS5, Duration.EIGHTH), Note(
        Pitch.G5, Duration.HALF), Note(Pitch.C5, Duration.EIGHTH, True), Note(Pitch.C5, Duration.SIXTEENTH),
    Note(Pitch.D5, Duration.QUARTER, True), Note(Pitch.D5, Duration.EIGHTH), Note(Pitch.AS5, Duration.EIGHTH), Note(
        Pitch.A5, Duration.EIGHTH), Note(Pitch.G5, Duration.EIGHTH), Note(Pitch.F5, Duration.EIGHTH),
    Note(Pitch.F5, Duration.EIGHTH), Note(Pitch.G5, Duration.EIGHTH), Note(Pitch.A5, Duration.EIGHTH), Note(Pitch.G5, Duration.QUARTER), Note(
        Pitch.D5, Duration.EIGHTH), Note(Pitch.E5, Duration.QUARTER), Note(Pitch.C5, Duration.EIGHTH, True), Note(Pitch.C5, Duration.SIXTEENTH),
    Note(Pitch.D5, Duration.QUARTER, True), Note(Pitch.D5, Duration.EIGHTH), Note(Pitch.AS5, Duration.EIGHTH), Note(
        Pitch.A5, Duration.EIGHTH), Note(Pitch.G5, Duration.EIGHTH), Note(Pitch.F5, Duration.EIGHTH),

    Note(Pitch.C6, Duration.EIGHTH, True), Note(Pitch.G5, Duration.SIXTEENTH), Note(
        Pitch.G5, Duration.HALF), REST, Duration.EIGHTH, Note(Pitch.C5, Duration.EIGHTH),
    Note(Pitch.D5, Duration.QUARTER, True), Note(Pitch.D5, Duration.EIGHTH), Note(Pitch.AS5, Duration.EIGHTH), Note(
        Pitch.A5, Duration.EIGHTH), Note(Pitch.G5, Duration.EIGHTH), Note(Pitch.F5, Duration.EIGHTH),
    Note(Pitch.F5, Duration.EIGHTH), Note(Pitch.G5, Duration.EIGHTH), Note(Pitch.A5, Duration.EIGHTH), Note(Pitch.G5, Duration.QUARTER), Note(
        Pitch.D5, Duration.EIGHTH), Note(Pitch.E5, Duration.QUARTER), Note(Pitch.C6, Duration.EIGHTH, True), Note(Pitch.C6, Duration.SIXTEENTH),
    Note(Pitch.F6, Duration.QUARTER), Note(Pitch.DS6, Duration.EIGHTH), Note(Pitch.CS6, Duration.QUARTER), Note(Pitch.C6, Duration.EIGHTH), Note(
        Pitch.AS5, Duration.QUARTER), Note(Pitch.GS5, Duration.EIGHTH), Note(Pitch.G5, Duration.QUARTER), Note(Pitch.F5, Duration.EIGHTH),
    Note(Pitch.C6, Duration.WHOLE)
]

SONG = Song(WHOLE_NOTE, MELODY)
