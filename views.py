
from flask_sqlalchemy import SQLAlchemy
from flask import Flask ,render_template,request,redirect,session,flash, url_for, send_from_directory
from jogoteca import app,db
from models import Jogos,Usuarios
from helpers import recupera_imagem
@app.route('/')
#index
def index():
    lista=Jogos.query.order_by(Jogos.id) # pega a class jogos com os dados do model banco /query procura eles/orden ordena eles por id
    return render_template('lista.html', titulo='Jogos',jogos= lista)

@app.route('/novo')
#novo
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=novo')
    return render_template('novo.html', titulo='Novo Jogo')
@app.route('/criar', methods=['POST',]) #rota que liga o formas a pagina inicio /adc methodo post para receber o forms sem da erro de rota
#criar
def criar():
    nome= request.form['nome'] #puxando as informações do forms 
    categoria= request.form['categoria']
    console= request.form['console'] 
    jogo= Jogos.query.filter_by(nome=nome).first()
    if jogo:
        flash('Jogo já existente!') #flash são mensagens rapidas que aparecem no navegador para seu funcionamento ele tem que receber um codigo pronto no html
        return redirect(url_for('index'))

    novo_jogo=Jogos(nome=nome, categoria=categoria, console=console)
    db.session.add(novo_jogo) #adc o jogo ao banco de dados
    db.session.commit() #salva a informação

    arquivo= request.files['arquivo'] #
    upload_path= app.config('UPLOAD_PATH')
    arquivo.save(f'{upload_path}/capa{novo_jogo.id}.jpg')


    return redirect('/')
#Editar
@app.route('/editar/<int:id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=editar')
    jogo=Jogos.query.filter_by(id=id).first()#first busca o primeiro 
    capa_jogo= recupera_imagem(id) # puxa a recuperação de imagem criada na pagina novo
    return render_template('editar.html', titulo='Editar Jogo',jogo=jogo, capa_jogo=capa_jogo)

#atualizar
@app.route('/atualizar', methods=['POST',]) #rota que liga o formas a pagina inicio /adc methodo post para receber o forms sem da erro de rota
def atualizar():
    jogo= Jogos.query.filter_by(id=request.form['id']).first()
    jogo.nome=request.form['nome']
    jogo.categoria=request.form['categoria']
    jogo.console =request.form['console'] #pega o que já foi escirto
    db.session.add(jogo)#adc e atualiza o jogo
    db.session.commit()

    arquivo= request.files['arquivo'] #
    upload_path= app.config('UPLOAD_PATH')
    arquivo.save(f'{upload_path}/capa{jogo.id}.jpg')

    return redirect(url_for('index'))
#deletar
@app.route('/deletar/<int:id>')
def deletar (id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login')
    jogo= Jogos.query.filter_by(id=id).delete
    db.session.commit()
    flash('Jogo deletado!')
    return redirect(url_for('index'))
    
@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima= proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    usuario=Usuarios.query.filter_by(nickname=request.form['usuario']).first() #first retorna o que foi pedido
    if usuario:
        if request.form['senha'] == usuario.senha:
             session['usuario_logado']= usuario.nickname
             flash(session['usuario_logado'] +' logado com sucesso!')
             proxima_pagina= request.form['proxima']
             return redirect('/{}'.format(proxima_pagina))

        else:
            flash('Usuário não logado :(')
            return redirect('/login')


@app.route('/logout')
def logout():
    session['usuario_logado']= None
    flash ('Usuário deslogado com sucesso!')
    return redirect(url_for('index'))
    
@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('uploads', nome_arquivo)


