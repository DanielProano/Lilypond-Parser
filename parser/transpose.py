from ly.document import Document, Cursor
import ly.lex
from ly.pitch import PitchIterator
from ly.pitch.transpose import ModalTransposer
from ly.pitch import Pitch

with open("music.ly", "r") as file:
	content = file.read()

s = ly.lex.state("lilypond")
pitch_tr = ModalTransposer(1, 0)
all_pitches = PitchIterator(s.tokens(content), language='nederlands')

with open("output.ly", "w") as file:
	for i in all_pitches.pitches():
		if isinstance(i, Pitch):
			pitch_tr.transpose(i)
			i = i.output('nederlands')
		file.write(i)
	
