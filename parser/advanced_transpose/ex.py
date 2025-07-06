from ly.pitch import PitchIterator, Pitch
from fractions import Fraction
import ly.lex

def invert_pitch(pitch, pivot):
    """Reflect the pitch around the pivot pitch."""
    semitones_original = pitch.to_semitones()
    semitones_pivot = pivot.semitones
    inverted_semitones = 2 * semitones_pivot - semitones_original
    return Pitch.from_semitones(inverted_semitones)

def main():
    with open("music.ly", "r") as file:
        content = file.read()

    s = ly.lex.state("lilypond")
    all_pitches = PitchIterator(s.tokens(content), language='nederlands')

    pivot = Pitch(0, 0, 0)  # Middle C as inversion axis

    with open("output.ly", "w") as file:
        for i in all_pitches.pitches():
            if not isinstance(i, Pitch):
                print(i)
                file.write(i)
                continue

            print(f"Original: {i} {i.note} {i.octave} {i.alter}")
            inverted = invert_pitch(i, pivot)
            print(f"Inverted: {inverted} {inverted.note} {inverted.octave} {inverted.alter}")
            out_str = inverted.output('nederlands')
            file.write(f" {out_str}")

if __name__ == "__main__":
    main()

