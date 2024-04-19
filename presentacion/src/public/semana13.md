# Introducción a Python

## Semana 13
<!-- .element style="text-align:center" -->

![alt text](./img/logo2.png) <!-- .element style="margin-left: auto; margin-right: auto; display: block" -->

---

# Dibujar en Python

Dibujar es difícil. Hace falta una librería. Hay diferentes enfoques:

- [tcl/tk](https://www.tcl.tk/): Dibujo de bajo nivel. Normalmente es usado por otras librerías
- [Pygame](https://www.pygame.org/news): Orientado a la creación de juegos.
- [Matplotlib](https://matplotlib.org/) Orientada a dibujar gráficos. Es la que vamos a utilizar hoy.

---

# Matplotlib

- Biblioteca para generar gráficos de distintos tipos
- Se integra con [numpy](https://numpy.org/) (librería de manejo de datos)
- Tipos básicos de gráfico:
<style>
    table {
        border-collapse: collapse;
    }
    td, th {
        border: none;
        padding: 5px; /* Adjust padding as needed */
    }
</style>

<table style="border:none !important">
  <tr>
    <td style="border:none">
      <img src="image1.jpg" alt="Image 1" style="vertical-align: middle;">
    </td>
    <td style="vertical-align: middle; border: none">
      Text for Image 1
    </td>
  </tr>
  <tr>
    <td style="border:none">
      <img src="image1.jpg" alt="Image 1" style="vertical-align: middle;">
    </td>
    <td style="vertical-align: middle; border: none">
      Text for Image 1
    </td>
  </tr>
  <tr>
    <td style="border:none !important">
      <img src="image1.jpg" alt="Image 1" style="vertical-align: middle;">
    </td>
    <td style="vertical-align: middle; border: none">
      Text for Image 1
    </td>
  </tr>
</table>


https://www2.eii.uva.es/fund_inf/python/notebooks/Bibliotecas/01_Introduccion_a_Matplotlib/Introduccion_a_Matplotlib.html




---

# Preparación del entorno

- Vamos a trabajar en un servidor de Jupyter Lab:<br/>
[https://becoming-formally-lab.ngrok-free.app](https://becoming-formally-lab.ngrok-free.app) (password: `patata`)
- Puedes lanzar tu propio servidor de Jupyter en casa con docker compose:
```sh
cd jupyter
docker compose up
```
- Puedes trabajar en local con entornos virtuales (mira el fichero README.md)

Notes:
`ngrok http 8888 --domain=becoming-formally-lab.ngrok-free.app`


---


lista_x = np.linspace(x_min, x_max, num_puntos)

---

Dos equipos:
- Nivel alto de programación: preparan el gráfico con una funcion distancia falsa
- Nivel bajo de preparación: preparan la función distancia

Luego los juntamos

---


---



---
