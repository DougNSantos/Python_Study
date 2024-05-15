import random

#OUTRA MANEIRA, USANDO AGORA A FUNÇÃO random.choice, para escolher um item aleatório de uma lista!

pcItems=['pedra','papel','tesoura']
choice=random.choice(pcItems)

user=input('Escolha, pedra/papel/tesoura, apenas um: ')

if choice == user:
    print('Deu empate!')
elif choice == 'pedra' and user == 'tesoura':
    print('Pc escolheu ',choice,', você perdeu')
elif choice == 'pedra' and user == 'papel':
    print('Pc escolheu ',choice,', você venceu') 
elif choice == 'tesoura' and user == 'papel':
    print('Pc escolheu ',choice,', você perdeu')  
elif choice == 'tesoura' and user == 'pedra':
    print('Pc escolheu ',choice,', você venceu')
elif choice == 'papel' and user == 'pedra':
    print('Pc escolheu ',choice,', você perdeu')
elif choice == 'papel' and user == 'tesoura':
    print('Pc escolheu ',choice,', você venceu')  
else:
    print('Escolha errada, rode o programa novamente!!!')          

#RANDOM.CHOICE() PEGA UM ITEM ALEATÓRIO DE UMA LISTA
#RANDOM.RANDINT() PEGA UM NÚMERO ALEATÓRIO DENTRE OS ESTIPULADOS NOS PARÂMETROS DE ENTRADA DELE    
