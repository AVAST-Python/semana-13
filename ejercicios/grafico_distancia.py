import matplotlib.pyplot as plt

def funcion_condicional(punto):
    # Ejemplo de una función condicional: devuelve True si la suma de las coordenadas es mayor a 10
    return sum(punto) > 10

def generar_puntos(punto_central, distancia, num_puntos):
    x_central, y_central = punto_central
    puntos_generados = []
    for i in range(num_puntos):
        angulo = 2 * i * 3.14159 / num_puntos  # Distribuir los puntos uniformemente alrededor del círculo
        x = x_central + distancia * 1.0 * math.cos(angulo)
        y = y_central + distancia * 1.0 * math.sin(angulo)
        puntos_generados.append((x, y))
    return puntos_generados

def scatter_plot_condicional(punto_central, distancia, num_puntos):
    # Generar los puntos alrededor del punto central con la distancia especificada
    puntos = generar_puntos(punto_central, distancia, num_puntos)

    # Separar los puntos que cumplen la condición de la función
    puntos_verdaderos = [punto for punto in puntos if funcion_condicional(punto)]

    # Obtener las coordenadas x e y de los puntos y del punto central
    xs, ys = zip(*puntos)
    x_central, y_central = punto_central

    # Crear el scatter plot
    plt.scatter(xs, ys, color='gray', label='Puntos')

    # Agregar el punto central
    plt.scatter(x_central, y_central, color='red', label='Punto Central')

    # Agregar los puntos que cumplen la condición
    if puntos_verdaderos:
        xs_verdaderos, ys_verdaderos = zip(*puntos_verdaderos)
        plt.scatter(xs_verdaderos, ys_verdaderos, color='blue', label='Puntos Verdaderos')

    # Configuraciones adicionales
    plt.xlabel('Coordenada X')
    plt.ylabel('Coordenada Y')
    plt.title('Scatter Plot con Función Condicional')
    plt.legend()
    plt.grid(True)

    # Mostrar el gráfico
    plt.show()

# Ejemplo de uso
import math
punto_central = (5, 5)
distancia = 1
num_puntos = 10
scatter_plot_condicional(punto_central, distancia, num_puntos)
