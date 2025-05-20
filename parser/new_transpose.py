import ly.lex
from ly.document import Document, Cursor
from ly.pitch.transpose import Transposer, transpose

# 1) Read the file into a Document
with open("music.ly") as f:
    text = f.read()
doc = Document.fromLilypondString(text)

# 2) Pick your semitone transposer (C → Cis = +1)
from ly.pitch import Pitch
transposer = Transposer(Pitch("c"), Pitch("cis"))

# 3) Run the high‑level transpose on the whole doc
#    relative_first_pitch_absolute=True makes the first note respect its written octave 
transpose(
    doc,
    transposer,
    language="nederlands",
    relative_first_pitch_absolute=True
)

# 4) Dump back out, preserving the original \relative block
with open("output.ly", "w") as f:
    f.write(doc.toString())

