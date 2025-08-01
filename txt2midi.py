from mido import Message, MidiFile, MidiTrack
import string

def char_to_midi_note(char):
    # Map printable characters to MIDI note range (21 to 108 = piano range)
    ascii_val = ord(char)
    return 21 + (ascii_val % (108 - 21))

def text_to_midi(text, filename="output.mid"):
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    time = 240  # delay between notes

    for char in text:
        if char in string.printable:
            note = char_to_midi_note(char)
            track.append(Message('note_on', note=note, velocity=64, time=0))
            track.append(Message('note_off', note=note, velocity=64, time=time))

    mid.save(filename)
    print(f"MIDI file saved as '{filename}'")

# Example usage
input_text = "Hello123!"
text_to_midi(input_text)
