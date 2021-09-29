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
def pintaI(imagen, titulo=""):
    plt.title(titulo)
    # si la imagen es tribanda, tenemos que invertir los canales B y R
    # si es en blanco y negro, tenemos que decirle a matplotlib que es monobanda
    if imagen.ndim == 3 and imagen.shape[2] >= 3:
        plt.imshow(imagen[:,:,::-1])
    else:
        plt.imshow(imagen, cmap='gray')
    plt.show()


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
# Funciones auxiliares
def isBW(im):
  """Indica si una imagen está en blanco y negro"""
  return len(im.shape) != 3

# Función principal 
def pintaMI (vim, titulo= "Imágenes"): 
  '''Pinta múltiples imágenes
  @param vim: vector de imágenes
  @param titulo: Título de las imágenes 
  '''
  altura = max([ imagen.shape[1]for imagen in vim   ])

  for i,imagen in enumerate(vim):
    # Pasamos a color si es blanco y negro
    if isBW(imagen): # Pasar a color
      vim[i] = cv2.cvtColor(vim[i], cv2.COLOR_GRAY2BGR)

    if imagen.shape[0] < altura: # Redimensionar imágenes
      vim[i] = cv2.copyMakeBorder(
        vim[i], 0, altura - vim[i].shape[0],
        0, 0, cv2.BORDER_CONSTANT, value = (0,0,0))

  imMulti = cv2.hconcat(vim)
  pintaI(imMulti, titulo)

## Ejecución de ejemplo 
pintaMI ( [img_messi_color, img_orapple_color], 'Messi y orapple')
pintaMI(imagenes_color, 'Todas pintadas en color')
pintaMI(imagenes_gris, 'Todas pintadas en Gris')

# ¿Qué corre si mezclamos una en blanco y negro con otra en color?
pintaMI( [imagenes_color[1], imagenes_gris[1]], 'Mezclamos color con blanco y negro')
# Lo hace sin problema gracias a que lo transformamos a color
STOP()




