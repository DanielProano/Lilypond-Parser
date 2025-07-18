from ly.music import pitch

axis = pitch.pitch("d'")

original = pitch.putch("e'")

interval = pitch.diff(axis, original)

inverted = pitch.transpose(axis, -interval)

print(inverted)
