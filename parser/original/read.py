from ly.document import Document
import ly.lex


with open("music.ly", "r") as file:
    content = file.read()

s = ly.lex.state("lilypond")
#with open("each_token.ly", "w") as file:
	#for h in s.tokens(content):
		#file.write(f"{h}, {h.__class__.__name__}\n")

with open("result.ly", "w") as file:
	for t in s.tokens(content):
		file.write(str(t))

