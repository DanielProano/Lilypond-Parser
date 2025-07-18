 cat parser.py
from ly.document import Document, Cursor
import ly.lex
from ly.pitch import PitchIterator
from ly.pitch.transpose import Transposer, Simplifier
from ly.pitch import Pitch
from fractions import Fraction
import math


def diatonic_invert(pitch, axis_note, scale):
    # scale = list of 7 pitch class numbers (e.g. C major: [0, 2, 4, 5, 7, 9, 11])
    note_index = pitch.note  # from 0 to 6 (C to B)
    alter = pitch.alter

    # Get index of pitch in scale
    try:
        scale_index = scale.index(NOTE_TO_SEMI[note_index])
    except ValueError:
        raise Exception("Note not in scale")

    # Invert index around axis
    axis_index = scale.index(NOTE_TO_SEMI[axis_note])
    inverted_index = (2 * axis_index - scale_index) % 7

    # Get new note and calculate base semitone
    inverted_note_pc = scale[inverted_index]
    inverted_note = NOTE_TO_SEMI.index(inverted_note_pc)

    # Reapply alter to stay consistent
    new_pitch = Pitch(inverted_note, alter, pitch.octave)
    return new_pitch

def main():
        with open("d_scale.ly", "r") as file:
                content = file.read()

        s = ly.lex.state("lilypond")
        all_pitches = PitchIterator(s.tokens(content), language='nederlands')

        with open("output.ly", "w") as file:
                depth = 0
                for i in all_pitches.pitches():
                        # Print anything that isnt a pitch
                        if not isinstance(i, Pitch):
                                token_str = str(i)

                                if token_str == '{':
                                        depth += 1
                                        file.write('{')
                                        continue
                                elif token_str == '}':
                                        depth -= 1
                                        file.write('}')
                                        continue

                                if token_str == "bass":
                                        file.write("treble")
                                        continue
                                elif token_str == "treble":
                                        file.write("bass")
                                        continue

                                file.write(f"{token_str}")
                                continue


                        if depth > 0:
				scale = ['c', 'd', 'e', 'f', 'g', 'a', 'b']
				axis = scale.index('d')
                        else:
                                file.write(i.output('nederlands' ))
if __name__ == "__main__":
        main()
