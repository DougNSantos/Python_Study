#um modelo de código mostrado no livro, baseado:
import random

winner='' #Aqui ,declaramos uma variavel vazia de Strings

pcItems=['pedra','papel','tesoura']
choice=random.choice(pcItems)

user=input('Escolha, pedra/papel/tesoura, apenas um: ')
    
#Diminuimos o número de declarações de if e else, pois pensamos no algoritmo e pseudocódigo, usando apenas um lado, assim ficou melhor
#OU SEJA, CONSIDERAMOS APENAS OS CASOS EM QUE O COMPUTADOR GANHA, ASSIM SABEMOS QUE O RESTO O USUÁRIO GANHA!!!
if choice == user:
    winner='EMPATE'
elif choice == 'pedra' and user == 'tesoura': #o AND aqui é um operador Booleana!!! vamos descobrir se é True ou False
    winner='COMPUTADOR'
elif choice == 'tesoura' and user == 'papel': #aqui ele junta duas expressões Boolenas para ver se é True ou False
    winner='COMPUTADOR' 
elif choice == 'papel' and user == 'pedra': #todo o conjunto de código desta linha acabou se tornando uma Expressão Booleana completa!!!
    winner='COMPUTADOR'
else:
    winner='USUÁRIO'   
#o espaço de um avanço normal, em python é de 4 espaços    
#print() adiciona um espaço em valores separados por vírgula. Por isso quando queremos pontuar, podemos usar a
#concatenação de valores com +

if winner == 'EMPATE':
    print('Nós dois escolhemos o mesmo, jogue novamente!')
else:    
    print(winner,'Ganhou! O computador escolheu:',choice,'e você escolheu:',user)