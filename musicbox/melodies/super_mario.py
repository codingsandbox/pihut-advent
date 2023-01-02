from melodies.note import Note, Pitch, Duration, Song

# Adapted from:
# https:#github.com/robsoncouto/arduino-songs/blob/master/zeldaslullaby/zeldaslullaby.ino

TEMPO = 200
WHOLE_NOTE = (60000 * 4)/TEMPO

MELODY = [
    Note(Pitch.E5, Duration.EIGHTH), Note(Pitch.E5, Duration.EIGHTH), Note(Pitch.REST, Duration.EIGHTH), Note(Pitch.E5,
                                                                                                              Duration.EIGHTH), Note(Pitch.REST, Duration.EIGHTH), Note(Pitch.C5, Duration.EIGHTH), Note(Pitch.E5, Duration.EIGHTH),  # 1
    Note(Pitch.G5, Duration.QUARTER), Note(Pitch.REST, Duration.QUARTER), Note(
        Pitch.G4, Duration.EIGHTH), Note(Pitch.REST, Duration.QUARTER),
    Note(Pitch.C5, Duration.QUARTER, True), Note(Pitch.G4, Duration.EIGHTH), Note(
        Pitch.REST, Duration.QUARTER), Note(Pitch.E4, Duration.QUARTER, True),  # 3
    Note(Pitch.A4, Duration.QUARTER), Note(Pitch.B4, Duration.QUARTER), Note(
        Pitch.AS4, Duration.EIGHTH), Note(Pitch.A4, Duration.QUARTER),
    Note(Pitch.G4, Duration.EIGHTH, True), Note(Pitch.E5, Duration.EIGHTH, True), Note(Pitch.G5, Duration.EIGHTH, True), Note(Pitch.A5,
                                                                                                                              Duration.QUARTER), Note(Pitch.F5, Duration.EIGHTH), Note(Pitch.G5, Duration.EIGHTH),
    Note(Pitch.REST, Duration.EIGHTH), Note(Pitch.E5, Duration.QUARTER), Note(Pitch.C5,
                                                                              Duration.EIGHTH), Note(Pitch.D5, Duration.EIGHTH), Note(Pitch.B4, Duration.QUARTER, True),
    Note(Pitch.C5, Duration.QUARTER, True), Note(Pitch.G4, Duration.EIGHTH), Note(
        Pitch.REST, Duration.QUARTER), Note(Pitch.E4, Duration.QUARTER, True),  # repeats from 3
    Note(Pitch.A4, Duration.QUARTER), Note(Pitch.B4, Duration.QUARTER), Note(
        Pitch.AS4, Duration.EIGHTH), Note(Pitch.A4, Duration.QUARTER),
    Note(Pitch.G4, Duration.EIGHTH, True), Note(Pitch.E5, Duration.EIGHTH, True), Note(Pitch.G5, Duration.EIGHTH, True), Note(Pitch.A5,
                                                                                                                              Duration.QUARTER), Note(Pitch.F5, Duration.EIGHTH), Note(Pitch.G5, Duration.EIGHTH),
    Note(Pitch.REST, Duration.EIGHTH), Note(Pitch.E5, Duration.QUARTER), Note(Pitch.C5,
                                                                              Duration.EIGHTH), Note(Pitch.D5, Duration.EIGHTH), Note(Pitch.B4, Duration.QUARTER, True),


    Note(Pitch.REST, Duration.QUARTER), Note(Pitch.G5, Duration.EIGHTH), Note(Pitch.FS5, Duration.EIGHTH), Note(
        Pitch.F5, Duration.EIGHTH), Note(Pitch.DS5, Duration.QUARTER), Note(Pitch.E5, Duration.EIGHTH),  # 7
    Note(Pitch.REST, Duration.EIGHTH), Note(Pitch.GS4, Duration.EIGHTH), Note(Pitch.A4, Duration.EIGHTH), Note(Pitch.C4, Duration.EIGHTH), Note(
        Pitch.REST, Duration.EIGHTH), Note(Pitch.A4, Duration.EIGHTH), Note(Pitch.C5, Duration.EIGHTH), Note(Pitch.D5, Duration.EIGHTH),
    Note(Pitch.REST, Duration.QUARTER), Note(Pitch.DS5, Duration.QUARTER), Note(
        Pitch.REST, Duration.EIGHTH), Note(Pitch.D5, Duration.QUARTER, True),
    Note(Pitch.C5, Duration.HALF), Note(Pitch.REST, Duration.HALF),

    Note(Pitch.REST, Duration.QUARTER), Note(Pitch.G5, Duration.EIGHTH), Note(Pitch.FS5, Duration.EIGHTH), Note(
        Pitch.F5, Duration.EIGHTH), Note(Pitch.DS5, Duration.QUARTER), Note(Pitch.E5, Duration.EIGHTH),  # repeats from 7
    Note(Pitch.REST, Duration.EIGHTH), Note(Pitch.GS4, Duration.EIGHTH), Note(Pitch.A4, Duration.EIGHTH), Note(Pitch.C4, Duration.EIGHTH), Note(
        Pitch.REST, Duration.EIGHTH), Note(Pitch.A4, Duration.EIGHTH), Note(Pitch.C5, Duration.EIGHTH), Note(Pitch.D5, Duration.EIGHTH),
    Note(Pitch.REST, Duration.QUARTER), Note(Pitch.DS5, Duration.QUARTER), Note(
        Pitch.REST, Duration.EIGHTH), Note(Pitch.D5, Duration.QUARTER, True),
    Note(Pitch.C5, Duration.HALF), Note(Pitch.REST, Duration.HALF),

    Note(Pitch.C5, Duration.EIGHTH), Note(Pitch.C5, Duration.QUARTER), Note(Pitch.C5, Duration.EIGHTH), Note(
        Pitch.REST, Duration.EIGHTH), Note(Pitch.C5, Duration.EIGHTH), Note(Pitch.D5, Duration.QUARTER),  # 11
    Note(Pitch.E5, Duration.EIGHTH), Note(Pitch.C5, Duration.QUARTER), Note(
        Pitch.A4, Duration.EIGHTH), Note(Pitch.G4, Duration.HALF),

    Note(Pitch.C5, Duration.EIGHTH), Note(Pitch.C5, Duration.QUARTER), Note(Pitch.C5, Duration.EIGHTH), Note(Pitch.REST,
                                                                                                             Duration.EIGHTH), Note(Pitch.C5, Duration.EIGHTH), Note(Pitch.D5, Duration.EIGHTH), Note(Pitch.E5, Duration.EIGHTH),  # 13
    Note(Pitch.REST, Duration.WHOLE),
    Note(Pitch.C5, Duration.EIGHTH), Note(Pitch.C5, Duration.QUARTER), Note(Pitch.C5, Duration.EIGHTH), Note(
        Pitch.REST, Duration.EIGHTH), Note(Pitch.C5, Duration.EIGHTH), Note(Pitch.D5, Duration.QUARTER),
    Note(Pitch.E5, Duration.EIGHTH), Note(Pitch.C5, Duration.QUARTER), Note(
        Pitch.A4, Duration.EIGHTH), Note(Pitch.G4, Duration.HALF),
    Note(Pitch.E5, Duration.EIGHTH), Note(Pitch.E5, Duration.EIGHTH), Note(Pitch.REST, Duration.EIGHTH), Note(Pitch.E5,
                                                                                                              Duration.EIGHTH), Note(Pitch.REST, Duration.EIGHTH), Note(Pitch.C5, Duration.EIGHTH), Note(Pitch.E5, Duration.QUARTER),
    Note(Pitch.G5, Duration.QUARTER), Note(Pitch.REST, Duration.QUARTER), Note(
        Pitch.G4, Duration.QUARTER), Note(Pitch.REST, Duration.QUARTER),
    Note(Pitch.C5, Duration.QUARTER, True), Note(Pitch.G4, Duration.EIGHTH), Note(
        Pitch.REST, Duration.QUARTER), Note(Pitch.E4, Duration.QUARTER, True),  # 19

    Note(Pitch.A4, Duration.QUARTER), Note(Pitch.B4, Duration.QUARTER), Note(
        Pitch.AS4, Duration.EIGHTH), Note(Pitch.A4, Duration.QUARTER),
    Note(Pitch.G4, Duration.EIGHTH, True), Note(Pitch.E5, Duration.EIGHTH, True), Note(Pitch.G5, Duration.EIGHTH, True), Note(Pitch.A5,
                                                                                                                              Duration.QUARTER), Note(Pitch.F5, Duration.EIGHTH), Note(Pitch.G5, Duration.EIGHTH),
    Note(Pitch.REST, Duration.EIGHTH), Note(Pitch.E5, Duration.QUARTER), Note(Pitch.C5,
                                                                              Duration.EIGHTH), Note(Pitch.D5, Duration.EIGHTH), Note(Pitch.B4, Duration.QUARTER, True),

    Note(Pitch.C5, Duration.QUARTER, True), Note(Pitch.G4, Duration.EIGHTH), Note(
        Pitch.REST, Duration.QUARTER), Note(Pitch.E4, Duration.QUARTER, True),  # repeats from 19
    Note(Pitch.A4, Duration.QUARTER), Note(Pitch.B4, Duration.QUARTER), Note(
        Pitch.AS4, Duration.EIGHTH), Note(Pitch.A4, Duration.QUARTER),
    Note(Pitch.G4, Duration.EIGHTH, True), Note(Pitch.E5, Duration.EIGHTH, True), Note(Pitch.G5, Duration.EIGHTH, True), Note(Pitch.A5,
                                                                                                                              Duration.QUARTER), Note(Pitch.F5, Duration.EIGHTH), Note(Pitch.G5, Duration.EIGHTH),
    Note(Pitch.REST, Duration.EIGHTH), Note(Pitch.E5, Duration.QUARTER), Note(Pitch.C5,
                                                                              Duration.EIGHTH), Note(Pitch.D5, Duration.EIGHTH), Note(Pitch.B4, Duration.QUARTER, True),

    Note(Pitch.E5, Duration.EIGHTH), Note(Pitch.C5, Duration.QUARTER), Note(Pitch.G4,
                                                                            Duration.EIGHTH), Note(Pitch.REST, Duration.QUARTER), Note(Pitch.GS4, Duration.QUARTER),  # 23
    Note(Pitch.A4, Duration.EIGHTH), Note(Pitch.F5, Duration.QUARTER), Note(
        Pitch.F5, Duration.EIGHTH), Note(Pitch.A4, Duration.HALF),
    Note(Pitch.D5, Duration.EIGHTH, True), Note(Pitch.A5, Duration.EIGHTH, True), Note(Pitch.A5, Duration.EIGHTH, True), Note(Pitch.A5,
                                                                                                                              Duration.EIGHTH, True), Note(Pitch.G5, Duration.EIGHTH, True), Note(Pitch.F5, Duration.EIGHTH, True),

    Note(Pitch.E5, Duration.EIGHTH), Note(Pitch.C5, Duration.QUARTER), Note(
        Pitch.A4, Duration.EIGHTH), Note(Pitch.G4, Duration.HALF),  # 26
    Note(Pitch.E5, Duration.EIGHTH), Note(Pitch.C5, Duration.QUARTER), Note(Pitch.G4,
                                                                            Duration.EIGHTH), Note(Pitch.REST, Duration.QUARTER), Note(Pitch.GS4, Duration.QUARTER),
    Note(Pitch.A4, Duration.EIGHTH), Note(Pitch.F5, Duration.QUARTER), Note(
        Pitch.F5, Duration.EIGHTH), Note(Pitch.A4, Duration.HALF),
    Note(Pitch.B4, Duration.EIGHTH), Note(Pitch.F5, Duration.QUARTER), Note(
        Pitch.F5, Duration.EIGHTH), Note(Pitch.F5, Duration.EIGHTH, True), Note(Pitch.E5, Duration.EIGHTH, True), Note(Pitch.D5, Duration.EIGHTH, True),
    Note(Pitch.C5, Duration.EIGHTH), Note(Pitch.E4, Duration.QUARTER), Note(
        Pitch.E4, Duration.EIGHTH), Note(Pitch.C4, Duration.HALF),

    Note(Pitch.E5, Duration.EIGHTH), Note(Pitch.C5, Duration.QUARTER), Note(Pitch.G4, Duration.EIGHTH), Note(
        Pitch.REST, Duration.QUARTER), Note(Pitch.GS4, Duration.QUARTER),  # repeats from 23
    Note(Pitch.A4, Duration.EIGHTH), Note(Pitch.F5, Duration.QUARTER), Note(
        Pitch.F5, Duration.EIGHTH), Note(Pitch.A4, Duration.HALF),
    Note(Pitch.D5, Duration.EIGHTH, True), Note(Pitch.A5, Duration.EIGHTH, True), Note(Pitch.A5, Duration.EIGHTH, True), Note(Pitch.A5,
                                                                                                                              Duration.EIGHTH, True), Note(Pitch.G5, Duration.EIGHTH, True), Note(Pitch.F5, Duration.EIGHTH, True),

    Note(Pitch.E5, Duration.EIGHTH), Note(Pitch.C5, Duration.QUARTER), Note(
        Pitch.A4, Duration.EIGHTH), Note(Pitch.G4, Duration.HALF),  # 26
    Note(Pitch.E5, Duration.EIGHTH), Note(Pitch.C5, Duration.QUARTER), Note(Pitch.G4,
                                                                            Duration.EIGHTH), Note(Pitch.REST, Duration.QUARTER), Note(Pitch.GS4, Duration.QUARTER),
    Note(Pitch.A4, Duration.EIGHTH), Note(Pitch.F5, Duration.QUARTER), Note(
        Pitch.F5, Duration.EIGHTH), Note(Pitch.A4, Duration.HALF),
    Note(Pitch.B4, Duration.EIGHTH), Note(Pitch.F5, Duration.QUARTER), Note(
        Pitch.F5, Duration.EIGHTH), Note(Pitch.F5, Duration.EIGHTH, True), Note(Pitch.E5, Duration.EIGHTH, True), Note(Pitch.D5, Duration.EIGHTH, True),
    Note(Pitch.C5, Duration.EIGHTH), Note(Pitch.E4, Duration.QUARTER), Note(
        Pitch.E4, Duration.EIGHTH), Note(Pitch.C4, Duration.HALF),
    Note(Pitch.C5, Duration.EIGHTH), Note(Pitch.C5, Duration.QUARTER), Note(Pitch.C5, Duration.EIGHTH), Note(Pitch.REST,
                                                                                                             Duration.EIGHTH), Note(Pitch.C5, Duration.EIGHTH), Note(Pitch.D5, Duration.EIGHTH), Note(Pitch.E5, Duration.EIGHTH),
    Note(Pitch.REST, Duration.WHOLE),

    Note(Pitch.C5, Duration.EIGHTH), Note(Pitch.C5, Duration.QUARTER), Note(Pitch.C5, Duration.EIGHTH), Note(
        Pitch.REST, Duration.EIGHTH), Note(Pitch.C5, Duration.EIGHTH), Note(Pitch.D5, Duration.QUARTER),  # 33
    Note(Pitch.E5, Duration.EIGHTH), Note(Pitch.C5, Duration.QUARTER), Note(
        Pitch.A4, Duration.EIGHTH), Note(Pitch.G4, Duration.HALF),
    Note(Pitch.E5, Duration.EIGHTH), Note(Pitch.E5, Duration.EIGHTH), Note(Pitch.REST, Duration.EIGHTH), Note(Pitch.E5,
                                                                                                              Duration.EIGHTH), Note(Pitch.REST, Duration.EIGHTH), Note(Pitch.C5, Duration.EIGHTH), Note(Pitch.E5, Duration.QUARTER),
    Note(Pitch.G5, Duration.QUARTER), Note(Pitch.REST, Duration.QUARTER), Note(
        Pitch.G4, Duration.QUARTER), Note(Pitch.REST, Duration.QUARTER),
    Note(Pitch.E5, Duration.EIGHTH), Note(Pitch.C5, Duration.QUARTER), Note(Pitch.G4,
                                                                            Duration.EIGHTH), Note(Pitch.REST, Duration.QUARTER), Note(Pitch.GS4, Duration.QUARTER),
    Note(Pitch.A4, Duration.EIGHTH), Note(Pitch.F5, Duration.QUARTER), Note(
        Pitch.F5, Duration.EIGHTH), Note(Pitch.A4, Duration.HALF),
    Note(Pitch.D5, Duration.EIGHTH, True), Note(Pitch.A5, Duration.EIGHTH, True), Note(Pitch.A5, Duration.EIGHTH, True), Note(Pitch.A5,
                                                                                                                              Duration.EIGHTH, True), Note(Pitch.G5, Duration.EIGHTH, True), Note(Pitch.F5, Duration.EIGHTH, True),

    Note(Pitch.E5, Duration.EIGHTH), Note(Pitch.C5, Duration.QUARTER), Note(
        Pitch.A4, Duration.EIGHTH), Note(Pitch.G4, Duration.HALF),  # 40
    Note(Pitch.E5, Duration.EIGHTH), Note(Pitch.C5, Duration.QUARTER), Note(Pitch.G4,
                                                                            Duration.EIGHTH), Note(Pitch.REST, Duration.QUARTER), Note(Pitch.GS4, Duration.QUARTER),
    Note(Pitch.A4, Duration.EIGHTH), Note(Pitch.F5, Duration.QUARTER), Note(
        Pitch.F5, Duration.EIGHTH), Note(Pitch.A4, Duration.HALF),
    Note(Pitch.B4, Duration.EIGHTH), Note(Pitch.F5, Duration.QUARTER), Note(
        Pitch.F5, Duration.EIGHTH), Note(Pitch.F5, Duration.EIGHTH, True), Note(Pitch.E5, Duration.EIGHTH, True), Note(Pitch.D5, Duration.EIGHTH, True),
    Note(Pitch.C5, Duration.EIGHTH), Note(Pitch.E4, Duration.QUARTER), Note(
        Pitch.E4, Duration.EIGHTH), Note(Pitch.C4, Duration.HALF),

    # game over sound
    Note(Pitch.C5, Duration.QUARTER, True), Note(
        Pitch.G4, Duration.QUARTER, True), Note(Pitch.E4, Duration.QUARTER),  # 45
    Note(Pitch.A4, Duration.EIGHTH, True), Note(Pitch.B4, Duration.EIGHTH, True), Note(Pitch.A4, Duration.EIGHTH, True), Note(Pitch.GS4,
                                                                                                                              Duration.EIGHTH, True), Note(Pitch.AS4, Duration.EIGHTH, True), Note(Pitch.GS4, Duration.EIGHTH, True),
    Note(Pitch.G4, Duration.EIGHTH), Note(
        Pitch.D4, Duration.EIGHTH), Note(Pitch.E4, Duration.HALF, True),
]

SONG = Song("Super Mario", WHOLE_NOTE, MELODY)
