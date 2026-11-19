import requests


comuna_destino = 'Valparaíso'  # comuna asociada al envío
url = 'https://midas.minsal.cl/farmacia_v2/WS/getLocalesTurnos.php'


respuesta = requests.get(url)
farmacias = respuesta.json()

for farmacia in farmacias:
    if farmacia["comuna_nombre"] == "INDEPENDENCIA":
     print(farmacia["local_nombre"],farmacia["local_direccion"],farmacia["comuna_nombre"])



