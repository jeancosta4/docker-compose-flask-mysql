from flask import Flask, request, jsonify, render_template, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Conexão com o banco de dados
db_config = {
    'user': 'root',
    'password': 'root',
    'host': 'db',
    'database': 'user'
}

@app.route('/', methods=['GET'])
def get_users():
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()
    query = "SELECT * FROM users"
    cursor.execute(query)
    users = cursor.fetchall()
    cursor.close()
    cnx.close()
    return jsonify([{'id': user[0], 'username': user[1], 'email': user[2]} for user in users])


@app.route('/cadastro', methods=['GET'])
def cadastro():
    return render_template('cadastro.html')

# Rota para processar o formulário de cadastro
@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form['username']
    email = request.form['email']
    #Conectar no Banco de Dados
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()

    # Inserir os dados no banco de dados
    sql = "INSERT INTO users (username, email) VALUES (%s, %s)"
    val = (nome, email)
    cursor.execute(sql, val)
    cursor.close()
    cnx.close()

    return redirect(url_for('cadastro'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
