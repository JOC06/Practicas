

import requests
from bs4 import BeautifulSoup

def buscar_en_linea(query):
    url = f"https://www.google.com/search?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        # Extraer los resultados de búsqueda
        resultados = soup.find_all("h3")
        for i, resultado in enumerate(resultados, 1):
            print(f"{i}. {resultado.get_text()}")

    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud: {e}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    busqueda = input("Ingresa tu consulta: ")
    buscar_en_linea(busqueda)

    #
    #