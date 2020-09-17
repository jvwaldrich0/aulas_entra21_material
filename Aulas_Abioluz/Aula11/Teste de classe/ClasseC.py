from datetime import date

class cliente:
    def __init__(self, nome, idade, sexo, telefone):
        self.nome = str(nome).upper()
        self.idade = idade
        self.sexo = self.genre(sexo)
        self.telefone = telefone
    def genre(self,sexo):
        if sexo == 'M':
            return 'MASCULINO'
        elif sexo == 'F':
            return 'FEMININO'
        else:
            raise ValueError("Só aceita M ou F")
    def idade(self):
        today = date.today()
        print('Por gentileza, Informe sua data de nascimento;')
        while True:
            try:
                dia = int(input('Dia: '))
                mes = int(input('Mês: '))
                ano = int(input('Ano: '))
                nascimento = date(ano,mes,dia)
            except ValueError:
                print('Talvez você tenha digitado algo errado, Informe sua idade novamente por favor')
            else:
                return today.year - nascimento.year - ((today.month, today.day) < (nascimento.month, nascimento.day))