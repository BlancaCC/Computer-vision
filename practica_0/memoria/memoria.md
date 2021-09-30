---
title: Práctica 0
author: Blanca Cano Camarero
header-includes:
- \usepackage{graphicx}
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

\newpage

## Ejercicio 2 
Escribir una función que permita visualizar una matriz de números reales
cualquiera/arbitraria, tanto monobanda como tribanda (pintaI(im)). Para
ello se deberá escalar el rango de cada banda al intervalo [0,1] sin pérdida
de información.

### Explicación    
Para conseguir el objetivo tendremos que resolver dos problemas principalmente: 
1. Conseguir un reeescalado. 
2. Mostrarlo. 

#### Soluciones 

1. Para conseguir el reescalado aplicaremos un homeomorfismo del intervalo $[a,b]$ a $[0,1]$. 

Como no se nos ha proporcionado información adicional sobre el ejercicio supondremos que $a$ es el valor mínimo de las entradas de la matriz y $b$ el valor máximo. 

Distinguimos las siguientes casuísticas: 

- Para $a$ = $b$,  puesto que no nos indica nada, tomamos el criterio arbitrario de poner a cero todas las entradas.

- En caso de que sean diferentes: 
Para todo $p \in \mathbb R^d$ con $d \in \{1,3\}$ un pixel de la matriz (1 si es gris, 3 si es de colores). El homeomorfismo de reescalado $R$ viene dado por: 

$$R(p) = \frac{p-a}{b-a}$$

2. Para la muestra. 
Vamos a mostrarlo con la biblioteca de mathplotlib. 
Cabe destacar que para mathplotlib es necesario invertir los canales de colores. 

