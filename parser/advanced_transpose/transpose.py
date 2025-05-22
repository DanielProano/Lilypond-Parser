from ly.document import Document, Cursor
import ly.lex
from ly.pitch import PitchIterator
from ly.pitch.transpose import Transposer, Simplifier
from ly.pitch import Pitch
from fractions import Fraction

with open("music.ly", "r") as file:
	content = file.read()

s = ly.lex.state("lilypond")
all_pitches = PitchIterator(s.tokens(content), language='nederlands')

from_pitch = Pitch(0, 0, 0)
to_pitch = Pitch(0, Fraction(1, 2), 0)
print(f"from {from_pitch} to_pitch {to_pitch}")
transposer_custom = Transposer(from_pitch, to_pitch)
simplify = Simplifier(scale=[0, 1, 2, 3, 4, 5, 6])

last_pitch = None
happened = False
with open("output.ly", "w") as file:
	for i in all_pitches.pitches():
		if not isinstance(i, Pitch):
			print(i)
			file.write(i)
			continue
		print(f"Original: {i}, {i.note}, {i.octave}, {i.alter}")
		transposer_custom.transpose(i)
		print(f"Transposer: {i}, {i.note}, {i.octave}, {i.alter}")
		simplify.transpose(i)
		print(f"Simplified: {i}, {i.note}, {i.octave}, {i.alter}")
		out_str = i.output('nederlands')
		file.write(f" {out_str}")
