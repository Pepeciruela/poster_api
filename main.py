import requests

API_KEY="e35ce937"
url_busqueda = "http://www.omdbapi.com/?apikey={}&s={}"
url_identificador = "http://www.omdbapi.com/?apikey={}&i={}"

def peticion(url):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        if datos['Response'] == "False":
            print(datos["Error"])
            # ver que hacer con el error
        else:
            return datos
    else:
        print("Error en consulta por id:", nueva_respuesta.status_code)
        # ver que hacer con el error
        
        primera_peli = datos['Search'][0]
        clave = primera_peli['imdbID']

pregunta = input("Titulo de la película: ")

respuesta = peticion(url_busqueda.format(API_KEY, pregunta))
primera_peli = respuesta["Search"][0]
clave = primera_peli["imdbID"]

respuesta = peticion(url_identificador.format(API_KEY, clave))
titulo = respuesta['Title']
agno = respuesta['Year']
director = respuesta['Director']
print("La peli {}, estrenada en el año {}, fue dirigida por {}".format(titulo, agno, director))    

