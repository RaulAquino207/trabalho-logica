from funcoes_projeto import imprimir_cursos, cadastrar_cursos, analisar_satisfatibilidade
analisar_satisfatibilidade()
# validacao = True
# while(validacao):
#     imprimir_cursos()
#     print('')
#     print('Para cadastrar cursos digite 1\nPara sair digite 2')
#     op = int(input('Digite a opção desejada: '))
#     if op == 1:
#         cursos_desejados = []
#         qtd_cursos = int(input('Informe quantos cursos você deseja realizar: '))
#         if qtd_cursos == 4:
#             todos_os_cursos = '1,2,3,4'
#             cadastrar_cursos(todos_os_cursos)
#
#         elif qtd_cursos < 4 and qtd_cursos > 0:
#             for i in range(qtd_cursos):
#                 curso_desejado = input('Informe o(s) curso(s) desejado(s): ')
#                 cursos_desejados.append(curso_desejado)
#                 envio_arquivo = ','.join(cursos_desejados)
#             cadastrar_cursos(envio_arquivo)
#         else:
#             print('Quatidade de cursos inválida')
#     elif op == 2:
#         print('Obrigado!')
#         validacao = False
#     else:
#         print('Valor inválido digite novamente')
