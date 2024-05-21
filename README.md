## About
The Record Label Hub presents ChordGenerator: a free and opensource chords engine that prompts the user for Key Signature then creates a unique and random chord progression in that Key, empowered by the RL Ai technology stack. The Chord Generator asks user to name the output file and outputs a .mid aka MIDI file for the chords it generates. Make your next hit with The Record Label's Chord Generator Now!

Once You Have VS Code or IDE with Python installed:
## Summary of Commands

# Open the terminal in VS Code and run:
```
python -m venv .venv
```
Click on Yes use folder as workspace or select the .venv from the search bar at the top of VS Code or IDE.

Now that you've installed .venv in your directory let's go ahead and activate it:
```
.\.venv\Scripts\activate
```
## OPTIONAL SETUP FOR .ENV
        IF YOU WANT TO USE A .ENV FOR ANY REASON:
        Now we need to set your ca-bundle.crt location in the environment using the command:
        ```
        $env:REQUESTS_CA_BUNDLE="C:\Users\Replace\With\Actual\ca-bundle.crt"
        ```

        Ok now we can fully install the python_dotenv inside of our .venv environment.
        ```
        pip --cert 'C:\Users\Ryda\Documents\2023 WIN PROGRMS\wordpress\wp-includes\certificates\ca-bundle.crt' install python-dotenv
        ```

Now that you've initialized your Python environment you're ready to start installing your required packages:

```
pip install midiutil
```

# After pasting the script into your .py file, run:
```
python createchords.py
```

Your new midi file is in the directory! Happy jamming!

This service is provided to you for FREE by TheRecordLabel.ai Community.

IF you Don't have VS Code or IDE and Python:
## Step 1: Install Python
Make sure Python is installed on your system. You can download it from python.org.

## Step 2: Install VS Code
Download and install Visual Studio Code from code.visualstudio.com.

## Step 3: Set Up Your Python Environment in VS Code
Open VS Code.
Install the Python extension for VS Code:
Go to the Extensions view by clicking the square icon in the sidebar or pressing Ctrl+Shift+X.
Search for "Python" and install the extension by Microsoft.

## Step 4: Create a New Python File
Create a new file in VS Code and save it with a .py extension, for example, generate_midi_chord_progression.py.

## Step 5: Install Required Libraries
Open a terminal in VS Code:

You can open the terminal by selecting Terminal > New Terminal from the top menu or by pressing Ctrl+` (backtick).
Install the midiutil library:

pip install midiutil

## Step 6: Copy and Paste the Script
Copy the provided script into your new Python file createchords.py

## Run the Script:

Save the provided script as generate_midi_chord_progression.py.
Run the script in your terminal or command prompt:

```
python createchords.py
```

## Specify the Key Signature:

Modify the key_signature variable to your desired key before running the script.
This script will include a key signature meta event in the MIDI file, ensuring that the key used to generate the chords is noted in the file.

You can specify the key signature in the following format:

Major keys: Use the uppercase note name (e.g., "C", "G", "D", "A", "E", "B", "F#", "C#", "F", "Bb", "Eb", "Ab", "Db", "Gb", "Cb").
Minor keys: Use the note name followed by a lowercase "m" (e.g., "Am", "Em", "Bm", "F#m", "C#m", "G#m", "D#m", "A#m").
Here are some examples:

For C major, use "C".
For A minor, use "Am".
For G major, use "G".
For E minor, use "Em".
The script will interpret these key signatures and apply the appropriate key signature meta event in the MIDI file.

Example Usage
To generate a random chord progression in A minor:

key_signature = "Am"  # For A minor
filename = f"{key_signature}_random_chord_progression.mid"
create_midi_chord_progression(key_signature, filename)

print(f"MIDI file saved as '{filename}'")
To generate a random chord progression in D major:

python
Copy code
key_signature = "D"  # For D major
filename = f"{key_signature}_random_chord_progression.mid"
create_midi_chord_progression(key_signature, filename)

print(f"MIDI file saved as '{filename}'")
Modify the key_signature variable according to the key you want, and the script will handle the rest.


## Original Code:

```
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
```

Your new midi file is in the directory! Happy jamming!

This service is provided to you for FREE by TheRecordLabel.ai Community.
