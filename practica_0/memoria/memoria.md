---
title: Práctica 0
author: Blanca Cano Camarero
header-includes:
- \usepackage{graphicx}
- \usepackage{subfig}
- \usepackage{subcaption}
- \graphicspath{ {./media/} }
---


Esta memoria contiene la resolución de ejercicios de la práctica 0. 

## **Ejercicio** 1
Escribir una función que lea el fichero de una imagen y permita mostrarla
tanto en grises como en color (im=leeimagen(filename, flagColor)).
flagColor es la variable que determina si la imagen se muestra en escala
de grises o en color.

### Explicación de la solución  

La solución se implementa con la función `leeImagen(filename, flagColor):`
Usaremos la función propia de cv2 imread. 
`imread(path, flag)`, que muestra el path de la imagen y flag el método en que la variable será leída.  

Los flags que nos van a ser útiles son: 


- `cv2.IMREAD_COLOR` para color equivale al entero 1. 
- `cv2.IMREAD_GRAYSCALE` Modo de escala de grises, equivale al entero 0.


Recursos utilizados (fecha de consulta 24/09/21): 
[Geekforgeek](https://www.geeksforgeeks.org/python-opencv-cv2-imread-method/)

Prueba de que la solución parece estar bien hecho son las figuras \ref{fig:1_naranja_color} y \ref{fig:1_naranja_gris}


 \begin{figure}[htp] 
    \centering
    \subfloat[Imagen a color]{%
        \includegraphics[width=0.45\textwidth]{1_naranja_color.png}%
        \label{fig:1_naranja_color}%
        }%
    \hfill%
    \subfloat[Imagen en gris]{%
        \includegraphics[width=0.45\textwidth]{1_naranja_gris.png}%
        \label{fig:1_naranja_gris}%
        }%
    \caption{Imágenes mostradas con imread (Notebook)}
\end{figure}

## Ejercicio 2 
Escribir una función que permita visualizar una matriz de números reales
cualquiera/arbitraria, tanto monobanda como tribanda (pintaI(im)). Para
ello se deberá escalar el rango de cada banda al intervalo [0,1] sin pérdida
de información.

### Explicación    
La solución es implementada con la función `pintaI(imagen, titulo="")`.
Vamos a mostrarlo con la biblioteca de mathplotlib, usando la función usando la función `imsshow`. La documentación [ha sido la oficial (pulse par redirigir)](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html)
Consultada a día 29 de septiembre. 

Destacamos el rango de valores que pueden tomar los colores, en el intervalo [0,1] si usamos flaot y de 0 a 255 si enteros.  
(Información oficial)

\begin{figure}[htp] 
    \centering
    \subfloat[Imagen a color]{%
        \includegraphics[width=0.45\textwidth]{2_matriz_color.png}%
        \label{fig:1_naranja_color}%
        }%
    \hfill%
    \subfloat[Imagen en gris]{%
        \includegraphics[width=0.45\textwidth]{2_matriz_gris.png}%
        \label{fig:1_naranja_gris}%
        }%
    \caption{Imágenes mostradas con `PintaI`}
\end{figure}

## Ejercicio 3

Escribir una función que visualice varias imágenes distintas a la vez
(concatenando las imágenes en una última imagen final 1 ): pintaMI(vim).
(vim será una secuencia de imágenes) ¿Qué pasa si las imágenes no son
todas del mismo tipo?

### Descripción 

Pretendemos visualizar varias imágenes concatenadas. 
La descripción general del algoritmo es:
1. Criterio para manejar las que estén en color y las que no.
2. Ajustar tamaño
3. Concatenar. 

La soluciones aportadas:
1. Se pasan todas a color.
2. Deben de ser del mismo tamaño: hemos optado por agrandar hasta el tamaño de la mayor. Se añadirán border si fuera necesario utilizando: `copyMakeBorder`. 
3. Concatenamos las sucesivas imágenes. 

La solución se encuentra implementada en `pintaMI`. 

El resultado de usar la función con diferentes combinaciones de imágenes es: 

\begin{figure}[htbp]
  \centering
  \begin{subfigure}{0.56\textwidth}
    \includegraphics{3_todas_pintadas_color.png}
    \caption{Todas imágenes concatenadas}
    \label{fig:3_todas_color}
  \end{subfigure}
   \begin{subfigure}{0.56\textwidth}
    \includegraphics{3_todas_pintadas_gris.png}
    \caption{Todas imágenes concatenadas en escala de gris}
    \label{fig:3_todas_gris}
  \end{subfigure}
  \begin{subfigure}{0.56\textwidth}
    \includegraphics{3_mezclamos_colores-png}
    \caption{Combinamos imagen en blanco y negro}
    \label{fig:demo3}
  \end{subfigure}
  \caption{Demo}
\end{figure}



