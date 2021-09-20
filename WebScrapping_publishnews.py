from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pandas as pd
path = r'C:\Users\duran\Documents\chromedriver'
driver = webdriver.Chrome(path)
driver.get('https://www.publishnews.com.br/ranking')
time.sleep(5)
list_posicao = []
list_titulo = []
list_volume = []
list_data = []
list_autores = []
list_editoras = []
list_resumos =[]
list_isbn = []
list_categoria = []
list_paginas = []
final_list_isbn = []


all_weeks = driver.find_elements_by_class_name("pn-periodos-periodo")
link_list = []

for week in all_weeks:
    link = week.get_attribute('href')
    link_list.append(link)
for link in link_list:
    driver.get(link)
    fixer = link.split('mensal')[0]
    data = link.split("0/")[1]
    if fixer == 'https://www.publishnews.com.br/ranking/':
        break
    elements_titulo = driver.find_elements(By.CLASS_NAME,'pn-ranking-livro-nome')
    elements_posicao = driver.find_elements(By.CLASS_NAME,'pn-ranking-livros-posicao-numero')
    elements_volume = driver.find_elements(By.CLASS_NAME,'pn-ranking-livros-posicao-volume')
    elements_autor = driver.find_elements(By.CLASS_NAME, "pn-ranking-livro-autor")
    elements_editora = driver.find_elements(By.CLASS_NAME, "pn-ranking-livro-editora")
    elements_resumo = driver.find_elements(By.CLASS_NAME, "pn-ranking-livro-resumo")
    elements_categoria = driver.find_elements(By.CLASS_NAME, "pn-ranking-livro-categoria")
    elements_paginas = driver.find_elements(By.CLASS_NAME, "pn-ranking-livro-paginas")
    elements_isbn = driver.find_elements(By.CLASS_NAME, "pn-ranking-livro-isbn")

    counter_titulos = 0
    counter_posicao = 0
    counter_volume = 0
    counter_autores = 0
    counter_editora = 0
    counter_categoria = 0
    counter_paginas = 0
    counter_isbn = 0
    for elements in elements_titulo:
        counter_titulos += 1
    for elements in elements_posicao:
        counter_posicao += 1

    for elements in elements_volume:

        counter_volume += 1
    for elements in elements_autor:

        counter_autores += 1
    for elements in elements_editora:

        counter_editora += 1
    for elements in elements_categoria:

        counter_categoria += 1
    for elements in elements_paginas:

        counter_paginas += 1

    for elements in elements_isbn:
        counter_isbn += 1
        soma_counter = counter_titulos + counter_editora + counter_volume + counter_autores + counter_categoria + counter_isbn + counter_paginas + counter_posicao

        if counter_titulos == 20 and counter_editora == 20 and counter_volume == 20 and counter_autores == 20 and counter_categoria == 20 and counter_isbn == 20 and counter_paginas == 20 and counter_posicao == 20:
            for elements in elements_titulo:
                title = elements.text
                list_titulo.append(title)
                counter_titulos += 1
            for elements in elements_posicao:
                counter_posicao += 1
                list_posicao.append(elements.get_attribute("textContent"))
            for elements in elements_volume:
                list_volume.append(elements.get_attribute("textContent"))
                counter_volume += 1
            for elements in elements_autor:
                list_autores.append(elements.get_attribute("textContent"))
                counter_autores += 1
            for elements in elements_editora:
                list_editoras.append(elements.get_attribute("textContent"))
                counter_editora += 1
            for elements in elements_categoria:
                list_categoria.append(elements.get_attribute("textContent"))
                counter_categoria += 1
            for elements in elements_paginas:
                list_paginas.append(elements.get_attribute("textContent"))
                counter_paginas += 1
                list_data.append(data)
            for elements in elements_isbn:
                list_isbn.append(elements.get_attribute("textContent"))
                print(len(list_titulo))
                print(len(list_categoria))
                print(len(list_volume))
                print(len(list_isbn))
                print(len(list_autores))
                print(len(list_paginas))
                print(len(list_editoras))
                print(len(list_data))
                print('-------------------')

for i in list_isbn:
    string = i.split('ISBN')[1].split('-')
    isbn = ''.join(string).split(' ')[1]
    final_list_isbn.append(isbn)



publish_news_dict = {
        'titulo': list_titulo,
        'autor': list_autores,
        'editora': list_editoras,
        'categoria': list_categoria,
        'paginas': list_paginas,
        'isbn': final_list_isbn,
        'Volume': list_volume,
        'data': list_data,}

df = pd.DataFrame.from_dict(publish_news_dict, orient='columns', dtype=None)
print(df)
df.to_excel(r"C:\Users\duran\OneDrive\Desktop\jogos\DF_with_volume.xlsx")
