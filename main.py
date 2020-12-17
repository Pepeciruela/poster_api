import requests

pregunta = input("Titulo de la película: ")

API_KEY = "e35ce937"

direccion = f"http://www.omdbapi.com/?apikey={API_KEY}&Ss={pregunta}"

respuesta = requests.get(direccion)

if respuesta.status_code == 200:
    datos = respuesta.json()
    if datos ["Response"] == "False":
        print(datos("Error"))
    else:
        primera_peli = datos["Search"][0]
        clave = primera_peli["imbID"]
        
        otra_direccion = f"http://www.omdbapi.com/?apikey={API_KEY}&Si={clave}"
        nueva_respuesta = requests.get(otra_direccion)
        if nueva_respuesta.status_code == 200:
            datos = nueva_respuesta.json()
            if datos ["Response"] == "False":
            print(datos("Error"))
            else:
                titulo = datos["Title"]
                agno = datos["Year"]
                director = datos["Director"]
                print(f"La pelicula {titulo}, estrenada en el año {agno}, fue dirigida por {director}")
        else:
            print("Error en consulta:", nueva_respuesta.status_code)
else:
    print("Error en consulta:", respuesta.status_code)
    
            