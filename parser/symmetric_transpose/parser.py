from ly.document import Document, Cursor
import ly.lex
from ly.pitch import PitchIterator
from ly.pitch.transpose import Transposer, Simplifier
from ly.pitch import Pitch
from fractions import Fraction

d_note = Pitch(1, 0, 0)
NOTE_TO_SEMI = [0, 2, 4, 5, 7, 9, 11]


#Takes a note to its corresponding semitone
def pitch_to_semi(note):
	return NOTE_TO_SEMI[note.note] + note.alter + 12 * (note.octave + 1)

#Takes a semitone back to its pitch
def semi_to_pitch(semitone):
	octave, semi_in_octave = divmod(semitone, 12)
	best_note = 0
	min_distance = float('inf')
	for i in range(7):
		potential = abs(NOTE_TO_SEMI[i] - semi_in_octave)
		if potential < min_distance:
			min_distance = potential
			best_note = i
	alter = semi_in_octave - NOTE_TO_SEMI[best_note]
	alter = round(alter * 2) / 2
	return Pitch(note=best_note, alter=alter, octave=octave - 1)

#Inverts a note around an axis
def invert(note, axis):
	note_semi = pitch_to_semi(note)
	axis_semi = pitch_to_semi(axis) 
	inverted_note = 2 * axis_semi - note_semi
	return semi_to_pitch(inverted_note)

def main():
	new_note = invert(Pitch(0,0,0), d_note)
	print(new_note)

	with open("d_scale.ly", "r") as file:
		content = file.read()

	s = ly.lex.state("lilypond")
	all_pitches = PitchIterator(s.tokens(content), language='nederlands')
	axis = Pitch(1, 0, 0)

	with open("output.ly", "w") as file:
		for i in all_pitches.pitches():
			if not isinstance(i, Pitch):
				file.write(i)
				continue
			inverted_note = invert(i, axis)
			out_str = inverted_note.output('nederlands')
			file.write(f" {out_str}")

if __name__ == "__main__":
	main()
