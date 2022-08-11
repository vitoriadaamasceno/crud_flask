from flask_sqlalchemy import SQLAlchemy
from flask import Flask 



app= Flask(__name__)
app.config.from_pyfile('config.py')#from_pyfile puxa informação dessa pagina
db=SQLAlchemy(app)
#run
from views import *
if __name__=='__main__':#garante que vai rodar todas as pastas e aplicações
    app.run(debug=True)