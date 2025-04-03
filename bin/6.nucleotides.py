# Este programa extrae los primeros tres nucleótidos de una secuencia de ADN dada por el usuario.

sequences = (input('Introduzca una secuencia de DNA que se encuentre separada por comas: ')).split(',') #generamos una lista de secuencias separada por comas

start_codons= [sequence.strip()[:3] for sequence in sequences] 
print (f'Los primeros tres nucleótidos son: {start_codons}')