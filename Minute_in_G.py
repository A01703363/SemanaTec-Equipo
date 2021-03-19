# Offset + Duration
from music21 import note, stream, meter


notes  = ['C5', 'F', 'G', 'A', 'Bb', 
        'C5', 'F', 'F', 
        'D5', 'Bb', 'C5', 'D5', 'E5', 
        'F5', 'F', 'F',
        'Bb', 'C5', 'Bb', 'A', 'G',
        'A', 'Bb', 'A', 'G', 'F',
        'E', 'F', 'G', 'A', 'F',
        'G',
        'C5', 'F', 'G', 'A', 'Bb', 
        'C5', 'F', 'F', 
        'D5', 'Bb', 'C5', 'D5', 'E5', 
        'F5', 'F', 'F',
        'Bb', 'C5', 'Bb', 'A', 'G',
        'A', 'Bb', 'A', 'G', 'F',
        'E', 'F', 'G', 'A', 'F',
        'F',
        'A5', 'F5', 'G5', 'A5', 'F5',
        'G5', 'C5', 'D5', 'E5', 'C5',
        'F5', 'D5', 'E5', 'F5', 'C5',
        'Bb', 'A', 'Bb', 'G', 
        'G', 'A', 'Bb', 'C5', 'D5','E5',
        'F5', 'E5', 'D5',
        'E5', 'G', 'Bb', 
        'C5']


# Posiciones de las notas que duran 1/4
cuartos = [0, 5, 6, 7, 8, 13, 14, 15, 16, 21, 
          26, 31, 32, 37, 38, 39, 40, 45, 46, 
          47, 48, 53, 58, 63, 64, 69, 74, 78,
          81, 90, 93, 94] 
st = stream.Stream()
for i in range(len(notes)):
  new_note = note.Note(notes[i])
  if(i not in cuartos):
    new_note.duration.quarterLength = 0.5  
  st.append(new_note)
  st.insert(0, meter.TimeSignature('3/4'))
st.write('midi', fp="cancion17.mid")
