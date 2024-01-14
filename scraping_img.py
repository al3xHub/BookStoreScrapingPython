import bs4
import requests

url = requests.get('https://www.escueladirecta.com/courses/')
soup = bs4.BeautifulSoup(url.text, 'html.parser')

images = soup.select('.course-box-image')[0]['src']
print(images)

imagen_curso = requests.get(images)
f = open('mi_imagen.jpg', 'wb')  # abrir un archivo que escribe en binario
f.write(imagen_curso.content)
f.close()


