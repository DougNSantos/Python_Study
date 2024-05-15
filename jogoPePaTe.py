import random

numeroPc=random.randint(0,2)
escolhaPc='nenhum'

#ao inves de usar uma variavel para guardar o nome, posso usar direto os numeros gerados pela variavel escolhaPc direto, fica menor o código!

if numeroPc == 0:
    escolhaPc='PEDRA'
elif numeroPc == 1:
    escolhaPc='PAPEL'
else:
    escolhaPc='TESOURA'

suaEscolha=input('digite sua escolha entre PEDRA, PAPEL ou TESOURA:')

if escolhaPc == suaEscolha:
    print('Deu empate!')
elif escolhaPc == 'PEDRA' and suaEscolha == 'TESOURA':
    print('Pc escolheu ',escolhaPc,', você perdeu')
elif escolhaPc == 'PEDRA' and suaEscolha == 'PAPEL':
    print('Pc escolheu ',escolhaPc,', você venceu') 
elif escolhaPc == 'TESOURA' and suaEscolha == 'PAPEL':
    print('Pc escolheu ',escolhaPc,', você perdeu')  
elif escolhaPc == 'TESOURA' and suaEscolha == 'PEDRA':
    print('Pc escolheu ',escolhaPc,', você venceu')
elif escolhaPc == 'PAPEL' and suaEscolha == 'PEDRA':
    print('Pc escolheu ',escolhaPc,', você perdeu')
elif escolhaPc == 'PAPEL' and suaEscolha == 'TESOURA':
    print('Pc escolheu ',escolhaPc,', você venceu')  
else:
    print('Escolha errada, rode o programa novamente!!!')          
