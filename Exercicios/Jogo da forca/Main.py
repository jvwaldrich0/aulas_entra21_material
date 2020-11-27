from Class.Forca import JogoForca

mesma_letra = []
condicional = True
vitoria = False
letra = '_'

jogo = JogoForca('teste.txt')

jogo.msg_start(jogo.tamanho_palavra)

print(jogo.soletrar(jogo.palavra))

while condicional:
    try:
        jogo.clear()
        letra = jogo.tratamento(
            input(f'\n{jogo.traco(letra)}\n\nDigite uma letra:\n> '),
            mesma_letra)
    except ValueError:
        print('Não é permitido número')
    except AttributeError:
        print('Digite apenas uma letra')
    except TypeError:
        print('Não repita a mesma letra')
    else:
        mesma_letra += [letra]
    finally:
        if vitoria:
            escolha = int(input('Digite 1 para repetir'))
            if escolha != 1:
                condicional = False
