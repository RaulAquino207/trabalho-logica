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
    # print(cursos_cadastrados)

    # for valores in cursos_cadastrados:
    #     print(valores)

    verificando_cursos(cursos_cadastrados)

    manipulador_arquivo.close()

def verificando_cursos(cursos_cadastrados):
    querem_um_e_dois = False
    querem_um_e_tres = False
    querem_um_e_quatro = False
    querem_dois_e_tres = False
    querem_dois_e_quatro = False
    querem_tres_e_quatro = False
    querem_todos = False

    disponibilidade_horarios = []

    for index, valores in enumerate(cursos_cadastrados):

        if '1,2' in cursos_cadastrados[index] or '2,1' in cursos_cadastrados[index]:
            querem_um_e_dois = True
        if '1,3' in cursos_cadastrados[index] or '3,1' in cursos_cadastrados[index]:
            querem_um_e_tres = True
        if '1,4' in cursos_cadastrados[index] or '4,1' in cursos_cadastrados[index]:
            querem_um_e_quatro = True
        if '2,3' in cursos_cadastrados[index] or '3,2' in cursos_cadastrados[index]:
            querem_dois_e_tres = True
        if '2,4' in cursos_cadastrados[index] or '4,2' in cursos_cadastrados[index]:
            querem_dois_e_quatro = True
        if '3,4' in cursos_cadastrados[index] or '4,3' in cursos_cadastrados[index]:
            querem_tres_e_quatro = True
        if '1,2,3,4' in cursos_cadastrados[index]:
            querem_todos = True

    disponibilidade_horarios.append(querem_um_e_dois)
    disponibilidade_horarios.append(querem_um_e_tres)
    disponibilidade_horarios.append(querem_um_e_quatro)
    disponibilidade_horarios.append(querem_dois_e_tres)
    disponibilidade_horarios.append(querem_dois_e_quatro)
    disponibilidade_horarios.append(querem_tres_e_quatro)
    count_aux = 0

    for index , cursos in enumerate(disponibilidade_horarios):
        if disponibilidade_horarios[index] == True:
            count_aux += 1
    if count_aux == 6:
        print('Não é possivel oferecer 4 cursos em 3 horas')
    elif querem_todos == True:
        print('Não é possivel oferecer 4 cursos em 3 horas')
    else:
        print('Ainda é possivel oferecer os cursos 3 horas')

    # print(disponibilidade_horarios)



