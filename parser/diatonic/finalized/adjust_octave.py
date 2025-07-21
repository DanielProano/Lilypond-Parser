import ly.lex
from ly.pitch import PitchIterator
from ly.pitch import Pitch

with open("output.ly", "r") as file:
	content = file.read()

s = ly.lex.state("lilypond")
all_pitches = PitchIterator(s.tokens(content), language='nederlands')

with open("output.ly", "w") as file:
	depth = 0
	for i in all_pitches.pitches():
		token_str = str(i)

		if token_str == '{':
			depth += 1
			file.write('{')
			continue
		elif token_str == '}':
			depth -= 1
			file.write('}')
			continue
	

		if depth > 0 and isinstance(i, Pitch):
			out = Pitch(i.note, i.alter, -i.octave)
			file.write(out.output('nederlands') + ' ')
		else:
			if isinstance(i, Pitch):
				file.write(i.output('nederlands') + ' ')
			else:
				file.write(str(i))
