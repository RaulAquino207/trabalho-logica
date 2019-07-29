def imprimir_cursos():
    manipulador_arquivo = open('arquivo_texto.txt', 'r')
    manipulador_arquivo.seek(0)
    print('{}Cursos ofertados{}'.format(6 * '-', 6 * '-'))
    for linha in manipulador_arquivo:
        linha = linha.rstrip()
        if '#' in linha:
            break

        print('\t\t', linha)
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
    qtd_cursos_vetor = []

    for i in range(qtd_cursos):
        qtd_cursos_vetor.append(i + 1)
    # print(qtd_cursos_vetor)

    verificando_cursos(cursos_cadastrados, qtd_cursos_vetor, qtd_cursos)
    # print(qtd_cursos)

    manipulador_arquivo.close()


def retirando_cursos(valor, cursos_cadastrados, cursos_diponiveis, qtd_cursos):
    cursos = []
    cursos = cursos_diponiveis
    todos_os_cursos = []
    valor = str(valor)
    cursos_cadast = []
    # print(valor)
    if len(valor) == 3:
        aux1 = valor[0]
        aux2 = valor[2]
        valor_novo = aux2 + ',' + aux1
        # print(valor)
        # print(valor_novo)

        if cursos_diponiveis == []:
            return cursos_diponiveis

        elif valor in cursos_cadastrados or valor_novo in cursos_cadastrados:
            cursos.remove(valor)
            cursos.remove(valor_novo)
    elif len(valor) != 3:

        valor = valor.split(',')
        len_da_linha = len(valor)
        # print(valor)

        if cursos_diponiveis == []:
            return cursos_diponiveis
        else:

            for i, valores in enumerate(valor):
                # print(i)
                # print(valores)
                aux = ''
                if i == len(valor):
                    break
                # print(valor)

                for index in range(len(valor)):
                    aux = valor[i] + ',' + valor[index]
                    cursos_cadast.append(aux)

            for index in range(len(cursos_cadast)):
                valores_removidos = cursos_cadast[::len_da_linha + 1]
                # print(valores_removidos)

            for i in valores_removidos:
                cursos_cadast.remove(i)
            # print(cursos_cadast)
            for index, remv in enumerate(cursos_cadast):
                # print(remv)
                if remv in cursos:
                    cursos.remove(remv)

    return cursos_diponiveis


def verificando_cursos(cursos_cadastrados, qtd_cursos_vetor, qtd_cursos):
    horarios_ainda_disponiveis = []

    for index, valores in enumerate(qtd_cursos_vetor):
        qtd_cursos_vetor[index] = str(qtd_cursos_vetor[index])

    # print(qtd_cursos_vetor)

    for i, valor in enumerate(qtd_cursos_vetor):
        aux = ''
        if i == len(qtd_cursos_vetor):
            break

        for index in range(len(qtd_cursos_vetor)):
            aux = qtd_cursos_vetor[i] + ',' + qtd_cursos_vetor[index]
            horarios_ainda_disponiveis.append(aux)

    for index in range(len(horarios_ainda_disponiveis)):
        valores_removidos = horarios_ainda_disponiveis[::qtd_cursos + 1]
        # print(valores_removidos)

    for i in valores_removidos:
        horarios_ainda_disponiveis.remove(i)

    # print(horarios_ainda_disponiveis)

    for index, valores in enumerate(cursos_cadastrados):
        # print(valores)
        horarios_ainda_disponiveis = retirando_cursos(valores, cursos_cadastrados, horarios_ainda_disponiveis,
                                                      qtd_cursos)
    # print(horarios_ainda_disponiveis)
    for i, valor in enumerate(horarios_ainda_disponiveis):
        # print(i)
        # print(valor)
        aux1 = valor[0]
        aux2 = valor[2]
        valor_novo = aux2 + ',' + aux1
        if valor_novo in horarios_ainda_disponiveis:
            horarios_ainda_disponiveis.remove(valor_novo)

    # print(horarios_ainda_disponiveis)

    if horarios_ainda_disponiveis == []:
        print('\nNão é possivel oferecer {} cursos em 3 horas\n'.format(qtd_cursos))
    else:
        print('\nAinda é possivel oferecer os {} cursos 3 horas\n'.format(qtd_cursos))
        print('Colocando os cursos {} na mesma hora'.format(horarios_ainda_disponiveis))
