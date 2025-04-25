def at_content(dna, sig_figs=2):
    """
    Calcula el contenido AT de una secuencia de ADN,
    redondeando a un número específico de cifras decimales.
    Parámetros:
    dna (str): Secuencia de ADN (ej. 'ATGCGC')
    sig_figs (int, opcional): número de cifras decimales (por defecto = 2)
    Retorna:
    float: contenido AT redondeado
    """
    dna = dna.upper()
    length = len(dna)
    a_count = dna.count ('A')
    t_count = dna.count ('T')
    at_content = (a_count + t_count)/ length
    return round(at_content, sig_figs)



#assert lo utilizamos para comprobar que el resultado es correcto, este es un testing temporal 
#assert at_content("ATGCGC",1) == 0.5
#assert at_content("ATCGNNN", 1) == 0.5 
#para resolver este último caso tendríamos que remplazar o eliminar las N's



# Imprimir el resultado de la función at_content
resultado = at_content("GAGAGCGGTGAGCTG",1) 
print(resultado)

resultado = at_content("gagcgagtgacgt")
print(resultado)
