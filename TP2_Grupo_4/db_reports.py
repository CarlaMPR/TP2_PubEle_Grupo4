import shelve
from re import *

# Função que permite ir buscar todos os relatórios
def find_all():
	with shelve.open('reports.db') as s:
		return list(s.keys())

# Função que permite ir buscar apenas um relatório
def find_one(report):
	with shelve.open('reports.db') as s:    
		return s[report]

# Função que permite inserir um relatório na base de dados 
def insert(report_data):
	with shelve.open('reports.db', writeback=True) as s:
		s[report_data['title']] = report_data
		return list(s.keys())

# Função que permite eliminar um relatório da base de dados
def delete(report):
    with shelve.open('reports.db', writeback=True) as s:
        del(s[report['report']])
        return list(s.keys())

# Função que permite procurar todos os relatórios que tenham uma determinada palavra ou expressão (sequência de caracteres espaçados ou não)
# Permite ainda, retornar o excerto do relatório onde aparece a palavra/ expressão em questão a negrito
# De salientar que se trata de uma pesquisa case insensitive
def search(word):
    with shelve.open('reports.db', writeback=True) as s:
        l=[]
        t=[]
        d={}
        for report, info in s.items():
            for key in info:
                text=info[key]
                matches = findall(rf"(?i){word}",text)
                if matches:
                    if report not in l:
                        l.append(report)
                        pos=text.index(matches[0])
                        if len(text)>=300:
                            t.append(text[pos:pos+len(matches[0])+300].replace(matches[0],'<b>'+matches[0]+'</b>'))
                        else:
                            t.append(text.replace(matches[0],'<b>'+matches[0]+'</b>'))
        for i in range(len(l)):
            for i in range(len(t)):
                d[l[i]]=t[i]
        return d

"""
Estrutura da BD: 

report_data={
    "title": "Java RMI", 
    "theme": "Redes",
    "authors": "Carla, Claudia, Eduarda",
    "date": 2020-12-12,
    "text": "Blah blah"
}

===>

s = {
    "Java RMI": {
    	"title":"Java RMI"
        "theme": "Redes"
        "authors": "Carla, Claudia, Eduarda",
        "date": 2020-12-12,
        "text": "Blah blah"
    },
    "DJango": {
        "title":"DJango"
        "theme": "Conexões"
        "authors": "Carla, Claudia, Eduarda",
        "date": 2020-10-13,
        "text": "Blah blah Blah"
    }
}
"""