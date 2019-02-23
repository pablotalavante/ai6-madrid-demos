import os
from PIL import Image

path = './'
os.listdir(path) #devuelve una lista de los elementos en PATH

path = './house'
image_list = os.listdir(path) #devuelve una lista de los elementos en la carpeta sample_data
image_list = list(filter(lambda x: x.endswith('.jpg'), image_list)) #filtrado ?

for img in image_list:
  image_path = os.path.join(path, img)
  im = Image.open(image_path)
  image_path

