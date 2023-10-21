#Lista 3 - exercício 1

idade = int(input('Bem vindo ao credencimaneto de atletas de natação que irão participar das eliminatórias para o próximo mundia. Para descobrir sua categoria, informe sua idade. '))
if idade <5:
    print('Infelizmente você ainda não possui idade o suficiente para participar.')
elif idade <7:
    print('Você pertence à categoria INFANTIL A.')
elif idade <11:
    print('Você pertence à categoria INFANTIL B.')
elif idade <14:
    print('Você pertence à categoria JUVENIL A.')
elif idade <18:
    print('Você pertence à categoria JUVENIL B.')
else:
    print('Você pertence à categoria SENIOR.')
