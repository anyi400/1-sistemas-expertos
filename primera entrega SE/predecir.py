#hacemos uso de la libreria tesseract para poder hacerder al texto dentro de la imagen 
#! pip install tesseract-ocr 
#! pip install pytesseract

#importamos las dependencias que se van a utilizar 
# Importamos Pytesseract
#! sudo apt install tesseract-ocr 

import shutil
import os
import random
import pytesseract
try:
 from PIL import Image
except ImportError:
 import Image

 #hacemos uso de la dependencia que nos pernite acceder a cualquier archivo dentro de nuestro equipo 
#from google.colab import files
from io import BytesIO
from PIL import Image

#uploaded = files.upload()
#BytesIO(uploaded['letras.jpg'])
im = Image.open("letras.jpg")

# Utilizamos el método "image_to_string"
# Le pasamos como argumento la imagen abierta con opencv
texto = pytesseract.image_to_string(im)

# Mostramos el resultado
print(texto)

