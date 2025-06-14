from ly.document import Document, Cursor

import ly.lex
from ly.pitch import PitchIterator
from ly.pitch.transpose import Transposer, Simplifier
from ly.pitch import Pitch
from fractions import Fraction
import math

NOTE_TO_SEMI = [0, 2, 4, 5, 7, 9, 11]


#Takes a note to its corresponding semitone
def pitch_to_semi(note):
	return NOTE_TO_SEMI[note.note] + note.alter + 12 * (note.octave + 4)

#Takes a semitone back to its pitch
def semi_to_pitch(semitone):
	octave = math.floor(semitone / 12)
	semi_in_octave = semitone - 12 * octave

	best_note = 0
	min_distance = float('inf')
	for i in range(7):
		potential = abs(NOTE_TO_SEMI[i] - semi_in_octave)
		if potential < min_distance:
			min_distance = potential
			best_note = i
	alter = semi_in_octave - NOTE_TO_SEMI[best_note]
	alter = round(alter * 2) / 2
	return Pitch(note=best_note, alter=alter, octave=octave - 4)

#Inverts a note around an axis
def invert(note, axis):
	note_semi = pitch_to_semi(note)
	axis_semi = pitch_to_semi(axis) 
	inverted_semi = 2 * axis_semi - note_semi
	return semi_to_pitch(inverted_semi)

def adjust_relative_octave(prev_pitch, curr_pitch):
    prev_semi = pitch_to_semi(prev_pitch)

    options = []
    for delta in [-2, -1, 0, 1, 2]:
        test_pitch = Pitch(curr_pitch.note, curr_pitch.alter, curr_pitch.octave + delta)
        semi = pitch_to_semi(test_pitch)
        diff = abs(semi - prev_semi)
        options.append((diff, test_pitch))

    return min(options, key=lambda x: x[0])[1]


def main():
	with open("music.ly", "r") as file:
		content = file.read()

	s = ly.lex.state("lilypond")
	all_pitches = PitchIterator(s.tokens(content), language='nederlands')

	axis = Pitch(0, 0, 1)
	note_in_the_key = False
	simplifier = Simplifier()
	prev_pitch = None

	with open("output.ly", "w") as file:
		for i in all_pitches.pitches():
			if not isinstance(i, Pitch):
				if i == "bass":
					file.write("treble")
					continue
				elif i == "treble":
					file.write("bass")
					continue
				file.write(i)
				continue
	
			if note_in_the_key == False:
				inverted = invert(i, axis)
				file.write(f"{inverted.output('nederlands')} ")
				note_in_the_key = True
				continue

			print(i)
			inv = invert(i, axis)
			print(inv)
			inv = simplifier.transpose(inv) or inv
			print(inv)
			if prev_pitch:
				inv = adjust_relative_octave(prev_pitch, inv)
				print(inv)
			prev_pitch = inv
			print(" ")
			file.write(f" {inv.output('nederlands')}")
			
if __name__ == "__main__":
	main()
