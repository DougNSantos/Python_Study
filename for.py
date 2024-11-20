#usando o loop for em uma lista

smoothies=['coconut','strawberry','banana','tropical','açai berry']

#o loop for é um primo do while, mas é mais usado para iteraçoes, ja o while é mais usado para uma condição!
for smoothie in smoothies:
	output='Nós servimos ' + smoothie
	print(output)
#dessa forma, não precisamos cuidar do indice:
#no loop for, para cada vez que ele iterar, que ele percorer o loop, ele vai por um item da lista SMOOTHIES, na variavel criada na declaração do for SMOOTHIE
#assim podemos usar a variavel SMOOTHIE dentro do bloco do código for:	


#Há uma outra forma de usar o loop for, quando precisamos de intervalos de numeros:
teste=range(5) #a função range() cria um intervalo estipulado, por exemplo, range(5) cria uma sequencia de 0 a 4 pois ele começa do 0! tipo um indice
print(teste) #aqui, como estamos mostrando todo o valor da variavel teste, ele vai nos mostrar a sequencia conforme os intervalos

for i in range(5):
	print('iterando atraves de :', i) #aqui, como vamos mostrar a variavel i para cada iteração, ele vai nos mostrar o print de cada iteração e cada valor atribuida pela função range()

for i in range(len(smoothies)): #sendo mais conciso, reduzir código, deixar no essencial
	print('Smoothies:', smoothies[i])	


for i in range(len(smoothies)): 
	print('Smoothies #:',i, smoothies[i])

#OU SEJA, USANDO O FOR COM A FUNÇÃO RANGE(), NÃO PRECISAMOS DECLARAR UMA VARIAVEL i ANTES DOS LOOPS, ELE VAI SER CRIADO JUNTAMENTE COM O LAÇO FOR E ATRIBUIDO UM VALOR A ELE COM A FUNÇÃO RANGE()!
#DAÍ BASTA USARMOS ELE COMO VALOR PARA INDICE DE LISTAS, POR EXEMPLO	

#além dessas maneiras, podemos usar range() em intervalos:
range(5,10) #começa em 5 e vai até 10, sem contar o 10, ou seja: 5,6,7,8,9.
range(3,10,2) #o ultimo valor é um passo, o valor de incremento, então: 3,5,7,9. indo de passo 2 em 2
range(10,0,-1) #é contado de 10 até 0 decrementando em um passo de -1, então: 10,9,8,7,6,5,4,3,2,1.
range(-10,2) #começamos com um valor negativo, então: -10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1.

#então, na função range(), o ultimo valor não é contado. lembrar disto	