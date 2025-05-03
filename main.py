#Um site onde você pode criar vagas e procurar vagas de emprego
#Ter como selecionar áreas como marketing, TI, etc.
#Fazer algo bonito, separando cada área em uma guia diferente, e colocando darkmode
from flask import Flask, render_template, request, redirect, flash, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
import json
from crypto import hash_password
import sqlite3

app= Flask(__name__)

users = {}
vagas = []

def carregar_vagas():
    with open("vagas.json", encoding="utf-8") as f:
        return json.load(f)
    #faz isso virar tipo uma lista ou dicionário

@app.route('/')
def index():
    vagas = carregar_vagas()
    busca = request.args.get('busca', '').lower()
    area = request.args.get('area', '')
    #Essas linhas pegam os valores dos filtros digitados pelo usuário na URL ou no formulário da página. 
    #(como um campo de busca ou um filtro de área).
    vagas_filtradas = [v for v in vagas if (busca.lower() in v['titulo'].lower() and (area == '' or v['area'] == area))]
    for vaga in vagas:
        if busca in vaga["titulo"].lower() and (area == "" or vaga["area"] == area):
                vagas_filtradas.append(vaga)

    password = "1212"  # Ensure password is a string
    hpassword = hash_password(password)
    print(hpassword)

    return render_template('index.html', vagas=vagas_filtradas, busca=busca, area=area, user=session.get('user'))
    

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        if username in users:
            return 'Usuário já existe!'
        users[username] = password
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and check_password_hash(users[username], password):
            session['user'] = username
            return redirect(url_for('index'))
        return 'Login inválido'
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)