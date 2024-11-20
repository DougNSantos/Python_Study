scores=[60,50,60,58,54,54,58,50,52,54]

ultimo=len(scores)
ver=scores[ultimo-1]
print(ver)

print("Lista completa:", scores)

#O PYTHON TEM UM SUPORTE PARA AO INVES DE USAR O MÉTODO ACIMA DE DIMINUIR -1 PARA ACESSAR O ULTIMO ITEM DA LISTA:
#ELE PODE USAR INDICES NEGATIVOS (-1,-2...) ASSIM ELE ACESSA OS INDICES AO CONTRÁRIO SENDO -1 O ÚLTIMO ITEM DE UMA LISTA E ASSIM POR DIANTE!
print("Lista ao contrário usando indices negativos do Python:")
print(scores[-1])
print(scores[-2])
print(scores[-3])

