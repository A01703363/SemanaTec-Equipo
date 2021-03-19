# Offset + Duration
from music21 import note, stream, meter


notes  = ['C5', 'F', 'G', 'A', 'Bb', 'C5', 'F', 'F', 'D5', 'Bb', 
         'C5', 'D5', 'E5', 'F5', 'F', 'F']
# Posiciones de las notas que duran 1/4
cuartos = [0, 5, 6, 7, 8, 13, 14, 15] 
st = stream.Stream()
for i in range(len(notes)):
  new_note = note.Note(notes[i])
  if(i not in cuartos):
    new_note.duration.quarterLength = 0.5  
  st.append(new_note)
  st.insert(0, meter.TimeSignature('3/4'))
st.write('midi', fp="cancion14.mid")
