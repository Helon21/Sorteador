import random
from random import shuffle

quantidade_participantes = int(input("Informe a quantidade de participantes"))
nomes = []

for i in range(quantidade_participantes):
    inserirNome = input("Digite o nome do participante")
    nomes.append(inserirNome)

shuffle(nomes)
print("O participante sorteado foi.... música de suspense... {}".format(random.choice(nomes)))
