secuencia = input("Ingrese una secuencia de nucleótidos: ")
print (f'La secuencia proporcionada es: {secuencia}')

for nucleotido in "ACGT": 
  print(f"El nucleótido {nucleotido} aparece {secuencia.count(nucleotido)} veces") # count es un método que cuenta el número de veces que aparece un elemento