Otra opción (implementada en pintaI2)
la función `cv2.imshow` no es posible usarla en colab, luego hemos usado una alternativa proporcionada por google 
Hemos usado este ejemplo
[Link ejemplo colab](
https://colab.researchb.google.com/github/xn2333/OpenCV/blob/master/Image_Processing_in_Python_Final.ipynb#scrollTo=6dy-iP-VTib)

Un ejemplo de ejecución sería:
1. Matriz de colores aleatoria \ref{fig:2_color}. 
2. Matriz solo de unos \ref{fig:2_unos}.
3. Matriz en blanco y negro \ref{fig:2_gris}.
\begin{figure}[htp] 
    \centering
    \subfloat[Matriz aleatoria colores]{%
        \includegraphics[width=0.45\textwidth]{2_matriz_colores.png}%
        \label{fig:2_color}%
        }%
    \hfill%
    \subfloat[Matriz con todas las entradas a uno]{%
        \includegraphics[width=0.45\textwidth]{2_matriz_de_unos.png}%
        \label{fig:2_unos}%
        }%
        \hfill%
    \subfloat[Imagen en escala de grises]{%
        \includegraphics[width=0.45\textwidth]{2_matriz_gris.png}%
        \label{fig:2_gris}%
        }%
    
    \caption{Imágenes mostradas con `PintaI`}
\end{figure}

\newpage

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
1. Se transforman todas a color gracias a la función `cv2.cvtColor`.  

2. Deben de ser del mismo tamaño: hemos optado por escalar la alturas hasta el tamaño de la mayor.
Esto se hace por medio de la función de `cv2.resize`.  

La documentación seguida ha sido la de la página oficial  a día  29 de septiembre 
[link](https://docs.opencv.org/3.4.15/dd/d52/tutorial_js_geometric_transformations.html)  

3. Concatenamos las sucesivas imágenes.   

El resultado de usar la función con diferentes combinaciones de imágenes es: 

\begin{figure}[]
  \centering
  \begin{subfigure}{\textwidth}
   \centering
    \includegraphics{3_todas_color.png}
    \caption{Todas las imágenes concatenadas}
    \label{fig:3_todas_color}
  \end{subfigure}
   \begin{subfigure}{\textwidth}
    \centering
    \includegraphics{3_todas_gris.png}
    \caption{Todas imágenes concatenadas en escala de gris}
    \label{fig:3_todas_gris}
  \end{subfigure}
  \begin{subfigure}{\textwidth}
   \centering
    \includegraphics{3_mezcla}
    \caption{Combinamos imagenes en blanco y negro}
    \label{fig:3_mezcla}
  \end{subfigure}
  \caption{Ejemplos de ejecución ejercicio 3}
\end{figure}

Como podemos observar en \ref{fig:3_mezcla} nuestra función admite combinar imágenes en blanco y negro y color gracias a que hemos transformado todas las imágenes a color. 

Esto tiene la desventaja de que durante la ejecución consumirá más memoria, este gasto será además innecesario para el caso en que todas las imágenes sean grises. Sin embargo al nivel en que estamos trabajando consideramos esta opción por agilidad en programación. 

\newpage

# Ejercicio 4

4. Escribir una función que modifique el color en la imagen de cada uno de
los elementos de una lista de coordenadas de píxeles 2 . En concreto, los
alumnos deben insertar un cuadrado azul de 100x100 pixeles en el centro
de la imagen a modificar.

## Descripción general del procedimiento

Dado que las imágenes no dejan de ser matrices, cambiaremos el color de las entradas pedidas. 
La función `CambiaPixeles` permite cambiar el color de píxeles de la lista de manera genérica. 
`InsertaCuadradoAzul` es la función que resuelve nuestro problema. 

Detalles que se han tenido en cuenta:   

1. El color se encuentra en BGR en vez de RGB y va de 0 a 255 (en el caso de estar en modo entero). 

Cabe además destacar que se ha tenido en cuenta que la imagen puede estar en escala de grises, en ese caso se le asociará el gris correspondiente al azul (que no es más que que la media). 

2. Los ejes están girados 90º en sentido horario con centro en el origen con respecto al sistema de referencia usual en matemáticas.   

Por lo demás, las operaciones para calcular el centros son tan simples como dado un lado (ya sea altura o anchura), restarle los 100 píxeles del cuadrado azul y dividir entre dos. El píxel resultante y los 100 siguientes serán un lado del cuadrado. 

### Ejemplos 

- Imagen a color a la que se le ha añadido cuadrado azul \ref{fig:4_color}.  

- Imagen en escala de grises que ha sido transformada a color y por lo que se le ha añadido cuadrado azul \ref{fig:4_messi_color}. 

- Imagen, monocromática a la que se le ha añadido el cuadrado \ref{fig:4_gris}. Por ser monocromática el cuadrado respeta la escala de grises. 


\begin{figure}[h]
  \centering
   \begin{subfigure}{\textwidth}
    \centering
    \includegraphics[width=0.45\textwidth]{4_naranja.png}
    \caption{Imagen a color.}
    \label{fig:4_color}
  \end{subfigure}
  \begin{subfigure}{\textwidth}
   \centering
    \includegraphics[width=0.45\textwidth]{4_messi_color.png}
    \caption{Combinamos imagenes en blanco y negro}
    \label{fig:4_messi_color}
  \end{subfigure}
  \begin{subfigure}{\textwidth}
   \centering
    \includegraphics[width=0.45\textwidth]{4_gris.png}
    \caption{Imagen en escala de grises.}
    \label{fig:4_gris}
  \end{subfigure}
  \caption{Ejemplos del ejercicio 4, añadir cuadrado azul en el centro}
\end{figure}

\newpage  

# Ejercicio 5  

5.Una función que sea capaz de representar varias imágenes con sus títulos en una misma ventana.

## Solución  

Puesto que no se especifica se han contemplado los siguientes casos:   

1. Las imágenes se quieren separadas. Para ello nos hemos basado en  [estos ejemplos](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html)
. Un ejemplo del resultado en la imagen \ref{fig:5_dispersas}.

2. Se ha contemplado la opción de que se quieran la imágenes concatenadas. esto se resuelve en la función multiplesImagenConcatenadasConTitulo(v_image, v_titulo )`.  Un ejemplo del resultado en la imagen \ref{fig:5_concatenadas}.



\begin{figure}[h]
  \centering
   \begin{subfigure}{\textwidth}
    \centering
    \includegraphics[width=\textwidth]{5_dispersas}
    \caption{Imágenes juntas en la misma imagen}
    \label{fig:5_dispersas}
  \end{subfigure}
  \begin{subfigure}{\textwidth}
   \centering
    \includegraphics[width=\textwidth]{5_concatenadas}
    \caption{Se concatenan las imágenes y se le añaden los respectivos títulos}
    \label{fig:5_concatenadas}
  \end{subfigure}
  \caption{Ejemplos del ejercicio 5}
\end{figure}