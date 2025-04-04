# Este programa va a hacer uso de listas anidadas para devolver una lista con la catidad de ATCG en cada secuencia dada por el usuario.

sequences = input('Introduzca una secuencia de DNA que se encuentre separada por comas: ').split(',') 

counter = [f'A: {sequence.count("A")}, T: {sequence.count("T")}, C: {sequence.count("C")}, G: {sequence.count("G")}' for sequence in sequences] #por cado nucleótido vamos a contar su frecuencia de aparición y count nos va a ayudar a contar la cantidad de nucleótidos que hay en cada secuencia
print (f'La frecuencia de cada nucleótido en la secuencia es: {counter}') 