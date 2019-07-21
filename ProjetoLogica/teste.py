def impl_free(clausula):
    if 'ʌ' in clausula:
        clausula = clausula.replace('ʌ','v')
    elif '→' in clausula:
        clausula = clausula.replace('→', 'v')
        negacao = '¬'
        clausula = clausula.split(' ')
        # print(clausula)
        clausula[0] = negacao + clausula[0]
        # print(clausula)
        clausula = ' '.join(clausula)

    print(clausula)

clausula1 = 'p1ʌp2ʌp3'
clausula2 = 'p1'
clausula3  = 'p2 → p1'
impl_free(clausula1)
impl_free(clausula2)
impl_free(clausula3)





