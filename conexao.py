import mysql.connector
from mysql.connector import errorcode

class conexao:
    def __init__(self):
        
        self.db_connection = ""
        self.con = ""
        self.con = self.db_connection.cursor()

    def conectar(self):
        try:
            self.db_connection = mysql.connector.connect(host="localhost",user="root",password="",database="bancoFlask")

            return self.db_connection
        except mysql.connector.Error as erro:
            if erro.errno == errorcode.ER_BAD_DB_ERROR:
                print("Banco de Dados Não Existe!")
            elif erro.errno == errorcode.ER_ACESS_DENIED_ERROR:
                print("Usuario ou senha invalido!")
            else:
                print(erro)
        else:
            self.db_connection.close()
