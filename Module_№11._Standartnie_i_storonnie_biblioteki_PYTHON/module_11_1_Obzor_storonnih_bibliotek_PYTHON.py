import requests as rq
import numpy as np
from PIL import Image

URL = "https://binaryjazz.us/wp-json/genrenator/v1/genre/"

zapros = rq.get(URL)

print(zapros.url)
print(zapros.json())
print(zapros.raw,'\n')

massNum = np.array([10,50,1,-25,90,0,-10,7])
print(massNum)
print(massNum.min())
print(massNum.argmin())
print(massNum.max())
print(massNum.argmax())
print(massNum.argsort())
massNum.sort()
print(massNum)
print(sum(massNum),"\n")

izobrajenie = Image.open("cosmos.jpg")
r, g, b = izobrajenie.split()
print(izobrajenie.format,izobrajenie.size,izobrajenie.mode)
izobrajenie = Image.merge("RGB", (b, r, g))
izobrajenie = izobrajenie.resize((1920,1080))
izobrajenie = izobrajenie.rotate(180)
print(izobrajenie.format,izobrajenie.size,izobrajenie.mode)
izobrajenie.show()