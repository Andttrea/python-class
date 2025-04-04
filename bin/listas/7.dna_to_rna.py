# Este programa va a uso de comprensión de listas para converitr una secuencia de ADN en ARN.

sequences = input('Introduzca una secuencia de DNA que se encuentre separada por comas: ').split(',') 

rna_sequences = [(sequence.strip().replace ('T', 'U')) for sequence in sequences]
print (f'Las secuencias de ARN son: {rna_sequences}')