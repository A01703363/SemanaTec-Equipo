# Offset + Duration

notes  = [ 'C', 'F3', 'G3', 'A3', 'B3', 
          'C', 'F3', 'F3', 
          'D', 'B3', 'C', 'D', 'E', 
          'F', 'F3', 'F3',
          'B3', 'C', 'B3', 'A3', 'G3', 
          'A3','B3', 'A3', 'G3', 'F3', 
          'E3', 'F3', 'G3', 'A3', 'F3',
          'G3']

st = stream.Stream()

for n in notes:
  new_note = note.Note(n)
  st.append(new_note)


st.write('midi', fp="cancion2.mid")