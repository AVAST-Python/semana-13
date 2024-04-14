
def como_de_buena_eres_1(tu_puntuacion, puntuaciones_clase):
    total = 0
    cuenta = 0
    for puntuacion in puntuaciones_clase:
        total += puntuacion
        cuenta += 1
    media = total / cuenta

    if tu_puntuacion > media:
        return True
    else:
        return False



def como_de_buena_eres_2(tu_puntuacion, puntuaciones_clase):
    total = 0
    for puntuacion in puntuaciones_clase:
        total += puntuacion
    media = total / len(puntuaciones_clase)

    return tu_puntuacion > media




def media_1(puntuaciones_clase):
    total = 0
    for puntuacion in puntuaciones_clase:
        total += puntuacion
    return total / len(puntuaciones_clase)

def media(puntuaciones_clase):
    return sum(puntuaciones_clase) / len(puntuaciones_clase)

def como_de_buena_eres(tu_puntuacion, puntuaciones_clase):
    media_clase = media(puntuaciones_clase)
    return tu_puntuacion > media_clase




NOTAS_CLASE_1 = [5, 6, 7, 8, 9] # media 7
NOTAS_CLASE_2 = [7, 8, 9, 10, 8, 10, 7] # media 8.4285
NOTAS_CLASE_3 = [2, 3, 4, 5, 3, 1] # media 3


print(como_de_buena_eres(8, NOTAS_CLASE_1))
print(como_de_buena_eres(8, NOTAS_CLASE_2))
print(como_de_buena_eres(6, NOTAS_CLASE_1))
