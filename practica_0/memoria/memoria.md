---
title: Práctica 0
author: Blanca Cano Camarero
header-includes:
- \usepackage{graphicx}
- \graphicspath{ {./media/} }
---


Esta memoria contiene la resolución de ejercicios de la práctica 0. 

## **Ejercicio** 1
Escribir una función que lea el fichero de una imagen y permita mostrarla
tanto en grises como en color (im=leeimagen(filename, flagColor)).
flagColor es la variable que determina si la imagen se muestra en escala
de grises o en color.

### Explicación de la solución  
Usaremos la función propia de cv2 imread. 
`imread(path, flag)`, que muestra el path de la imagen y flag el método en que la variable será leída.  

Los flags que nos van a ser útiles son:  
- `cv2.IMREAD_COLOR` para color 
- `cv2.IMREAD_GRAYSCALE` Modo de escala de grises. 

Los flags no son más que los enteros 1 y 0 respectivamente.

Recursos utilizados (fecha de consulta 24/09/21): 

![Geekforgeek](https://www.geeksforgeeks.org/python-opencv-cv2-imread-method/)

Prueba de que la solución parece estar bien hecho son las figuras 1 y 2.

\begin{figure}[!h]
 \centering \includegraphics[width=1\textwidth]{1_naranja_gris.png} \caption{Naranja manzana a color}
 } \end{figure}.

