from ly.document import Document, Cursor

import ly.lex
from ly.music import items
from ly.pitch import PitchIterator
from ly.pitch.transpose import Transposer, Simplifier
from ly.pitch import Pitch
from fractions import Fraction
import math


# These numbers represent the steps from C in a 31 TET system
SEMI_TO_NOTE_31 = [0, 5, 9, 13, 18, 22, 27]


# Pitch to 31 TET MIDI representation
def pitch_to_semi_31(note):
	return SEMI_TO_NOTE_31[note.note] + note.alter + note.octave * 31


# MIDI representation to a Pitch object
def semi_to_pitch_31(semi):
	octave = semi // 31
	print(f"Octave: {octave}")
	semi_in_octave = semi % 31

	# Starts at the largest range possible and goes
	# until the note closest to the Pitch is found

	for i in reversed(range(7)):
		base = SEMI_TO_NOTE_31[i]
		if base <= semi_in_octave:	
			note = i
			alter = semi_in_octave - base
			print(f"Note: {note}")
			print(f"Alter: {alter}")
			return Pitch(note, alter, octave)


#Inverts a note around an axis
def invert(note, axis):
	print(" ")
	note_semi = pitch_to_semi_31(note)
	print(f"Semi: {note_semi}")
	axis_semi = pitch_to_semi_31(axis) 
	print(f"Axis semitone: {axis_semi}")
	inverted_semi = 2 * axis_semi - note_semi
	print(f"Inverted semitone: {inverted_semi}")
	return semi_to_pitch_31(inverted_semi)


def main():
	with open("music.ly", "r") as file:
		content = file.read()

	s = ly.lex.state("lilypond")
	all_pitches = PitchIterator(s.tokens(content), language='nederlands')

	axis = Pitch(0, 0, 1)

	# A list for testing purposes, composing of all the basic pitches
	# necessary.
	pitch_list = [Pitch(-3, -1, 0), Pitch(-2, -1, 0), Pitch(-1, -1, 0), 
Pitch(0, -1, 0), Pitch(1, -1, 0), Pitch(2, -1, 0), Pitch(3, -1, 0),
Pitch(-3, 0, 0), Pitch(-2, 0, 0), Pitch(-1, 0, 0), Pitch(0, 0, 0),
Pitch(1, 0, 0), Pitch(2, 0, 0), Pitch(3, 0, 0), Pitch(-3, 1, 0),
Pitch(-2, 1, 0), Pitch(-1, 1, 0), Pitch(0, 1, 0), Pitch(1, 1, 0),
Pitch(2, 1, 0), Pitch(3, 1, 0)]

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
			inv = invert(i, axis)
			file.write(f" {inv.output('nederlands')}")
			
if __name__ == "__main__":
	main()
