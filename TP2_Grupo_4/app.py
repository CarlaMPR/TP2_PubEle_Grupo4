from flask import Flask, render_template, request, redirect
import requests
import json
import db_reports

app = Flask(__name__)

# FRONTEND

# Rota que devolve a página incial (índice com todos os relatórios e funcionalidades)
@app.route('/')
def index():
	res = requests.get('http://localhost:5000/api')
	reports = json.loads(res.content)

	return render_template('index.html', reports=reports)

# Rota que devolve a página onde tem um formulário que permite adicionar um relatório
@app.route('/add', methods=['GET'])
def add():
	
	return render_template('add_view.html')    

# Ainda dentro da página anterior, permite fazer o POST do relatório
@app.route('/add', methods=['POST'])
def add_report():
	
	data = dict(request.form)
	requests.post('http://localhost:5000/api/add', data=data)
	
	return redirect('http://localhost:5000/')

# Rota que devolve a página para visualizar individualmente um relatório
@app.route('/<report>', methods=['GET'])
def get_report(report):
	
	res = requests.get('http://localhost:5000/api/'+report)
	r = json.loads(res.content)
	
	return render_template('report_view.html', r=r)

# Rota que devolve a página que permite eliminar um relatório
@app.route('/delete', methods=['GET'] )
def get_delete():
	
	res = requests.get('http://localhost:5000/api')
	reports = json.loads(res.content)
	
	return render_template('delete_view.html', reports=reports)

# Ainda dentro da página anterior, permite fazer o POST e efetivamente eliminar o relatório
@app.route('/delete', methods=['POST'] )
def delete_report():
	
	r = dict(request.form)
	requests.post('http://localhost:5000/api/delete', data=r)

	return redirect('http://localhost:5000/')

# Rota que devolve a página que permite procurar relatórios
@app.route('/search', methods=['GET'] )
def get_search_word():
	
	return render_template('search_view.html')

# Ainda dentro da página anterior, permite efetuar a procura por relatórios que contêm determinada palavra ou expressão (sequência de caracteres espaçados ou não)
@app.route('/search', methods=['POST'] )
def search_report():
	
	data = dict(request.form)
	res = requests.post('http://localhost:5000/api/search', data=data)
	r = json.loads(res.content)
	d = r.items()

	if len(r)==0:
		text="Não foram encontradas correspondências nos relatórios para: "+"'" +data['search']+"'."
	else:
		text="Relatórios encontrados com a(s) palavra(s): "+ "'" +data['search'] + "'."

	return render_template('search_view.html', dict_item = d, text=text)

# Permite editar um relatório, opção de editar presente na mesma página que permite visualizar o mesmo
@app.route('/<report>/edit', methods=['GET'])
def get_edit_report(report):
	
	res = requests.get('http://localhost:5000/api/'+report+'/edit')
	r = json.loads(res.content)

	return render_template('edit_view.html', report=r)

# Permite efetivar a edição do relatório
@app.route('/<report>/edit', methods=['POST'])
def edit_report(report):
	
	data=dict(request.form)
	requests.post('http://localhost:5000/api/add', data=data)
	
	return redirect('http://localhost:5000/'+report) 

# BACKEND

# Recorre à função find_all para retornar todos os relatórios existentes
@app.route('/api', methods=['GET'])
def api_get_reports():
	
	reports = db_reports.find_all()
	
	return json.dumps(reports)

# Permite o insert da informação preenchida no formulário, quer seja para inserir um novo relatório ou editar um já existente
@app.route('/api/add', methods=['POST'])
def api_post_report():
	
	data = dict(request.form)
	db_reports.insert(data)
	
	return json.dumps(db_reports.find_all())

# Recorre à função find_one para ver um relatório individual
@app.route('/api/<report>', methods=['GET'])
def api_get_report(report):	
	
	r = db_reports.find_one(report)
	
	return json.dumps(r)

# Recorre à função delete para remover um relatório da base de dados
@app.route('/api/delete', methods=['POST'])
def api_delete_report():
	
	r = dict(request.form)
	db_reports.delete(r)
	
	return json.dumps(db_reports.find_all())

# Recorre à função search para retornar todos os relatórios que contêm determinada palavra ou expressão (sequência de caracteres espaçados ou não)
@app.route('/api/search', methods=['POST'])
def api_search_report():
	
	data = dict(request.form)
	l = db_reports.search(data['search'])
	
	return json.dumps(l)

# Recorre à função find_one para ver um relatório e poder editá-lo
@app.route('/api/<report>/edit', methods=['GET'])
def api_get_edit_report(report):
	
	r = db_reports.find_one(report)
	
	return json.dumps(r)