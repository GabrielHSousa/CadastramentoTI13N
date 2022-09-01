from conexao import conexao

class model:
    def __init__(self):
        self.conex = conexao()
        self.conex.conectar()

    def inserir(self,nome,telefone,endereco,dataDeNascimento):
        try:
            sql="insert into person(codigo,nome,telefone,endereco,dataDeNascimento) values('','{}','{}','{}','{}')".format(nome,telefone,endereco,dataDeNascimento)
            self.conex.execute(sql)
            self.conex.commit()
            return "{} Inserido".format(self.conex.rowcount)
        except Exception as erro:
            return erro

    def consultar(self,codigo):
        try:
            sql = "select * from person where codigo = '{}'".format(codigo)
            self.conex.execute(sql)

            for(codigo,nome,telefone,endereco,dataDeNascimento) in self.conex:
                msg = msg + "\nCodigo: {}, Nome: {},Telefone:{},Endereco {},Nascimento{}".format(codigo,nome,telefone,endereco,dataDeNascimento)
                return msg 
            except Exception as erro:
                return erro