from ly.document import Document
from ly.music.items import Transpose, Note
import ly.lex

with open("c_scale.ly", "r") as file:
    content = file.read()

print(f"Content: {content}")

s = ly.lex.state("lilypond")

with open("result.ly", "w") as file:
	for t in s.tokens(content):
		file.write(t)

