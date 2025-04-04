# Este es un programa que convierte las secuencias en fomrato tsv a formato fasta.

with open('data/dna_sequences.txt', 'r') as infile, open('results/dna_sequences.fa', 'w') as outfile:
    for line in infile:
        columns = line.strip().split('\t') #strip elimina los espacios y split separa la cadena ṕor tabuladores, cada uno de esos les asigna indices

        outfile.write  (f'>{columns[0]}\n{columns[1].upper()}\n') # upper convierte la cadena a mayúsculas
    


    