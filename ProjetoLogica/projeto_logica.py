# manipulador = open('arquivo_texto.txt', 'a')
# cursos_desejados = []
# qtd_cursos = int(input('Informe quantos cursos você deseja realizar: '))
# for i in range(qtd_cursos):
#     curso_desejado = str(input('Informe o(s) curso(s) desejado(s): '))
#     cursos_desejados.append(curso_desejado)
#     x = ','.join(cursos_desejados)
# print(x)
# manipulador.write(f'\n{x}')
# manipulador.close()

manipulador_arquivo = open('arquivo_texto.txt', 'r')

print('Cursos cadastrados')
for i in manipulador_arquivo:
    i = i.rstrip()
    # print(i)
    if i == '#':
        break

manipulador_arquivo.seek(0)

cursos_cadastrados = ''

for linha in manipulador_arquivo:
    linha = linha.rstrip()
    print(linha)
    if '#' in linha:
        for linha in manipulador_arquivo:
            linha = linha.rstrip()
            cursos_cadastrados += linha + ' '

cursos_cadastrados = cursos_cadastrados.split(' ')
cursos_cadastrados.pop()
print(cursos_cadastrados)

# → ʌ
mesma_hora = ' → ¬mh'

for index, curso in enumerate(cursos_cadastrados):
    if len(cursos_cadastrados[index]) != 1:
        curso = curso.split(',')
        curso = '^'.join(curso)
        curso = curso + mesma_hora

    print(curso)

manipulador_arquivo.close()