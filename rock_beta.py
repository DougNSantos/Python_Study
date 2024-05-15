#código do jogo documentado:
import random

winner='' 

pcItems=['pedra','papel','tesoura']
choice=random.choice(pcItems)

user=input('Escolha, pedra/papel/tesoura, apenas um: ')

if choice == user:
    winner='EMPATE'
elif choice == 'pedra' and user == 'tesoura': 
    winner='COMPUTADOR'
elif choice == 'tesoura' and user == 'papel': 
    winner='COMPUTADOR' 
elif choice == 'papel' and user == 'pedra':
    winner='COMPUTADOR'
else:
    winner='USUÁRIO'   

if winner == 'EMPATE':
    print('Nós dois escolhemos o mesmo, jogue novamente!')
else:    
    print(winner,'Ganhou! O computador escolheu:',choice,'e você escolheu:',user)