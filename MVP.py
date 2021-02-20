import pandas as pd
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import Screen, ScreenManager
import mysql.connector


class TelaInicial(Screen):
    pass


class TelaFornecedores(Screen):
    def __init__(self, **kwargs):
        super(TelaFornecedores, self).__init__(**kwargs)

    def registrafornecedor(self, *args):
        mydb = mysql.connector.connect(host="bellateste.cy6ap9vbmbq6.us-east-2.rds.amazonaws.com",
                                       user="Brau2021", passwd="Revici159!",
                                       database="Bella")
        mycursor = mydb.cursor()
        query = "INSERT INTO fornecedores(fornecedor) VALUES (%s)"
        val = args
        mycursor.execute(query, val)
        mydb.commit()
        mydb.close()
        print(args)
        self.ids.cadastro_sucesso.text = 'Fornecedor Cadastrado Com Sucesso!'
        self.ids.nome_fornecedor.text = ''


class TelaCompras(Screen):

    def __init__(self, **kwargs):
        super(TelaCompras, self).__init__(**kwargs)

    def carregafornecedores(self):
        mydb = mysql.connector.connect(host="bellateste.cy6ap9vbmbq6.us-east-2.rds.amazonaws.com",
                                       user="Brau2021", passwd="Revici159!",
                                       database="Bella")
        lista = pd.read_sql_query('SELECT fornecedor FROM fornecedores', mydb)
        print(lista)
        mydb.commit()
        mydb.close()
        self.ids.spinner_fornecedores.values = [str(i) for i in lista['fornecedor']]


    def carregaprodutos(self):
        mydb = mysql.connector.connect(host="bellateste.cy6ap9vbmbq6.us-east-2.rds.amazonaws.com",
                                       user="Brau2021", passwd="Revici159!",
                                       database="Bella")
        lista = pd.read_sql_query('SELECT produto FROM produtos', mydb)
        print(lista)
        mydb.commit()
        mydb.close()
        self.ids.spinner_produtos.values = [str(i) for i in lista['produto']]


    def registracompra(self, *args):
        try:
            int(args[3])
            try:
                float(args[2])
                mydb = mysql.connector.connect(host="bellateste.cy6ap9vbmbq6.us-east-2.rds.amazonaws.com",
                                               user="Brau2021", passwd="Revici159!",
                                               database="Bella")
                mycursor = mydb.cursor()
                query = "INSERT INTO compras(fornecedor, produto, preço, quantidade, porte) VALUES (%s,%s,%s,%s,%s)"
                val = args
                mycursor.execute(query, val)
                mydb.commit()
                mydb.close()
                print(args)
                self.ids.compra_sucesso.text = "Compra Registrada Com Sucesso!"
                self.ids.preço_produto.text = ''
                self.ids.spinner_fornecedores.text = 'Selecione o Fornecedor'
                self.ids.spinner_produtos.text = 'Selecione o Produto'
                self.ids.quantidade_produto.text =''
                self.ids.spinner_porte.text = 'Selecione o Porte'

            except:
                self.ids.preço_produto.text = ''
                self.ids.preço_produto.hint_text = 'Preço Inválido'
        except:
            print("Quantidade inválida")


class TelaProdutos(Screen):

    def __init__(self, **kwargs):
        super(TelaProdutos, self).__init__(**kwargs)

    def registraproduto(self, *args):
        mydb = mysql.connector.connect(host="bellateste.cy6ap9vbmbq6.us-east-2.rds.amazonaws.com",
                                       user="Brau2021", passwd="Revici159!",
                                       database="Bella")
        mycursor = mydb.cursor()
        query = "INSERT INTO produtos(produto) VALUES (%s)"
        val = args
        mycursor.execute(query, val)
        mydb.commit()
        mydb.close()
        print(args)
        self.ids.cadastro_sucesso.text = 'Produto Cadastrado Com Sucesso!'
        self.ids.cadastro_sucesso.height = 100
        self.ids.cadastro_sucesso.width = 50
        self.ids.nome_produto.text = ''


class GerenciadorDeTelas(ScreenManager):
    pass


kv = Builder.load_file('Bella_MVP.kv')


class BellaSystem(App):
    def build(self):
        return kv


if __name__ == "__main__":
    BellaSystem().run()
