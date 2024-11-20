#Código de um jogo pedra, papel e tesoura:

#OBS: Documentação é importante, usar no código também!

import random #importamos a lib random
#poderiamos usar o método random.choice com uma lista também

winner='' #iniciamos uma variavel string vazia. há outras formas de fazer isso também

user_choice=''
#usamos while para repetir trechos de códigos!
while (user_choice != 'pedra' and #podemos formatar no código os trechos para ficarem mais legiveis
    user_choice !='papel' and
    user_choice !='tesoura'): 
#usamos () na operação while quando usamos mais de uma expressao de comparação e devemos repetir toda a declaração para todas as comparações!    
   choice=input('Pedra, Papel ou Tesoura?')
   user_choice=choice.lower() #usando método de string para deixar tudo em minusculas   

   #então, as expressões while e if vão ser executadas enquanto tivermos um resultado booleano True!!!

random_choice=random.randint(0,2) #randint nos dara inteiros aleatórios entre 0 e 2
pc_choice=''
if random_choice == 0:
    pc_choice='pedra'
elif random_choice == 1:
    pc_choice='papel'
else:
    pc_choice='tesoura'

if user_choice==pc_choice:
    winner='empate'
    
elif pc_choice=='papel' and user_choice=='pedra': #analisamos apenas quando o pc ganha, depois apenas o usuario ganha
    winner='PC'    
elif pc_choice=='pedra' and user_choice=='tesoura':
    winner='PC'    
elif pc_choice=='tesoura' and user_choice=='papel':
    winner='PC'    
else:
    winner='usuário'

if winner=='empate':
    print('Os dois empataram')
else:    
    print('O ganhador foi: ' + winner + ', o pc escolheu: ' + pc_choice)        

# o WHILE enquanto a condição for verdadeira, será realizado o bloc de código do while.
# em nosso caso, o operador lógico AND vai precisar que todos os operando sejam True para que o resultado seja True e execute o bloco:
# como se o usuário digitar corretamente a palavra, um deles resultara em False, pois teremos dois verdadeiros e um false:
# e o operador AND não retornará True, mas sim False, encerrando o loop do while
# por isso usamos AND e não OR pois no OR o loop seria interminável            