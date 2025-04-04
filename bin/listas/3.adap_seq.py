# Este programa se trata de eliminar los primeros 14 adaptadores de una secuencia dada.

with open('data/4_input_adapters.txt', 'r')as infile, open('results/4_output_adapters.txt', 'w') as outfile:
    for line in infile:
        no_primers = line.strip()[14:]

        outfile.write(f'{no_primers}\n')
    