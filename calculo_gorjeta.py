# Para agilizar o processo, João quer um programa que receba o valor total da conta e a porcentagem de gorjeta desejada e exiba o valor final que o cliente deverá pagar.

# Crie um programa que peça ao usuário o valor da conta e a porcentagem de gorjeta. O programa deve calcular e exibir o valor da gorjeta e o total a ser pago.
import time
while True:
    try:
        gorjeta = input("Digite a taxa da gorjeta em porcentagem: ")
        if not gorjeta.isdigit():
            raise ValueError #Aqui eu estou forçando o erro ... 
        else:
            gorjeta = int(gorjeta)
        break
    except ValueError:
        print("Você digitou um valor inválido, tente novamente em ")
        for i in range (5,0,-1):
            print(i)
            time.sleep(1)

while True:
    try:
        conta =(input("Digite o valor conta: "))
        if not conta.isdigit():
            raise ValueError #Aqui eu estou forçando o erro ... 
        else:
            conta = int(conta)
        break
    except ValueError:
        print("Você digitou um valor inválido, tente novamente em ")
        for i in range (5,0,-1):
            print(i)
            time.sleep(1)
def calculo():
    return conta * (gorjeta/100)

def main():
    taxa = (calculo())
    print("-" * 30)
    print(f"O valor da sua taxa de garçom é R${taxa}")
    print("-" * 30)
    print(f"O valor final da sua conta, considerando a taxa inclusa, fica em R${taxa + conta}")
    
    
if __name__ == '__main__':
    main()


#Como ponto de melhoria aqui, eu colocaria duas casas decimais no valor e também vou dar a opção de inserir taxas decimais (float).... 