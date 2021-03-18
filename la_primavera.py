# Offset + Duration
from music21 import note, stream, tempo
notes = ['G', 'E','E', 'E','D', 'C', 'G', 'G', 'F', 'E','E', 'E','D','C','G']

st = stream.Stream()

for n in notes:
  new_note = note.Note(n)
  new_note.duration.quarterLength = 0.5
  st.append(new_note)

st.insert(0,tempo.MetronomeMark(number = 96))

st.write('midi', fp = 'la_primavera_vivaldi.mid')