import ly.lex
from ly.pitch import PitchIterator
from ly.pitch import Pitch

def extract_key_pitch(tokens):
	tokens = list(tokens)
	it = iter(tokens)
	for token in it:
		if str(token) == '\\key':
			while True:
				try:
					next_token = next(it)
					if next_token and str(next_token).strip():
						return next_token
				except StopIteration:
					return None
	return None

def main():
	with open("twinkle.ly", "r") as file:
		content = file.read()

	s = ly.lex.state("lilypond")
	tokens = list(s.tokens(content))
	all_pitches = PitchIterator(s.tokens(content), language='nederlands')
	
	axis = Pitch(1, 0, 1)
	key_pitch = extract_key_pitch(tokens)
	if key_pitch:
		axis = key_pitch
		print(axis)

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
				file.write(i.output('nederlands'))
if __name__ == "__main__":
        main()
