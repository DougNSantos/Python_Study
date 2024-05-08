import random

def starthero():

    hero1=random.randint(0,2)
    if hero1==0:
        hero1='mago'
    elif hero1==1:
        hero1='guerreiro'
    else:
        hero1='clérigo'

#    hero2=random.randint(0,2)
#    if hero2==0:
#        hero2='mago'
#    elif hero2==1:
#        hero2='guerreiro'
#    else:
#        hero2='clérigo'

#    hero3=random.randint(0,2)
#    if hero3==0:
#        hero3='mago'
#    elif hero3==1:
#        hero3='guerreiro'
#    else:
#        hero3='clérigo'

    return hero1

#DEVO INPLEMENTAR UM ALGORITMO DE HERO, POIS ASSIM DECLARO UMA VARIAVEL FORA DA FUNÇÃO PARA CADA HEROI QUE PRECISAR!!!

def startenemy():
    inimigo1=random.randint(0,2)
    if inimigo1==0:
        inimigo1='goblin'
    elif inimigo1==1:
        inimigo1='esqueleto'
    else:
        inimigo1='slime'
    return inimigo1    

user=input('Informe seu nome guerreiro:')
print(user,'vamos começar criando seu grupo de 3 aventurreiros')

champion1=starthero() 
champion2=starthero()
champion3=starthero()  
print('seu grupo será:',champion1,champion2,champion3)     

choice=input('Quer rolar os dados novamente? (y,n)')
while choice=='y':
    champion1=starthero() 
    champion2=starthero()
    champion3=starthero()
else:
    startenemy()     

print('Iniciamos a rolagem de inimigos, esta não pode ser rerolada...')
