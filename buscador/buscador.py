import scholarly

class Articulo():
    abstract = ""
    author = ""
    title = ""
    url = ""
    source = "" 

papers = Articulo()
#valor = 'covid-19'
valor = input("Ingresa un tema de tu interés: ")
buscar_articulo = scholarly.search_pubs_query(valor)
articulos = []

for i in range(0,3):
    papers.title = next(buscar_articulo).bib['title']
    papers.abstract = next(buscar_articulo).bib['abstract']
    papers.author = next(buscar_articulo).bib['author']
    papers.url = next(buscar_articulo).bib['url']
    papers.source = next(buscar_articulo).source

    print("\n","Título:",papers.title)
    print("Resumen:",papers.abstract)
    print("Autor:",papers.author)
    print("URL:",papers.url)
    print("Fuente:",papers.source)
    print("-----------------------------------","\n")
"""
    articulos.insert(i+1,papers)#metodo 2
    #print(i,articulos[i].title)

for j in range(0,3):#metodo 2
    print("Título:",articulos[j].title,"\n")
    print("Resumen:",articulos[j].abstract,"\n")
    print("Autor:",articulos[j].author,"\n")
    print("URL:",articulos[j].url,"\n")
    print("Fuente:",articulos[j].source,"\n")
    print("-----------------------------------","\n")
""" 