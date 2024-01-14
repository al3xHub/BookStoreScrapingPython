import bs4
import requests

resultado = requests.get('https://escueladirecta-blog.blogspot.com/2022/10/por-que-se-utiliza-python-en-ciencia-de.html')
soup = bs4.BeautifulSoup(resultado.text, 'html.parser')

todos_elementos = soup.select('h1')
print(todos_elementos)

elementos_contengan_id = soup.select('#page-skin-1')
print(elementos_contengan_id)

elementos_contengan_class = soup.select('.blogger')
print(elementos_contengan_class)

elementos_dentro_elemento = soup.select('div a')
for a in elementos_dentro_elemento:
    print(a.getText())  # De cada div a imprime solo el texto del interior.

elemento_dentro_nada_en_medio = soup.select('div>span')
print(elemento_dentro_nada_en_medio)

