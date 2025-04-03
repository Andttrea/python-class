# Este programa cuenta el número de secuencias en un archivo FASTA.

data_file = 'data/secuencias.fasta'

with open(data_file, 'r') as file:
    lines = file.readlines() #aquí vamos a leer las líneas del archivo

filtered_lines = [line for line in lines if line.startswith('>')] #aquí vamos a filtrar las líneas que empiezan con '>'
print(f'EL número total de secuencias es: {len(filtered_lines)}') 
