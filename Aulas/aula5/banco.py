from veiculos import Pessoa

class Banco():
    def __init__(self):
        pass

class DataSaver():

    __arquivo_pessoa = "pessoas.txt"

    def __init__(self):
        pass

    def procurar_pessoa(self, cpf)-> Pessoa:
        try:
            #nome_arquivo = input('Nome do arquivo a ser editado:')
            arquivo = open(self.__arquivo_pessoa, 'r')
        except FileNotFoundError:
            print(u'Não há pessoas cadastradas!')
            return None
        for linha in arquivo:
            nome, idade, cpf = linha.split(";")
            p = Pessoa(nome, idade, cpf)
            return p

    def escrever_arquivo(self, nome_arquivo, conteudo_novo):
        try:
            #nome_arquivo = input('Nome do arquivo a ser editado:')
            arquivo = open(nome_arquivo, 'a')
        except FileNotFoundError:
            arquivo = open(nome_arquivo, 'a')
            print(u'Arquivo criado pois nao existia')
        arquivo.write(conteudo_novo + '\n')
        arquivo.close()
        return True

    def salvar_pessoa(self, pessoa):
        conteudo = f"{pessoa.nome};{pessoa.idade};{pessoa.cpf}"
        return self.escrever_arquivo(self.__arquivo_pessoa, conteudo)

class Conta():
    def __init__(self, banco:Banco, pessoa: Pessoa):
        pass


if __name__ == "__main__":
    data_saver = DataSaver()
    while True:
        valor = int(input(
            """Digite a operação desejada
            1 - Cadastrar Pessoa
            2 - Cadastrar Conta
            3 - Visualizar Saldo
            4 - Fazer um depósito
            5 - Procurar pessoa
            0 - Sair\n"""))

        if(valor == 1):
            print(data_saver.salvar_pessoa(Pessoa("Bruno", 29, "022.121.434-33")))

        if(valor == 5):
            print(data_saver.procurar_pessoa("022.121.434-33").nome)


        if(valor == 0):
            print("Agradecemos a sua visita!")
            break
