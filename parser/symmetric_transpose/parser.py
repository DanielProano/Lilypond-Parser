from ly.document import Document, Cursor
import ly.lex
from ly.pitch import PitchIterator
from ly.pitch.transpose import Transposer, Simplifier
from ly.pitch import Pitch
from fractions import Fraction
import math


# These numbers represent the distance in semitones from C
NOTE_TO_SEMI = [0, 2, 4, 5, 7, 9, 11]


# Takes a pitch and converts it to an MIDI number
def pitch_to_semi(note):
	return NOTE_TO_SEMI[note.note] + note.alter + 12 * (note.octave + 4)


# Takes a MIDI system back to a Pitch object for python-ly
def semi_to_pitch(semitone):
	octave = math.floor(semitone / 12)
	semi_in_octave = semitone - 12 * octave

	best_note = 0
	min_distance = float('inf')
	
	# Test every note and see which is the closest to the
	# position of the pitch

	for i in range(7):
		potential = abs(NOTE_TO_SEMI[i] - semi_in_octave)
		if potential < min_distance:
			min_distance = potential
			best_note = i
	alter = semi_in_octave - NOTE_TO_SEMI[best_note]
	alter = round(alter * 2) / 2
	return Pitch(note=best_note, alter=alter, octave=octave - 4)


# Inverts the MIDI protocol around an axis
def invert(note, axis):
	note_semi = pitch_to_semi(note) # Now we have an MIDI like 65
	axis_semi = pitch_to_semi(axis) # We will always use middle C: 60
	inverted_note = 2 * axis_semi - note_semi 
	return semi_to_pitch(inverted_note)


# Adjust the current pitch to better reflect that of
# previous notes.
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
	with open("d_scale.ly", "r") as file:
		content = file.read()

	s = ly.lex.state("lilypond")
	all_pitches = PitchIterator(s.tokens(content), language='nederlands')

	axis = Pitch(1, 0, 1) # Axis of Inversion
	prev_pitch = None
	note_in_the_key = False

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
				# This will invert a note 
				note = i.output('nederlands')
				if "'" in note or "," in note:
					inverted_note = invert(i, axis)
					out_str = inverted_note.output('nederlands')
					prev_pitch = inverted_note
					file.write(f"{out_str} ")
					continue
				print(i)

				'''
				Invert a regular note but flattens the octave,
				allowing Lilypond to handle the contextualization
				'''

				inverted_note = invert(i, axis)
				print(inverted_note)
				adjusted = adjust_relative_octave(prev_pitch, inverted_note) if prev_pitch else inverted_note
				print(adjusted)
				adjusted.octave = 0
				prev_pitch = adjusted
			
				out_str = adjusted.output('nederlands')
				file.write(f"{out_str} ")
			else:
				file.write(i.output('nederlands' ))
if __name__ == "__main__":
	main()
