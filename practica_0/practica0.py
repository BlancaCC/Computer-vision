'''
    PRÁCTICA 0
Blanca Cano Camarero
Septiembre 2021
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt

# __ Paths y configuraciones iniciales __
# Rutas posibles
colab =  '/content/drive/MyDrive/Visión por computador/práctica 0/images/'
local = './images/'
ruta_actual = local

if(ruta_actual == colab): 
    from google.colab import drive
    drive.mount('/content/drive')

# Path de las imágenes 
path_dave = ruta_actual +'dave.jpg'
path_messi = ruta_actual + 'messi.jpg'
path_orapple = ruta_actual +'orapple.jpg'
path_logo = ruta_actual +'logoOpenCV.jpg'

todas_imagenes = [path_dave, path_logo, path_messi, path_orapple]

#########################################
## __ Función de parada __
def STOP ():
    input('----------fin sección, enter para continuar------------')
    #print('----------fin sección, enter para continuar------------')

def INIT(n:int):
    print(f'Ejercicio {n} ')

#########################################
# Ejercicio 1
INIT(1)
def leeImagen(filename, flagColor):
  '''
  @param filename: nombre de la foto 
  @para flagColor: boolean escala de grises o color
  '''
  return cv2.imread(filename, flagColor)

## Ejemplos de uso de la función 
flagColor = cv2.IMREAD_ANYCOLOR
flagGrey = cv2.IMREAD_GRAYSCALE

#orapple 
img_orapple_color = leeImagen(path_orapple, flagColor) 
img_orapple_gris = leeImagen(path_orapple, flagGrey)

# messi
img_messi_color = leeImagen(path_messi, flagColor) 
# como la imagen está en blanco y negro
# aunque pongamos el flag de color se mostrará en blanco y negro
img_messi_gris = leeImagen(path_messi, flagGrey)

## Crearemos imagen del resto para el resto de path
imagenes_color = list(map( lambda img : leeImagen( img, flagColor), todas_imagenes))
imagenes_gris = list(map( lambda img : leeImagen( img, flagGrey), todas_imagenes))

STOP()


##############################################################################
# Ejercicio 2
INIT(2)

def Reescalado (img: np.ndarray) -> np.ndarray:
    """Homeomorfismo R (ver explicación)"""
    minimo = img.min()
    maximo = img.max() 
    matrizReescada = None
    
    if(minimo == maximo):
        matrizReescalada = 0*img
    else:
        matrizReescalada = (img - minimo)/(maximo - minimo)  
        
    return matrizReescalada

def pintaI(img, titulo=""):
    '''Visualiza una matriz de números reales cualquiera'''
    plt.title(titulo)
    # si la imagen es tribanda, tenemos que invertir los canales B y R
    # si es en blanco y negro, tenemos que decirle a matplotlib que es monobanda
    imagen = Reescalado(img)
    if imagen.ndim == 3 and imagen.shape[2] >= 3:
        plt.imshow(imagen[:,:,::-1])
    else:
        plt.imshow(imagen, cmap='gray')
    plt.show()

## Ejemplo colores la matriz aleatoria 
def HomeomorfismoMatriz(a:float, b:float, matriz: np.ndarray )-> np.ndarray:
    ''' De  [0,1] a [a,b] '''
    return matriz* (b-a) +a

#######
# Definición de intervalo de rangos
a = 1; b=10; 
c=9.443; d=10

# Generamos matrices
random_img_color = HomeomorfismoMatriz(a,b,np.random.rand(20, 20, 3))
matriz_unos= np.ones((20, 20, 3))
random_img_gray = HomeomorfismoMatriz(c,d,np.random.rand(20,20))
# Pintamos las matrices
pintaI(random_img_color, f'Matriz aleatoria color en intervalo [{a}, {b}]')
pintaI(matriz_unos, 'Matriz de unos')
pintaI(random_img_gray, f'Matriz aleatoria en escala de grises en intervalo [{c}, {d}]')


## Ejemplo colores la matriz aleatoria 
# La escala iría en el interval  [0,1] por ello no se ha cambiado la escala
random_img_color = np.random.rand(20, 20, 3)
random_img_gray = np.random.rand(20,20)
pintaI(random_img_color)
pintaI(random_img_gray)
STOP()

##############################################################################
# Ejercicio 3
INIT(3)

def pintaMI(v_img, title = ""):
    '''Dado un vector de imágenes los pinta concatenados.
    '''
    # Altura mínima de las imágenes
    altura_minima = min(img.shape[0] for img in v_img)

    numero_imagenes = len(v_img)
    # Añadimos un ínico title 
        
    for i in range(numero_imagenes):
        # Escalamos la altura a la más grande
        if v_img[i].shape[0] > altura_minima: 
            ancho_reescalado = int(v_img[i].shape[1]*altura_minima/v_img[i].shape[0])
            v_img[i] = cv2.resize(v_img[i], (ancho_reescalado, altura_minima),  interpolation=cv2.INTER_AREA)
    
        # pasamos a tribanda si está en monobanda
        if len(v_img[i].shape) != 3: 
            v_img[i] = cv2.cvtColor(v_img[i], cv2.COLOR_GRAY2RGB)
        
    img_v = cv2.hconcat(v_img)
    plt.clf()
    pintaI(img_v, title)

      

## Ejecución de ejemplo 
pintaMI ( [img_messi_color, img_orapple_color], 'Messi y orapple')
pintaMI(imagenes_color, 'Todas pintadas en color')
pintaMI(imagenes_gris, 'Todas pintadas en Gris')

# ¿Qué corre si mezclamos una en blanco y negro con otra en color?
pintaMI( [imagenes_color[1], imagenes_gris[1]], 'Mezclamos color con blanco y negro')
# Lo hace sin problema gracias a que lo transformamos a color
STOP()

##############################################################################
# Ejercicio 4
INIT(4)

def CambiaPixeles ( imagen, pixeles, color):
  '''
    imagen: imagen a cambiar
    pixeles: lista de píxeles que se desean cambiar
    colores: lista de colores, el color i-ésimo se corresponde al del pixel i-ésimo de la lista de píxeles. 
  '''
  imagen_nueva = np.copy(imagen)
  
  # si la imagen es gris 
  if len(imagen_nueva.shape) != 3: 
    color = sum(color)//3
  # cambiamos píxeles 
  for (x,y) in pixeles: 
    imagen_nueva[(x,y)] = color
    
  return imagen_nueva


def InsertarCuadradoAzul (imagen): 
  '''Inserta en el centro de "imagen" un cuadrado de lado 100px pixéles
  '''
  tam_cuadrado = 100 # numero de pixeles de lado que tendrá el cuadrado
  # color azul en BGR
  color_azul = np.array([255,0,0]) 

  # cálculo de coordenadas de los píxeles teniendo en cuenta inversión (x,y de coordenadas)
  x_inicial = (imagen.shape[0]-tam_cuadrado)//2
  x_final = x_inicial + tam_cuadrado
  y_inicial = (imagen.shape [1]- tam_cuadrado)//2
  y_final = y_inicial + tam_cuadrado

  pixeles = [(x,y) for x in range(x_inicial, x_final) 
    for y in range(y_inicial, y_final)]
 
  imagenConCuadrado = CambiaPixeles(imagen, pixeles, color_azul)
  return imagenConCuadrado

## Ejecución del ejercicio con la foto de messi 
messiGrisCuadrado = InsertarCuadradoAzul(img_messi_gris)
messiColorCuadrado = InsertarCuadradoAzul(img_messi_color)
naranjaCuadrado = InsertarCuadradoAzul(img_orapple_color )
pintaI(messiGrisCuadrado)
pintaI(messiColorCuadrado)
pintaI(naranjaCuadrado)

STOP()
##############################################################################
# Ejercicio 5
INIT(5)
# Solución 1
def pintaConTitulos(v_img:list, titulos: list, columnas :int, filas:int ):
    '''Representa varias imágenes en una misma ventana
    Filas. 
    
    Suponemos:
        columnas * filas > len(v_img)
    '''
    # Gestionamos columanas y filas 
    numero_imagenes = len(v_img)
    # Preparamos grid
    fig, axs = plt.subplots(columnas, filas)
   
    for i in range(numero_imagenes):
        # pasamos a tribanda si está en monobanda
        if len(v_img[i].shape) != 3: 
            v_img[i] = cv2.cvtColor(v_img[i], cv2.COLOR_GRAY2RGB)
        # Calculamos posición en el grid
        x = i % columnas
        y = i // filas
        axs[x,y].imshow(v_img[i][:,:,::-1])
        
        # Añadimos título si lo tiene  
        if type(titulos)==list and len(titulos)>i:
            axs[x,y].set_title(titulos[i])
            
    fig.tight_layout() # Para que no se solapen los subtítulos
   
    plt.show()
    plt.clf()

    
# Solución 2
def multiplesImagenConcatenadasConTitulo(v_image, v_titulo ):
    '''Concatena las imágenes para luesgo mostrarlas con los títulos'''
    titulo = ', '.join(v_titulo[:-1]) + ' y ' + v_titulo[-1]
    return pintaMI(v_image, titulo)

pintaConTitulos(imagenes_color, ['Sudokus', 'Logo', 'Messi', 'Naranja'], 2,2)
multiplesImagenConcatenadasConTitulo(imagenes_color, ['Sudokus', 'Logo', 'Messi', 'Naranja'])
STOP()

