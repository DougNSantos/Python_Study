
#iteração para mostrar cada teste da lista usando condição while:
#i=0
#while(i<len(scores)): #aqui não precisamos usar len(scores)-1 pois estamos usando i<len(scores), assim que ele chegar ao total ele vai parar um antes do final, pois i< é diferente de <=!
	#print("Teste Bolha #: ",i+1," ,Score: ",scores[i])
	#i=i+1
#quando usamos , na função print() ele adiciona automaticamente um espaço extra. aqui tem uma forma de eliminar o espaço:
#solucao="solucao #" + str(i)   =a função str() transforma um inteiro em uma string, parecido com int(), assim podemos concatenar strings e eliminar o espaço extra
#podemos passar a função direto nos argumentos de print(), assim deixaremos nosso código mais conciso

#i=0
#while i < total:
#	print("Bolha #" + str(i+1), "Resultado:", scores[i])
#	i=i+1

	#quer dizer que a concatenação com + não adiciona espaço extra, ja a concatenação com , adiocona espaço extra
	#mas só podemos usar concatenação com + em dados de mesmo tipo, por isso da função str()

#descobrindo o valor mais alto:
#for i in range(len(scores)):
#	if scores[i] > high_score:
#		high_score=scores[i]

#print("Score mais alto:",high_score)	

scores=[60,50,60,58,54,54,58,50,52,54,48,69,34,55,51,52,44,51,69,64,66,55,52,61,46,31,57,52,44,18,41,53,55,61,51,44]

#total de teste feitos:
total=len(scores)

high_score=0

for i in range(len(scores)):
	print("Bolha #" + str(i+1), "Resultado:", scores[i])
	if scores[i] > high_score:
		high_score=scores[i]

print("Número total de scores:", total)	
print("Score mais alto:",high_score)
