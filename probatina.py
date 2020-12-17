import requests

direccion = "http://www.omdbapi.com/?apikey=e35ce937&i=tt3896198"

#HACER PETICIÓN HTTP
respuesta = requests.get(direccion)

if respuesta.status_code == 200:
    print (respuesta.text)
    datos = respuesta.json()
    print(datos)
else:
    print ("Se ha producido un error", respuesta.status_code)