
from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)


# Função mock que retorna dados fictícios para testes
def get_mocked_pesquisas():
    # Retorna uma lista simulada de pesquisas
    return [
        (1, 'Pesquisa de Mobilidade', '2023-09-01', '2023-12-31'),
        (2, 'Pesquisa de Compras', '2023-10-01', '2023-11-30'),
        (3, 'Pesquisa de Lazer', '2023-08-01', '2023-09-30')
    ]

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
        
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO pesquisa (pesquisa_nome, data_inicio, data_fim) VALUES (%s, %s, %s)', (nome, data_inicio, data_fim))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('gerenciar_pesquisa'))
    
    return render_template('adicionar_pesquisa.html')

# Gerenciamento de Entrevistados
@app.route('/gerenciar_entrevistado')
def gerenciar_entrevistado():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM entrevistado;')
    entrevistados = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('gerenciar_entrevistado.html', entrevistados=entrevistados)

# Adicionar novo entrevistado
@app.route('/adicionar_entrevistado', methods=('GET', 'POST'))
def adicionar_entrevistado():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        data_nascimento = request.form['data_nascimento']
        
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO entrevistado (nome, email, data_nascimento) VALUES (%s, %s, %s)', (nome, email, data_nascimento))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('gerenciar_entrevistado'))
    
    return render_template('adicionar_entrevistado.html')

if __name__ == '__main__':
    app.run(debug=True)
