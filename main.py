from flask import Flask, render_template, request
from model import model
import this
this.nome = ""
this.telefone = ""
this.endereco = ""
this.data = ""
this.dados = ""
this.modelo = model()


pessoa = Flask(__name__)

@pessoa.route('/', methods=['GET','POST'])
def cadastrar():
    if request.method == 'POST':
        this.nome     = request.form['tNovoNome']
        this.Telefone = request.form['tNovoTelefone']
        this.endereco = request.form['tNovoEndereco']
        this.data     = request.form['tNovaData']
        this.dados    = this.modelo.inserir(this.nome,this.telefone,this.endereco,this.data)
    return render_template('index.html',titulo="Pagina Principal", resultado=this.dados) 

if __name__ == '__main__':
    pessoa.run(debug=True,port=5000)