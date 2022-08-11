import os

SECRET_KEY= 'maria'


SQLALCHEMY_DATABASE_URI =\
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(SGBD='mysql+mysqlconnector',
    usuario='root',
    senha='',
    servidor='localhost',
    database='jogoteca')
#file faz referencia ao pripio arquivo
#os ajuda a achar
# essa variavel pega o caminho da pasta uploads
UPLOAD_PATH= os.path.dirname(os.path.abspath(__file__))+ '/uploads'