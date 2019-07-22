def imprimir_cursos():

    manipulador_arquivo = open('arquivo_texto.txt', 'r')
    manipulador_arquivo.seek(0)
    print('{}Cursos ofertados{}'.format(6*'-',6*'-'))
    for linha in manipulador_arquivo:
        linha = linha.rstrip()
        if '#' in linha:
            break
        print('\t\t',linha)

    manipulador_arquivo.close()

def cadastrar_cursos(cursos):

    manipulador_arquivo = open('arquivo_texto.txt', 'a')
    manipulador_arquivo.write(f'\n{cursos}')
    manipulador_arquivo.close()
    print('Seus cursos foram cadastrados!')

def analisar_satisfatibilidade():

    manipulador_arquivo = open('arquivo_texto.txt', 'r')
    manipulador_arquivo.seek(0)
    cursos_cadastrados = ''
    for linha in manipulador_arquivo:
        if '#' in linha:
            for linha in manipulador_arquivo:
                linha = linha.rstrip()
                cursos_cadastrados += linha + ' '
                print(linha)
    cursos_cadastrados = cursos_cadastrados.split(' ')
    cursos_cadastrados.pop()
    print(cursos_cadastrados)

    for valores in cursos_cadastrados:

        if valores == '1,2' or valores == '1,2':
            print('OK')
        elif valores == '1,2' or valores == '1,2':
            print('OK')


    manipulador_arquivo.close()
