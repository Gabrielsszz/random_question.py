import random
Usuario = int(input('Digite:\n-1 para escolher pedra \n-2 para escolher tesoura \n-3 para escolher papel\n'))
while Usuario > 3 or Usuario <= 0:
      print('Erro, tente novamente!')
      Usuario = int(input('Digite:\n-1 para escolher pedra \n-2 para escolher tesoura \n-3 para escolher papel\n'))

opções = ['pedra','tesoura','papel']
escolha = opções[Usuario-1]
maq = 0
vencedor = 0
d=(random.randint(1,3))
maq = d

if Usuario == 1 and maq == 2 or Usuario == 2 and maq == 3 or Usuario == 3 and maq == 1:
    vencedor = 'usuario'
    print(f'Você escolheu {escolha} e o computador escolheu {opções[d-1]}. O {vencedor} venceu!')

elif Usuario == 1 and maq == 3 or Usuario == 2 and maq == 1 or Usuario == 3 and maq == 2:
    vencedor = 'computador'
    print(f'Você escolheu {escolha} e o computador escolheu {opções[d-1]}. O {vencedor} venceu!')

elif Usuario == maq:
    print(f'Você escolheu {escolha} e o computador escolheu {opções[d-1]}. Deu empate!')