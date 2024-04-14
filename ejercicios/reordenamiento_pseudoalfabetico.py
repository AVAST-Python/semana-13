
# -------------------------------------
# Creación del array de números
# -------------------------------------

numeros = []

# con un bucle
for number in range(1, 101):
    numeros.append(number)

# Con la función list
numeros = list(range(1, 101))

letras = []

# Creación del array de letras
for number in range(1, 101):
    letra = str(number)
    letras.append(letra)

# print(numeros)
# print(letras)

# -------------------------------------
# Ordenación
# -------------------------------------

# sorted() devuelve una copia ordenada del array
numeros_ordenados = sorted(numeros)
letras_ordenadas = sorted(letras)

# sort() ordena el array original
numeros.sort()
letras.sort()

# print(numeros)
# print(letras)
# print(numeros_ordenados)
# print(letras_ordenadas)


# -------------------------------------
# Comparación
# -------------------------------------

for indice in range(0, len(numeros)):
    print(numeros_ordenados[indice], letras_ordenadas[indice])
    if(str(numeros_ordenados[indice]) == letras_ordenadas[indice]):
        print(f'El número ${numeros_ordenados[indice]} coincide')

