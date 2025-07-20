from ly.document import Document, Cursor
import ly.lex
from ly.pitch import PitchIterator
from ly.pitch.transpose import Transposer, Simplifier
from ly.pitch import Pitch
from fractions import Fraction
import math


def main():
	with open("twinkle.ly", "r") as file:
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
				inverted_note = 2 * 1 - i.note % 7
				
				inverted_alter = -1 * i.alter

				inverted_octave = -1 * i.octave
				
				inverted_note = Pitch(inverted_note, inverted_alter, inverted_octave)
				file.write(inverted_note.output('nederlands') + ' ')
			else:
				file.write(i.output('nederlands'))
if __name__ == "__main__":
        main()
