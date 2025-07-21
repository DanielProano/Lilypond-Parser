import ly.lex
from ly.pitch import PitchIterator
from ly.pitch import Pitch

def extract_key_pitch(tokens):
	for token in tokens.pitches():
		if str(token) == '\\key':
				try:
					while True:
						next_token = next(tokens.pitches())
						if next_token and str(next_token).strip():
							return next_token
				except StopIteration:
					return None
	return None

def main():
	with open("d_scale.ly", "r") as file:
		content = file.read()

	s = ly.lex.state("lilypond")
	all_pitches = PitchIterator(s.tokens(content), language='nederlands')
	list_of_pitches = PitchIterator(s.tokens(content), language='nederlands')
	
	axis = Pitch(1, 0, 1)
	key_pitch = extract_key_pitch(list_of_pitches)
	if key_pitch:
		print(key_pitch)
		axis = key_pitch

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
				inverted_note = 2 * axis.note - i.note % 7

				inverted_alter = -i.alter

				if i.octave != 0:
					inverted_octave = 2 * axis.octave - i.octave
				else:
					inverted_octave = 0
	
				out = Pitch(inverted_note, inverted_alter, inverted_octave)
				file.write(out.output('nederlands') + ' ')
			else:
				file.write(i.output('nederlands') + ' ')
if __name__ == "__main__":
        main()
