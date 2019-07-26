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

    qtd_cursos = 0
    for linha in manipulador_arquivo:
        linha = linha.rstrip()
        if '#' in linha:
            break
        qtd_cursos += 1
    manipulador_arquivo.seek(0)
    cursos_cadastrados = ''
    for linha in manipulador_arquivo:
        if '#' in linha:
            for linha in manipulador_arquivo:
                linha = linha.rstrip()
                cursos_cadastrados += linha + ' '
                # print(linha)
    cursos_cadastrados = cursos_cadastrados.split(' ')
    cursos_cadastrados.pop()
    # print(cursos_cadastrados)

    verificando_cursos(cursos_cadastrados, qtd_cursos)

    manipulador_arquivo.close()

def verificando_cursos(cursos_cadastrados, qtd_cursos):
    querem_um_e_dois = False
    querem_um_e_tres = False
    querem_um_e_quatro = False
    querem_dois_e_tres = False
    querem_dois_e_quatro = False
    querem_tres_e_quatro = False
    querem_todos = False
    disponibilidade_horarios = []
    horarios_ainda_disponiveis = ['1,2','2,1','1,3','3,1','1,4','4,1','2,3','3,2','2,4','4,2','3,4','4,3']

    for index, valores in enumerate(cursos_cadastrados):

        if '1,2' in cursos_cadastrados[index] or '2,1' in cursos_cadastrados[index]:
            querem_um_e_dois = True
            horarios_ainda_disponiveis.remove('1,2')
            horarios_ainda_disponiveis.remove('2,1')

        if '1,3' in cursos_cadastrados[index] or '3,1' in cursos_cadastrados[index]:
            querem_um_e_tres = True
            horarios_ainda_disponiveis.remove('1,3')
            horarios_ainda_disponiveis.remove('3,1')

        if '1,4' in cursos_cadastrados[index] or '4,1' in cursos_cadastrados[index]:
            querem_um_e_quatro = True
            horarios_ainda_disponiveis.remove('1,4')
            horarios_ainda_disponiveis.remove('4,1')

        if '2,3' in cursos_cadastrados[index] or '3,2' in cursos_cadastrados[index]:
            querem_dois_e_tres = True
            horarios_ainda_disponiveis.remove('2,3')
            horarios_ainda_disponiveis.remove('3,2')

        if '2,4' in cursos_cadastrados[index] or '4,2' in cursos_cadastrados[index]:
            querem_dois_e_quatro = True
            horarios_ainda_disponiveis.remove('2,4')
            horarios_ainda_disponiveis.remove('4,2')

        if '3,4' in cursos_cadastrados[index] or '4,3' in cursos_cadastrados[index]:
            querem_tres_e_quatro = True
            horarios_ainda_disponiveis.remove('3,4')
            horarios_ainda_disponiveis.remove('4,3')

        if '1,2,3,4' in cursos_cadastrados[index]:
            querem_todos = True
        # print(horarios_ainda_disponiveis)

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
        print('\nNão é possivel oferecer {} cursos em 3 horas\n'.format(qtd_cursos))
    elif querem_todos == True:
        print('\nNão é possivel oferecer {} cursos em 3 horas\n'.format(qtd_cursos))
    else:
        print('\nAinda é possivel oferecer os {} cursos 3 horas\n'.format(qtd_cursos))
        print('Colocando os cursos {} na mesma hora'.format(horarios_ainda_disponiveis[::2]))
