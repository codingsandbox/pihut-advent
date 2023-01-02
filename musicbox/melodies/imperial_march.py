from melodies.note import Note, Pitch, Duration, Song

# Adapted from:
# https://github.com/robsoncouto/arduino-songs/blob/master/zeldaslullaby/zeldaslullaby.ino

TEMPO = 120
WHOLE_NOTE = (60000 * 4)/TEMPO

MELODY = [
    Note(Pitch.A4, Duration.QUARTER, True), Note(
        Pitch.A4, Duration.QUARTER, True),
    Note(Pitch.A4, Duration.SIXTEENTH), Note(Pitch.A4, Duration.SIXTEENTH), Note(Pitch.A4, Duration.SIXTEENTH), Note(
        Pitch.A4, Duration.SIXTEENTH), Note(Pitch.F4, Duration.EIGHTH), Note(Pitch.REST, Duration.EIGHTH),
    Note(Pitch.A4, Duration.QUARTER, True), Note(Pitch.A4, Duration.QUARTER, True), Note(Pitch.A4, Duration.SIXTEENTH), Note(Pitch.A4,
                                                                                                                             Duration.SIXTEENTH), Note(Pitch.A4, Duration.SIXTEENTH), Note(Pitch.A4, Duration.SIXTEENTH), Note(Pitch.F4, Duration.EIGHTH), Note(Pitch.REST, Duration.EIGHTH),
    Note(Pitch.A4, Duration.QUARTER), Note(Pitch.A4, Duration.QUARTER), Note(
        Pitch.A4, Duration.QUARTER), Note(Pitch.F4, Duration.EIGHTH, True), Note(Pitch.C5, Duration.SIXTEENTH),

    Note(Pitch.A4, Duration.QUARTER), Note(Pitch.F4, Duration.EIGHTH, True), Note(
        Pitch.C5, Duration.SIXTEENTH), Note(Pitch.A4, Duration.HALF),
    Note(Pitch.E5, Duration.QUARTER), Note(Pitch.E5, Duration.QUARTER), Note(
        Pitch.E5, Duration.QUARTER), Note(Pitch.F5, Duration.EIGHTH, True), Note(Pitch.C5, Duration.SIXTEENTH),
    Note(Pitch.A4, Duration.QUARTER), Note(Pitch.F4, Duration.EIGHTH, True), Note(Pitch.C5,
                                                                                  Duration.SIXTEENTH), Note(Pitch.A4, Duration.HALF),

    Note(Pitch.A5, Duration.QUARTER), Note(Pitch.A4, Duration.EIGHTH, True), Note(Pitch.A4, Duration.SIXTEENTH), Note(
        Pitch.A5, Duration.QUARTER), Note(Pitch.GS5, Duration.EIGHTH, True), Note(Pitch.G5, Duration.SIXTEENTH),
    Note(Pitch.DS5, Duration.SIXTEENTH), Note(Pitch.D5, Duration.SIXTEENTH), Note(Pitch.DS5, Duration.EIGHTH), Note(Pitch.REST, Duration.EIGHTH), Note(
        Pitch.A4, Duration.EIGHTH), Note(Pitch.DS5, Duration.QUARTER), Note(Pitch.D5, Duration.EIGHTH, True), Note(Pitch.CS5, Duration.SIXTEENTH),

    Note(Pitch.C5, Duration.SIXTEENTH), Note(Pitch.B4, Duration.SIXTEENTH), Note(Pitch.C5, Duration.SIXTEENTH), Note(Pitch.REST, Duration.EIGHTH), Note(
        Pitch.F4, Duration.EIGHTH), Note(Pitch.GS4, Duration.QUARTER), Note(Pitch.F4, Duration.EIGHTH, True), Note(Pitch.A4, -Duration.SIXTEENTH),
    Note(Pitch.C5, Duration.QUARTER), Note(Pitch.A4, Duration.EIGHTH, True), Note(Pitch.C5,
                                                                                  Duration.SIXTEENTH), Note(Pitch.E5, Duration.HALF),

    Note(Pitch.A5, Duration.QUARTER), Note(Pitch.A4, Duration.EIGHTH, True), Note(Pitch.A4, Duration.SIXTEENTH), Note(
        Pitch.A5, Duration.QUARTER), Note(Pitch.GS5, Duration.EIGHTH, True), Note(Pitch.G5, Duration.SIXTEENTH),
    Note(Pitch.DS5, Duration.SIXTEENTH), Note(Pitch.D5, Duration.SIXTEENTH), Note(Pitch.DS5, Duration.EIGHTH), Note(Pitch.REST, Duration.EIGHTH), Note(
        Pitch.A4, Duration.EIGHTH), Note(Pitch.DS5, Duration.QUARTER), Note(Pitch.D5, Duration.EIGHTH, True), Note(Pitch.CS5, Duration.SIXTEENTH),

    Note(Pitch.C5, Duration.SIXTEENTH), Note(Pitch.B4, Duration.SIXTEENTH), Note(Pitch.C5, Duration.SIXTEENTH), Note(Pitch.REST, Duration.EIGHTH), Note(
        Pitch.F4, Duration.EIGHTH), Note(Pitch.GS4, Duration.QUARTER), Note(Pitch.F4, Duration.EIGHTH, True), Note(Pitch.A4, -Duration.SIXTEENTH),
    Note(Pitch.A4, Duration.QUARTER), Note(Pitch.F4, Duration.EIGHTH, True), Note(Pitch.C5,
                                                                                  Duration.SIXTEENTH), Note(Pitch.A4, Duration.HALF),
]

SONG = Song("Imperial March", WHOLE_NOTE, MELODY)
