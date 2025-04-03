#Este programa va a hacer uso de comprensión de listas para invertir una secuencia de DNA dada por el usuario.

sequence = input('Introduzca una secuencia de DNA que se encuentre separada por comas: ').split(',') 
reverse_sequence = [(sequence.strip()[::-1]) for sequence in sequence] #el ::-1 indica que se va a imprimir la secuencia al reves
print (f'Las secuencia de DNA invertida es: {reverse_sequence}') 