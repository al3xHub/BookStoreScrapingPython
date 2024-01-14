import bs4
import requests

resultado = requests.get('https://escueladirecta-blog.blogspot.com/')

# print(resultado.text) # Te imprime el resultado en string
soup = bs4.BeautifulSoup(resultado.text, 'html.parser')  # Te imprime el resultado con los enlaces listos a hacer
# click (en azul)

print(soup.select('title')[0].getText())  # selecciona la etiqueta 'title' la primera posicion y solamente el texto.
parrafo_especial = soup.select('a')
print(parrafo_especial)
