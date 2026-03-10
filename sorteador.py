import random 

duplas = [
    "Dupla 1",
    "Dupla 2",
    "Dupla 3",
    "Dupla 4",
    "Dupla 5",
    "Dupla 6",
    "Dupla 7",
    "Dupla 8",
]

cenarios = [
    "Cenário 1",
    "Cenário 2",
    "Cenário 3",
    "Cenário 4",
    "Cenário 5",
    "Cenário 6",
    "Cenário 7",
    "Cenário 8",
]

random.shuffle(cenarios)

for dupla,cenario in zip(duplas,cenarios):
    print(f"Dupla {dupla} -> {cenario}")
    
#------------------------------------------------------#
import random 

duplas = [
    "Dupla 1",
    "Dupla 2",
    "Dupla 3",
    "Dupla 4",
    "Dupla 5",
    "Dupla 6",
    "Dupla 7",
    "Dupla 8",
]

cenarios = [
    "Cenário 1",
    "Cenário 2",
    "Cenário 3",
    "Cenário 4",
    "Cenário 5",
    "Cenário 6",
    "Cenário 7",
    "Cenário 8",
]

for dupla, cenario in zip(duplas,cenarios):
    print(f"Dupla {dupla} -----> {cenario}")
    
    # print(list(zip(duplas,cenarios)))