#Programinha que simula um Phrase_o_Matic em Python:

#importa a lib random
import random

#cria a lista(array) para a frase
lista=['eu','posso','ola','teste','fada',5,'sereia','machine']

#atribui uma palavra da lista as variaveis usando random.choice(), pega um index da um array
palavra1=random.choice(lista)
palavra2=random.choice(lista)
palavra3=random.choice(lista)

#mostra no terminal o resultado da mistura de palavras
print(palavra1 , ' ' , palavra2 , ' ' , palavra3) 

# Obs: usamos ,(virgula) pois tem inteiro na lista[] (diferentes tipos de dados usados), 
# o +(mais) é apenas usado para concatenar Strings