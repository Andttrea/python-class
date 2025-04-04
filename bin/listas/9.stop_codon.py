# Este programa va a hacer uso de comprensión de listas y listas para filtrar aquellas secuencias que contengas un codón de termino. 
sequences = input('Introduzca una secuencia de DNA que se encuentre separada por comas: ').split(',')

stop_codons = [sequence.strip() for sequence in sequences if "TAA" in sequence or "TAG" in sequence or "TGA" in sequence] 
print(f'El codón de termino es: {stop_codons}')