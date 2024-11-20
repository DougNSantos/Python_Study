#joguinho em terminal para o usuário descobrir a cor:

#iniciamos a variavel do tipo String
color='verde'

chute_cor='' #variavel iniciada vazia
tentativas=0

#quer dizer que toda vez que passar pelo while, vai ser atribuido um novo valor a variavel chute_cor!
while chute_cor != color:
    chute_cor=input('Qual cor estou pensando?')
    chute_cor.lower() #para validar, deixamos a String tudo em minusculas

    #incrementamos + 1 a variavel tentativas cada vez
    tentativas=tentativas+1

if tentativas == 1:
    print('Você acertou! teve ', tentativas , ' tentativa') 
else:
    print('Você acertou! teve ', tentativas , ' tentativas')        
