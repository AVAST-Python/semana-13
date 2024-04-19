def distancia_ascensor(A, B):
    # Desempaquetar las coordenadas de los puntos A y B
    x1, y1 = A
    x2, y2 = B

    # Si los puntos están en distinta vertical
    if x1 != x2 :
        # Calcular la distancia vertical desde A hasta el eje X (planta baja)
        distancia_vertical_A = abs(y1)
        # Calcular la distancia horizontal desde el eje X hasta la vertical del punto B
        distancia_horizontal = abs(x2 - x1)
        # Calcular la distancia vertical desde la vertical del punto B hasta B
        distancia_vertical_B = abs(y2)
        # Calcular la distancia total sumando las distancias verticales y horizontales
        distancia_total = distancia_vertical_A + distancia_horizontal + distancia_vertical_B

    else: # Los puntos están en la misma vertical
        distancia_total = abs(y1 - y2)

    return distancia_total

# Ejemplo de uso
punto_A = (3, 5)
punto_B = (3, 10)
print(f'La distancia ascensor entre los puntos {punto_A} y {punto_B} es:', distancia_ascensor(punto_A, punto_B))

punto_A = (3, 5)
punto_B = (4, 5)
print(f'La distancia ascensor entre los puntos {punto_A} y {punto_B} es:', distancia_ascensor(punto_A, punto_B))
