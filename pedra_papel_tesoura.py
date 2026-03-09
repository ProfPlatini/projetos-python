import random
import time

def jogo():
    while True:
        opcoes = ["pedra" , "papel" , "tesoura"]
        computador = random.choice(opcoes)
        usuario = input("Escolha a sua opção: ").lower()
        if usuario not in opcoes:
            print("Opção inválida, escolha novamente!") 
            continue
        else: 
            print("Opção válida!")
            break
    if usuario == computador:
        print("-" * 30)
        print(f"Você escolheu {usuario} e o computador escolheu {computador}!")
        print("-" * 30)
        print("... Calculando resultado ... ")
        time.sleep(5)
        print(" 😐 EMPATE! 😐")
    if usuario == "tesoura" and computador == "papel" or usuario == "papel" and computador == "pedra" or usuario  == "tesoura" and computador == "papel":
        print("-" * 30)
        print(f"Você escolheu {usuario} e o computador escolheu {computador}!")
        print("-" * 30)
        print("... Calculando resultado ... ")
        time.sleep(5)
        print(" 🏅 VITÓRIA! 🏅")
    else:
        print("-" * 30)
        print(f"Você escolheu {usuario} e o computador escolheu {computador}!")
        print("-" * 30)
        print("... Calculando resultado ... ")
        time.sleep(5)
        print("❌ DERROTA ❌!")
        
def main():
    jogo()
    
if __name__ == '__main__':
    main()