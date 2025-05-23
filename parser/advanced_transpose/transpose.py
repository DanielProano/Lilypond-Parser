from ly.document import Document, Cursor
import ly.lex
from ly.pitch import PitchIterator
from ly.pitch.transpose import Transposer, Simplifier
from ly.pitch import Pitch
from fractions import Fraction

"""
class Custom_Simplifier(Transposer):
	def __init__(self, scale=None):
		if scale is not None:
			self.scale = scale
	def transpose(self, pitch):
		if pitch.alter == 1:
			doct, note = divmod(pitch.note + 1, 7)
			pitch.alter -= doct * 6 + self.scale[note] - self.scale[pitch.note]
			pitch.octave += doct
			pitch.note = note
		elif pitch.alter == -1:
			doct, note = divmod(pitch.note - 1, 7)
			pitch.alter += doct * -6 + self.scale[pitch.note] - self.scale[note]
			pitch.octave += doct
			pitch.note = note
		if pitch.alter == Fraction(1, 2):
			doct, note = divmod(pitch.note + 1, 7)
			alter = doct * 6 + self.scale[note] - self.scale[pitch.note]
			print(alter)
			if alter == Fraction(1, 2):
				pitch.alter = 0
				pitch.octave += doct
				pitch.note = note
		elif pitch.alter == Fraction(-1, 2):
			doct, note = divmod(pitch.note - 1, 7)
			alter = doct * -6 + self.scale[pitch.note] - self.scale[note]
			if alter == Fraction(1, 2):
				pitch.alter = 0
				pitch.octave += doct
				pitch.note = note
"""

def main():
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
			print(f"{i} {i.note} {i.octave} {i.alter}")
			transposer_custom.transpose(i)
			print(f"{i} {i.note} {i.octave} {i.alter}")
			#simplify.transpose(i)
			out_str = i.output('nederlands')
			file.write(f" {out_str}")

if __name__ == "__main__":
	main()
