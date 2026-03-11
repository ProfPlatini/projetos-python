import random 

duplas = [
    "Dupla 1: João ²",
    "Dupla 2: Kauan e Gabriel",
    "Dupla 3: Eloyse e Camila",
    "Dupla 4: Antonio e Emily",
    "Dupla 5: Jean e Kaynã",
    "Dupla 6 : Josias e André",
    "Dupla 7: Guilherme e Bruno",
    "Dupla 8: Diego e Leo",
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
    print(f"Dupla {dupla} -------> {cenario}")