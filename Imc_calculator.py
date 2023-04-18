# Caculadora de Imc

print('--------Sistema 2.0--------')
print()
print()
print()
print()

print('Digite Sim ou Não')
iniciar = input('Quer ligar o sistema ?')


if (iniciar == 'Sim' and 'sim' and 's' and 'Quero' and 'Yes'):

    print('Vamos calcular o seu Imc')

    nome = input('Qual seu nome ?')

    idade = int(input('Qual sua idade ?'))

    peso = int(input('Qual seu peso ?'))

    altura = float(input('Qual sua altura em metros ?'))

    calculo = peso // (altura * altura)

    imc = (
        f'O Seu nome é {nome} você tem {idade} anos, pesa {peso:.2f} kg e tem {altura: .2f} de altura seu Imc é: {calculo}')

    print(imc)

else:
    print('Saindo do sistema')

muitoAbaixoDoPeso = 17
abaixoDoPeso = (17, 18.49)
pesoNormal = (18.5, 22.5)
acimaDoPeso = (25, 29.99)
obesidadeUm = (30, 34.99)
obesidadeDoisSevera = (35, 39.99)
obesidadeTresMorbida = 40

if (imc == muitoAbaixoDoPeso):
    print('Situação: Muito abaixo do peso')
    print('Procure aumentar o consumo de comida rica em fibras e carboidratos e beba agua.')

elif (imc == abaixoDoPeso):
    print('Situação: Abaixo do peso')
    print('Regule um pouco melhor sua dieta, desnutrição é prejudicial.')

elif (imc == pesoNormal):
    print('Situação: Peso normal')
    print('Ótimo mantenha seu peso assim, mas não deixe de fazer exercícios e ir ao médico todo ano.')

elif (imc == acimaDoPeso):
    print('Situação: Acima do peso')
    print('Procure diminuir os carboidratos, principalmente os ruins e pratique mais esportes.')

elif (imc == obesidadeUm):
    print('Situação: Obesidade I')
    print('Sua obesidade já está em grau I, tome cuidado gordura é prejudicial a saúde e causa infarto.')

elif (imc == obesidadeDoisSevera):
    print('Situação: Obesidade II Severa ')
    print('Procure ajuda de um profissional que possa lhe ajudar a regular oque você come e passar exercícios antes que seja tarde.')

elif (imc == obesidadeTresMorbida):
    print('Situação: Obesidade grau III Morbida ')
    print(f'Procure ajuda urgente {nome} !!')
