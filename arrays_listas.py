#estudo sobre listas em python. Em outras liguagens gostam de chamar este tipo de dado estruturado como Arrays

scores=[60,50,60,58,54,54,58,50,52,54]
score=scores[3]
print(score)

#usando Strings(usamos aspas como Strings também):
smoothies = ['coconut','strawberry','banana','pinnaple','açai berry']

favorite = smoothies[2]

#mudando um dado da lista:
smoothies[2] = 'tropical'

print(smoothies)

#usando len() nos retorna o total de itens de uma lista.
#cuidar que ele traz o total, para usar como index que começa em 0 devemos diminuir -1 por exemplo.
tamanho_total=len(smoothies) #total=5

#ultimo index dessa lista
tamanho=len(smoothies)-1 #total para uso do index=4
item=smoothies[tamanho]
print(item)

#posso usar a subtração dentro dos colchetes também, dessa forma:
tam=len(smoothies)
last=smoothies[tam -1]
print(last)

#uma forma de acessar o ultimo indice:
lastSmoothie=len(smoothies)-1
print("último smoothie é: ", smoothies[lastSmoothie])
#a outra forma de acessar o ultimo indice:
print("Último smoothie é: ", smoothies[-1])