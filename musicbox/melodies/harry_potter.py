from melodies.note import Note, Pitch, Duration, Song

# Adapted from:
# https://github.com/robsoncouto/arduino-songs/blob/master/zeldaslullaby/zeldaslullaby.ino

TEMPO = 144
WHOLE_NOTE = (60000 * 4)/TEMPO

MELODY = [
    Note(Pitch.REST, Duration.HALF), Note(Pitch.D4, Duration.QUARTER),
    Note(Pitch.G4, Duration.QUARTER, True), Note(
        Pitch.AS4, Duration.EIGHTH), Note(Pitch.A4, Duration.QUARTER),
    Note(Pitch.G4, Duration.HALF), Note(Pitch.D5, Duration.QUARTER),
    Note(Pitch.C5, Duration.HALF, True),
    Note(Pitch.A4, Duration.HALF, True),
    Note(Pitch.G4, Duration.QUARTER, True), Note(
        Pitch.AS4, Duration.EIGHTH), Note(Pitch.A4, Duration.QUARTER),
    Note(Pitch.F4, Duration.HALF), Note(Pitch.GS4, Duration.QUARTER),
    Note(Pitch.D4, Duration.WHOLE, True),
    Note(Pitch.D4, Duration.QUARTER),

    Note(Pitch.G4, Duration.QUARTER, True), Note(
        Pitch.AS4, Duration.EIGHTH), Note(Pitch.A4, Duration.QUARTER),
    Note(Pitch.G4, Duration.HALF), Note(Pitch.D5, Duration.QUARTER),
    Note(Pitch.F5, Duration.HALF), Note(Pitch.E5, Duration.QUARTER),
    Note(Pitch.DS5, Duration.HALF), Note(Pitch.B4, Duration.QUARTER),
    Note(Pitch.DS5, Duration.QUARTER, True), Note(
        Pitch.D5, Duration.EIGHTH), Note(Pitch.CS5, Duration.QUARTER),
    Note(Pitch.CS4, Duration.HALF), Note(Pitch.B4, Duration.QUARTER),
    Note(Pitch.G4, Duration.WHOLE, True),
    Note(Pitch.AS4, Duration.QUARTER),

    Note(Pitch.D5, Duration.HALF), Note(Pitch.AS4, Duration.QUARTER),
    Note(Pitch.D5, Duration.HALF), Note(Pitch.AS4, Duration.QUARTER),
    Note(Pitch.DS5, Duration.HALF), Note(Pitch.D5, Duration.QUARTER),
    Note(Pitch.CS5, Duration.HALF), Note(Pitch.A4, Duration.QUARTER),
    Note(Pitch.AS4, Duration.QUARTER, True), Note(
        Pitch.D5, Duration.EIGHTH), Note(Pitch.CS5, Duration.QUARTER),
    Note(Pitch.CS4, Duration.HALF), Note(Pitch.D4, Duration.QUARTER),
    Note(Pitch.D5, Duration.WHOLE, True),
    Note(Pitch.REST, Duration.QUARTER), Note(Pitch.AS4, Duration.QUARTER),

    Note(Pitch.D5, Duration.HALF), Note(Pitch.AS4, Duration.QUARTER),
    Note(Pitch.D5, Duration.HALF), Note(Pitch.AS4, Duration.QUARTER),
    Note(Pitch.F5, Duration.HALF), Note(Pitch.E5, Duration.QUARTER),
    Note(Pitch.DS5, Duration.HALF), Note(Pitch.B4, Duration.QUARTER),
    Note(Pitch.DS5, Duration.QUARTER, True), Note(
        Pitch.D5, Duration.EIGHTH), Note(Pitch.CS5, Duration.QUARTER),
    Note(Pitch.CS4, Duration.HALF), Note(Pitch.AS4, Duration.QUARTER),
    Note(Pitch.G4, Duration.WHOLE, True),
]

SONG = Song(WHOLE_NOTE, MELODY)
