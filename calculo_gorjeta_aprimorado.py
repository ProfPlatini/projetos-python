import time

while True:
    try:
        gorjeta = float(input("Insira o valor da porcentagem da sua gorjeta: "))
        break
    except ValueError:
        print(f"O valor inserido é inválido! Tente novamente em 5 segundos")
        for i in range (5,0,-1):
            print(i)
            time.sleep(1)
while True:
    try:
        conta = float(input("Insira o valor da sua conta total: "))
        break
    except ValueError:
        print(f"O valor inserido é inválido! Tente novamente em 5 segundos")
        for i in range (5,0,-1):
            print(i)
            time.sleep(1)
def calculo():
    return conta * (gorjeta/100)

def main():
    taxa = calculo()
    total = conta + taxa
    print("-" * 35)
    print(f"O valor da sua taxa é R${taxa:.2f}.") #Exibe as duas casas decimais
    print("-" * 35)
    print(f"O valor da sua conta total é R${total:.2f}.")
    print("-" * 35)
    
if __name__ == "__main__":
    main()

