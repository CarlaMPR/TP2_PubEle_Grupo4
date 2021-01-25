# TP2_PubEle_Grupo4
TP2_PubEle_Grupo4

<b>Grupo 4:</b>
<p>Carla Rodrigues, A84710</p>
<p>Cláudia Palma, A85401</p>
<p>Eduarda Ribeiro, A8541</p>

<p>O presente trabalho prático consistiu na elaboração de uma aplicação FLASK que permite criar, ler, editar/atualizar e eliminar relatórios (<b>funções CRUD</b>). Foi usada a SHELVE <b>reports.db</b> e, separou-se o backend do frontend da aplicação, <b>ficheiro app.py.</p>

<p>No ficheiro <b>reports.db</b> foram criadas cinco funções:</p>
<ul>

  <p><b>find_all</b>: permite visualizar o título de todos os relatórios;</p>
  <p><b>find_one</b>: permite visualizar apenas um relatório;</p>
  <p><b>insert</b>: permite inserir um relatório na base de dados;</p>
  <p><b>delete</b>: permite eliminar um relatório da base de dados;</p>
  <p><b>search</b>: permite procurar todos os relatórios que tenham uma determinada palavra ou expressão (sequência de caracteres espaçados ou não), e ainda, retornar o excerto do relatório onde aparece a palavra/expressão em questão a negrito; de salientar que se trata de uma pesquisa case insensitive.</p>

</ul>

<p>No ficheiro <b>app.py</b> na parte do <b>FRONTEND</b> foram criadas dez rotas :</p>
<ul>

  <b>@app.route('/')</b>: rota que devolve a página incial (índice com todos os relatórios e funcionalidades);
  <b>@app.route('/add', methods=['GET'])</b>: rota que devolve a página onde tem um formulário que permite adicionar um relatório;
  <b>@app.route('/add', methods=['POST'])</b>: ainda dentro da página anterior, permite fazer o POST do relatório;
  <b>@app.route('/<report>', methods=['GET'])</b>: rota que devolve a página para visualizar individualmente um relatório;
  <b>@app.route('/delete', methods=['GET'])</b>: rota que devolve a página que permite eliminar um relatório;
  <b>@app.route('/delete', methods=['POST'])</b>: ainda dentro da página anterior, permite fazer o POST e efetivamente eliminar o relatório;
  <b>@app.route('/search', methods=['GET'])</b>: rota que devolve a página que permite procurar relatórios;
  <b>@app.route('/search', methods=['POST'])</b>: ainda dentro da página anterior, permite efetuar a procura por relatórios que contêm determinada palavra ou expressão (sequência de caracteres espaçados ou não);
  <b>@app.route('/<report>/edit', methods=['GET'])</b>: permite editar um relatório, opção de editar presente na mesma página que permite visualizar o mesmo;
  <b>@app.route('/<report>/edit', methods=['POST'])</b>: permite efetivar a edição do relatório

</ul>

<p>No ficheiro <b>app.py</b> na parte do <b>BACKEND</b> foram criadas seis rotas:</p>
<ul>

  <b>@app.route('/api', methods=['GET'])</b>: recorre à função find_all para retornar todos os relatórios existentes; 
  <b>@app.route('/api/add', methods=['POST'])</b>: permite o insert da informação preenchida no formulário, quer seja para inserir um novo relatório ou editar um já existente;
  <b>@app.route('/api/<report>', methods=['GET'])</b>: recorre à função find_one para ver um relatório individual;
  <b>@app.route('/api/delete', methods=['POST'])</b>: recorre à função delete para remover um relatório da base de dados;
  <b>@app.route('/api/search', methods=['POST'])</b>: recorre à função search para retornar todos os relatórios que contêm determinada palavra ou expressão (sequência de caracteres espaçados ou não);
  <b>@app.route('/api/<report>/edit', methods=['GET'])</b>: recorre à função find_one para ver um relatório e poder editá-lo;

</ul>

<p>Foram criados seis <b>templates</b>:</p>

<ul>

  <p><b>index</b>: template da página inicial que, apresenta a identificação do grupo de trabalho, a identificação dos docentes; um índice dos relatórios existentes na base de dados e, as funionalidade adicionar, eliminar e procurar;</p>
  <p><b>report_view</b>: template associado à visualização de um relatório;</p>
  <p><b>add_view</b>: template da página que contém o formulário para adicionar relatórios;</p>
  <p><b>edit_view</b>: template da página que contém o formulário para editar um relatórios;</p>
  <p><b>delete_view</b>: template da página que permite selecionar o relatório a eliminar;</p>
  <p><b>search_view</b>: template da página que permite procurar todos os relatórios que contêm a palavra ou expressão (sequência de caracteres espaçados ou não) inserida na barra de pesquisa;</p>

</ul>
