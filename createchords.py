import random
from midiutil import MIDIFile

# Function to create a MIDI file with a chord progression
def create_midi_chord_progression(key, filename):
    midi = MIDIFile(1)
    track = 0
    time = 0
    midi.addTrackName(track, time, "Chord Progression in " + key)
    midi.addTempo(track, time, 120)

    # Add the key signature
    key_signature = get_key_signature(key)
    midi.addKeySignature(track, time, key_signature['sharps_flats'], key_signature['mode'])

    # Define the intervals for different types of chords
    chord_types = {
        "major": [0, 4, 7],
        "minor": [0, 3, 7],
        "diminished": [0, 3, 6],
        "augmented": [0, 4, 8],
        "major7": [0, 4, 7, 11],
        "minor7": [0, 3, 7, 10],
        "dominant7": [0, 4, 7, 10],
    }

    # Define the chords available in each key
    chords_in_key = {
        "C": [60, 62, 64, 65, 67, 69, 71],  # C, Dm, Em, F, G, Am, Bdim
        "G": [67, 69, 71, 72, 74, 76, 78],  # G, Am, Bm, C, D, Em, F#dim
        "D": [62, 64, 66, 67, 69, 71, 73],  # D, Em, F#m, G, A, Bm, C#dim
        "A": [69, 71, 73, 74, 76, 78, 80],  # A, Bm, C#m, D, E, F#m, G#dim
        "E": [64, 66, 68, 69, 71, 73, 75],  # E, F#m, G#m, A, B, C#m, D#dim
        "B": [71, 73, 75, 76, 78, 80, 82],  # B, C#m, D#m, E, F#, G#m, A#dim
        "F#": [66, 68, 70, 71, 73, 75, 77], # F#, G#m, A#m, B, C#, D#m, E#dim
        "C#": [61, 63, 65, 66, 68, 70, 72], # C#, D#m, E#m, F#, G#, A#m, B#dim
        "F": [65, 67, 69, 70, 72, 74, 76],  # F, Gm, Am, Bb, C, Dm, Edim
        "Bb": [70, 72, 74, 75, 77, 79, 81], # Bb, Cm, Dm, Eb, F, Gm, Adim
        "Eb": [63, 65, 67, 68, 70, 72, 74], # Eb, Fm, Gm, Ab, Bb, Cm, Ddim
        "Ab": [68, 70, 72, 73, 75, 77, 79], # Ab, Bbm, Cm, Db, Eb, Fm, Gdim
        "Db": [61, 63, 65, 66, 68, 70, 72], # Db, Ebm, Fm, Gb, Ab, Bbm, Cdim
        "Gb": [66, 68, 70, 71, 73, 75, 77], # Gb, Abm, Bbm, Cb, Db, Ebm, Fdim
        "Cb": [59, 61, 63, 64, 66, 68, 70], # Cb, Dbm, Ebm, Fb, Gb, Abm, Bdim
        "Am": [69, 71, 72, 74, 76, 77, 79], # Am, Bdim, C, Dm, Em, F, G
        "Em": [64, 66, 67, 69, 71, 72, 74], # Em, F#dim, G, Am, Bm, C, D
        "Bm": [71, 73, 74, 76, 78, 79, 81], # Bm, C#dim, D, Em, F#m, G, A
        "F#m": [66, 68, 69, 71, 73, 74, 76], # F#m, G#dim, A, Bm, C#m, D, E
        "C#m": [61, 63, 64, 66, 68, 69, 71], # C#m, D#dim, E, F#m, G#m, A, B
        "G#m": [68, 70, 71, 73, 75, 76, 78], # G#m, A#dim, B, C#m, D#m, E, F#
        "D#m": [63, 65, 66, 68, 70, 71, 73], # D#m, E#dim, F#, G#m, A#m, B, C#
        "A#m": [70, 72, 73, 75, 77, 78, 80], # A#m, B#dim, C#, D#m, E#m, F#, G#
    }

    # Get the root notes for the specified key
    roots = chords_in_key[key]
    
    # Generate a random chord progression
    progression = [random.choice(roots) for _ in range(8)]
    
    # Define possible chord types
    possible_chord_types = ["major", "minor", "diminished", "augmented", "major7", "minor7", "dominant7"]
    
    # Add chords to the MIDI file
    for root in progression:
        chord_type = random.choice(possible_chord_types)
        intervals = chord_types[chord_type]
        add_chord(midi, track, time, root, intervals)
        time += 1
    
    # Save the MIDI file
    with open(filename, "wb") as output_file:
        midi.writeFile(output_file)

# Function to add a chord to the MIDI file
def add_chord(midi, track, time, root, intervals, duration=1):
    for interval in intervals:
        midi.addNote(track, 0, root + interval, time, duration, 64)

# Function to get key signature parameters
def get_key_signature(key):
    key_signatures = {
        "C": {"sharps_flats": 0, "mode": 0},
        "G": {"sharps_flats": 1, "mode": 0},
        "D": {"sharps_flats": 2, "mode": 0},
        "A": {"sharps_flats": 3, "mode": 0},
        "E": {"sharps_flats": 4, "mode": 0},
        "B": {"sharps_flats": 5, "mode": 0},
        "F#": {"sharps_flats": 6, "mode": 0},
        "C#": {"sharps_flats": 7, "mode": 0},
        "F": {"sharps_flats": -1, "mode": 0},
        "Bb": {"sharps_flats": -2, "mode": 0},
        "Eb": {"sharps_flats": -3, "mode": 0},
        "Ab": {"sharps_flats": -4, "mode": 0},
        "Db": {"sharps_flats": -5, "mode": 0},
        "Gb": {"sharps_flats": -6, "mode": 0},
        "Cb": {"sharps_flats": -7, "mode": 0},
        "Am": {"sharps_flats": 0, "mode": 1},
        "Em": {"sharps_flats": 1, "mode": 1},
        "Bm": {"sharps_flats": 2, "mode": 1},
        "F#m": {"sharps_flats": 3, "mode": 1},
        "C#m": {"sharps_flats": 4, "mode": 1},
        "G#m": {"sharps_flats": 5, "mode": 1},
        "D#m": {"sharps_flats": 6, "mode": 1},
        "A#m": {"sharps_flats": 7, "mode": 1},
    }
    return key_signatures[key]

# Example usage
key_signature = "A"  # You can change this to any key you want
filename = f"{key_signature}_random_chord_progression.mid"
create_midi_chord_progression(key_signature, filename)

print(f"MIDI file saved as '{filename}'")