
from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)


# Função mock que retorna dados fictícios para testes
def get_mocked_pesquisas():
    return [
        {'id': 1, 'nome': 'Pesquisa de Mobilidade', 'data_inicio': '2023-09-01', 'data_fim': '2023-12-01'},
        {'id': 2, 'nome': 'Pesquisa de Compras', 'data_inicio': '2023-10-01', 'data_fim': '2023-11-01'},
        {'id': 3, 'nome': 'Pesquisa de Lazer', 'data_inicio': '2023-08-01', 'data_fim': '2023-09-01'}
    ]

pesquisas = get_mocked_pesquisas()

def get_mocked_entrevistados():
    # Retorna uma lista simulada de entrevistados usando dicionários
    return [
        {'id': 1, 'nome': 'João Silva', 'email': 'joao@gmail.com', 'data_nascimento': '1990-01-01'},
        {'id': 2, 'nome': 'Maria Oliveira', 'email': 'maria@gmail.com', 'data_nascimento': '1985-05-10'},
        {'id': 3, 'nome': 'Ana Souza', 'email': 'ana@gmail.com', 'data_nascimento': '1992-03-15'}
    ]

entrevistados = get_mocked_entrevistados()  # Carrega os dados simulados uma vez

# Função para conectar ao banco de dados
def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="dw_projetoilhaprimeira",
        user="postgres",
        password="admin",
        options="-c client_encoding=UTF8"
    )
    return conn

# Página inicial (Home)
@app.route('/')
def home():
    return render_template('home.html')

# Painel do Administrador
@app.route('/admin_dashboard')
def admin_dashboard():
    return render_template('admin_dashboard.html')

# Gerenciamento de Pesquisas
@app.route('/gerenciar_pesquisa')
def gerenciar_pesquisa():
    pesquisas = get_mocked_pesquisas()  # Usando função mock
    # conn = get_db_connection()
    # cur = conn.cursor()
    # cur.execute('SELECT * FROM pesquisa;')
    # pesquisas = cur.fetchall()
    # cur.close()
    # conn.close()
    return render_template('gerenciar_pesquisa.html', pesquisas=pesquisas)

# Adicionar nova pesquisa
@app.route('/adicionar_pesquisa', methods=('GET', 'POST'))
def adicionar_pesquisa():
    if request.method == 'POST':
        nome = request.form['nome']
        data_inicio = request.form['data_inicio']
        data_fim = request.form['data_fim']
        nova_pesquisa = {
            'id': len(pesquisas) + 1,
            'nome': nome,
            'data_inicio': data_inicio,
            'data_fim': data_fim
        }
        # conn = get_db_connection()
        # cur = conn.cursor()
        # cur.execute('INSERT INTO pesquisa (pesquisa_nome, data_inicio, data_fim) VALUES (%s, %s, %s)', (nome, data_inicio, data_fim))
        # conn.commit()
        # cur.close()
        # conn.close()
        pesquisas.append(nova_pesquisa)
        return redirect(url_for('gerenciar_pesquisa'))
    
    return render_template('adicionar_pesquisa.html')

@app.route('/editar_pesquisa/<int:id>', methods=('GET', 'POST'))
def editar_pesquisa(id):
    pesquisa = next((p for p in pesquisas if p['id'] == id), None)
    if not pesquisa:
        return "Pesquisa não encontrada", 404

    if request.method == 'POST':
        # Captura os dados enviados pelo formulário
        pesquisa['nome'] = request.form.get('nome')
        pesquisa['data_inicio'] = request.form.get('data_inicio')
        pesquisa['data_fim'] = request.form.get('data_fim')
        return redirect(url_for('gerenciar_pesquisa'))
    
    return render_template('editar_pesquisa.html', pesquisa=pesquisa)


@app.route('/remover_pesquisa/<int:id>', methods=['POST'])
def remover_pesquisa(id):
    global pesquisas
    pesquisas = [p for p in pesquisas if p['id'] != id]
    return redirect(url_for('gerenciar_pesquisa'))


# Gerenciamento de Entrevistados
@app.route('/gerenciar_entrevistado')
def gerenciar_entrevistado():
    entrevistados = get_mocked_entrevistados()
    # conn = get_db_connection()
    # cur = conn.cursor()
    # cur.execute('SELECT * FROM entrevistado;')
    # entrevistados = cur.fetchall()
    # cur.close()
    # conn.close()
    return render_template('gerenciar_entrevistado.html', entrevistados=entrevistados)

# Adicionar novo entrevistado
@app.route('/adicionar_entrevistado', methods=('GET', 'POST'))
def adicionar_entrevistado():
    global entrevistados
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        data_nascimento = request.form['data_nascimento']

        # Simula a adição de entrevistado à lista
        novo_entrevistado = {
            'id': len(entrevistados) + 1,
            'nome': nome,
            'email': email,
            'data_nascimento': data_nascimento
        }
        entrevistados.append(novo_entrevistado)
        # conn = get_db_connection()
        # cur = conn.cursor()
        # cur.execute('INSERT INTO entrevistado (nome, email, data_nascimento) VALUES (%s, %s, %s)', (nome, email, data_nascimento))
        # conn.commit()
        # cur.close()
        # conn.close()
        return redirect(url_for('gerenciar_entrevistado'))
    
    return render_template('adicionar_entrevistado.html')

@app.route('/editar_entrevistado/<int:id>', methods=('GET', 'POST'))
def editar_entrevistado(id):
    entrevistado = next((e for e in entrevistados if e['id'] == id), None)
    if not entrevistado:
        return "Entrevistado não encontrado", 404

    if request.method == 'POST':
        entrevistado['nome'] = request.form['nome']
        entrevistado['email'] = request.form['email']
        entrevistado['data_nascimento'] = request.form['data_nascimento']
        return redirect(url_for('gerenciar_entrevistado'))
    
    return render_template('editar_entrevistado.html', entrevistado=entrevistado)

@app.route('/remover_entrevistado/<int:id>', methods=['POST'])
def remover_entrevistado(id):
    global entrevistados
    entrevistados = [e for e in entrevistados if e['id'] != id]
    return redirect(url_for('gerenciar_entrevistado'))


if __name__ == '__main__':
    app.run(debug=True)
