# #Faça um contador de palavras. O projeto deve receber uma frase do usuário e contar quantas vezes cada palavra aparece.
# #O split() em Python serve para quebrar uma string em várias partes.
# Normalmente usamos quando queremos separar palavras ou valores digitados pelo usuário.
import time

while True:
    try:
      frase = str(input("Digite a sua frase:").lower())
      if frase.strip() == "" or frase.isdigit():
          raise ValueError("Frase vazia ou valor inválido...")
      break
    except ValueError:
        print(f"A frase inserida {frase} é inválida! Tente novamente!")      
        continue

frase = frase.split()

i=0 

palavra = input("Digite a palavra que vc deseja pesquisar: ").lower()
for item in frase: #O item (variável temporária) irá percorrer a lista frase 
    if palavra == item:
        i+=1
        print(f"Percorrendo para verificar quantas vezes a palavra {palavra} aparece na sua frase...")
        time.sleep(2)
  
if i < 2:
    print(f"A palavra {palavra} aparece {i} vez na frase {frase}")
elif i > 2:
    print(f"A palavra {palavra} aparece {i} vezes na frase {frase}")
else:
    print(f"A palavra {palavra} não aparece na frase {frase}")

