#GERINGONÇA: ela mistura caracteres e usa indices negativos para inverter a atribuição de caractres as variaveis

characters=['t','a','c','o']

output=''
length=len(characters)
i=0
while(i<length):
	output=output+characters[i]
	i=i+1

#inverte o valor de length=4 para length=-4
length=length*-1
i=-2

#-2 é maior do que -4
while(i>=length):
	output=output+characters[i]
	i=i-1

print(output)	


#USANDO OUTROS CARACTERES:
characters=['w','a','s','i','t','a','r']

output=''
length=len(characters)
i=0
while(i<length):
	output=output+characters[i]
	i=i+1

#inverte o valor de length=4 para length=-4
length=length*-1
i=-2

#-2 é maior do que -4
while(i>=length):
	output=output+characters[i]
	i=i-1

print(output)


#USANDO OUTROS CARACTERES:
characters=['a','m','a','n','a','p','l','a','n','a','c']
output=''
length=len(characters)
i=0
while(i<length):
	output=output+characters[i]
	i=i+1

#inverte o valor de length=4 para length=-4
length=length*-1
i=-2

#-2 é maior do que -4
while(i>=length):
	output=output+characters[i]
	i=i-1

print(output)