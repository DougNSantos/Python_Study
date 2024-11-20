#Código que calcula idade canina:

dog_name=input('Qual o nome de seu dog?')
dog_age=input('Qual a idade do '+ dog_name + '?')

#devemos transformar a String do input(por padrão ele recebe tudo como String) e deixá-lo como inteiro para multipicarmos por 7
human_age=int(dog_age)*7 #senão ele só multiplicaria a mensagem em String 7 vezes (repetiria a mensagem)
print('A idade de ' + dog_name + 'em anos humanos é de: ',human_age)

#dependendo da concatenação, usamos + ou , em python
#quando queremos concatenar Strings, usamos +, quando queremos concatenar inteiros ou outros tipos, usamos ,(virgula)
