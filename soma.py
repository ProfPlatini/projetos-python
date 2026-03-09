import time

def somar (a,b):
    return a + b 

while True:
    num1 = input("Digite o primeiro número da soma: ")
    num2 = input("Digite o segundo número da soma: ")

    if num1.isdigit() and num2.isdigit():
        print("Números inseridos válidos")
        num1 = float(num1)
        num2 = float(num2)
        break
    else:
        print("Você digitou um número inválido. Tentativa de login atrasada em 5 segundos")
        for i in range (5,0,-1):
            print(i)
            time.sleep(1)
            continue
def main():
    resultado = (somar(num1, num2))
    print("-" * 35)
    print(f"O resultado da sua soma é: {resultado}")
    print("-" * 35)
    
if __name__ == "__main__":
    main()
        
        
    