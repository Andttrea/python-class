# etse programa cuantas veces aparece cada base en una tupla

secuencia = tuple("ATGCGTAGC")

print(secuencia.count("A"))
print(secuencia.count("T"))
print(secuencia.count("G"))
print(secuencia.count("C"))

#Forma 2 = comprensión de listas
bases = list("ATGC")
freq = {base: secuencia.count(base) for base in bases}
print(freq) 


#Forma 3 ciclos
for base in "ACGT":
    print(f"{secuencia.count(base)} bases {base}")