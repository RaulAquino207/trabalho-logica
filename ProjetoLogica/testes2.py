def impl_free(proposicao):
    if '^' in proposicao:
        atomos = proposicao.split('^')
        print(f'Entrou pro if do ^: {atomos}')
        return impl_free(atomos[0]) + '^' + impl_free(atomos[1])
    elif 'v' in proposicao:
        atomos = proposicao.split('v')
        print(f'Entrou pro if do v: {atomos}')
        return impl_free(atomos[0]) + '^' + impl_free(atomos[1])
    elif len(proposicao) == 1:
        return proposicao


def funcao(proposicao):
    if '^' in proposicao:
        atomos = proposicao.split('^')
        retorno = ''

        for valor in atomos:
            retorno += f'funcao({valor})^'

        return retorno

proposicao = 'pvq^r'
atomos = proposicao.split(' ^ ')

print('-= ' * 10)

print(f'Resultado final: {funcao(proposicao)}')



