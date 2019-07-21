def impl_free(alguma_coisa):
    if alguma_coisa == 'atomo':
        return alguma_coisa
    elif alguma_coisa == 'clausula negada':
        return impl_free(alguma_coisa)
    elif '^' in alguma_coisa:
        alguma_coisa.split('^')


        return impl_free(alguma_coisa) and impl_free(alguma_coisa)