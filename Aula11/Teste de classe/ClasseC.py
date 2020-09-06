class cliente:
    def __init__(self, nome, idade, sexo, telefone):
        self.nome = str(nome).upper()
        self.idade = idade
        self.sexo = sexo
        self.telefone = telefone
    def genre(self):
        while True:
            sexo = input('Sexo(M/F): ').upper()
            if sexo == 'M':
                return 'MASCULINO'
            elif sexo == 'F':
                return 'FEMININO'
            else:
                print('Sexo Inválido')
                continue
    def idade(self):
        from datetime import date
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