from ly.document import Document, Cursor
import ly.lex
from ly.pitch import PitchIterator
from ly.pitch.transpose import Transposer
from ly.pitch import Pitch

with open("music.ly", "r") as file:
	content = file.read()

s = ly.lex.state("lilypond")
all_pitches = PitchIterator(s.tokens(content), language='nederlands')

from_pitch = Pitch(0, 0, 1)
to_pitch = Pitch(1, 0, 1)
transposer_custom = Transposer(from_pitch, to_pitch)

last_pitch = None
with open("output.ly", "w") as file:
	version, rest_of_file = content.split('\n', 1)
	file.write(version + "\n\n")
	file.write(r"absolute {" + "\n")
	for i in all_pitches.pitches():
		if isinstance(i, Pitch):
			transposer_custom.transpose(i)
			
			if last_pitch is not None:
				i.makeAbsolute(last_pitch)

			last_pitch = i.copy()
			i = i.output('nederlands')
			file.write(f" {i}")
			continue
		else:
			file.write(i)
	file.write("\n}")
	
