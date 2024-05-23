from flask import Blueprint, render_template, request, flash, redirect, session
from databases.models.usuario import usuario
import bcrypt
import time
home_route = Blueprint("home", __name__)
'''Formulário login (POST) user, senha'''
'''Formulário Cadastro (POST) user, email, senha'''

@home_route.route('/')
def home():
    if 'logado' in session and session['logado'] is True:
        pass
    else:
        flash('Faça o login para acessar a pagina', 'error')
        return redirect('/login')
    return render_template("index.html")

@home_route.route('/login', methods=['GET','POST'])
def login_page():
    if 'logado' in session and session['logado']:
        return redirect('/')
    return render_template('login.html')


@home_route.route('/logar',methods=['POST'])
def logar():
    email = request.form['user']
    senha = request.form['pass']
    try:
        # Verifica se o usuário existe pelo e-mail.
        usuario_consulta = usuario.get(usuario.email == email)
        print(senha.encode('utf-8'),usuario_consulta.senha.encode('utf-8'))

        # Verifica a senha (em produção, use hash de senha).
        if bcrypt.checkpw(senha.encode('utf-8'), usuario_consulta.senha.encode('utf-8')):
            flash('Usuário logado com sucesso', 'success')
            session['logado'] = True
            return redirect('/')
        else:
            flash('Dados incorretos', 'error')
            return redirect('/login')
    except:
        flash('Usuário não encontrado', 'error')
        return redirect('/login')


@home_route.route('/cadastro', methods=['GET','POST'])
def form_cadastro():
    return render_template('cadastro.html') 

@home_route.route('/cadastrar', methods=['POST'])
def cadastrar():
    senha = ""
    nome = request.form['user']
    email = request.form['email']
    pass1 = request.form['pass1']
    pass2 = request.form['pass2']
    if pass1 is not None and pass2 is not None:
        if pass1 == pass2:
            hashed_senha = bcrypt.hashpw(pass1.encode('utf-8'), bcrypt.gensalt())
            flash('Cadastrado com sucesso','success')
            novo_usuario = usuario.create(
                nome=nome,
                email=email,
                senha=hashed_senha.decode('utf-8')
            )
            return redirect('/cadastro')
        else:
            flash('As senhas não são iguais','error')
            return redirect('/cadastro')
    
    return render_template('cadastro.html')
    

