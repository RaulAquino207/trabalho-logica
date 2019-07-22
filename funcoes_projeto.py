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
        print(valores)

    manipulador_arquivo.close()

def verificando_cursos(cursos_cadastrados):
    querem_um_e_dois = False
    querem_um_e_tres = False
    querem_um_e_quatro = False
    querem_dois_e_tres = False
    querem_dois_e_quatro = False
    querem_tres_e_quatro = False
    querem_todos = False

    if cursos_cadastrados == '1,2' or cursos_cadastrados == '2,1':
        querem_um_e_dois = True
    elif cursos_cadastrados == '1,3' or cursos_cadastrados == '3,1':
        querem_um_e_tres = True
    elif cursos_cadastrados == '1,4' or cursos_cadastrados == '4,1':
        querem_um_e_quatro = True
    elif cursos_cadastrados == '2,3' or cursos_cadastrados == '3,2':
        querem_dois_e_tres = True
    elif cursos_cadastrados == '2,4' or cursos_cadastrados == '4,2':
        querem_dois_e_quatro = True
    elif cursos_cadastrados == '3,4' or cursos_cadastrados == '4,3':
        querem_tres_e_quatro = True
    elif cursos_cadastrados == '1,2,3,4':
        querem_todos = True



