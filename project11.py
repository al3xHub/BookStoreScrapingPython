import bs4
import requests

# Crear url sin nº de página.
url = 'https://books.toscrape.com/catalogue/page-{}.html'

lista_titulos_cuatro_estrellas = []

# iterar páginas
for pagina in range(1, 9 + 1):
    # crear sopa en cada página.
    url_pagina = url.format(pagina)
    resultado = requests.get(url_pagina)
    soup = bs4.BeautifulSoup(resultado.text, 'html.parser')

    # seleccionar datos de cada sopa
    libros = soup.select('.product_pod')

    # Iterar libro
    for libro in libros:
        # chequear +4 estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:
            # guardar titulo
            titulo_libro = libro.select('a')[1]['title']

            # agregar libro a la lista
            lista_titulos_cuatro_estrellas.append(titulo_libro)

# ver libros en consola
for t in lista_titulos_cuatro_estrellas:
    print(t)



