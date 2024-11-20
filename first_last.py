#código teste que inverte valores entre variaveis:

first='first'
last='last'
print(first + " e " + last)
temp=last #usamos uma variavel temporaria para gravar o valor de last e depois atribuir ele ao first e inverter!
last=first
first=temp
print(first + " e " + last)
