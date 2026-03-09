# #Ele serve para tentar executar um código que pode dar erro
# #Caso a tentativa no try dê errado, ele pula para o except 
# Imagine o Python lendo assim:

# 1️⃣ Tente executar isso
# 2️⃣ Se der erro
# 3️⃣ execute o except

import time

def soma(a,b):
    return a + b

while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o primeiro número: "))
        break
    except ValueError:
        print("Você digitou um valor inválido. Tente novamente em 5 segundos...")
        for i in range (5,0,-1):
            print(i)
            time.sleep(1)
            
def contagem():
    resultado = soma(num1,num2)
    print("-" * 30)
    print(f"\tO resultado da soma entre {num1}e {num2}\n\é {resultado}")
    print("-" * 30)
    
def main():
    contagem()
    
if __name__ == '__main__':
    main()