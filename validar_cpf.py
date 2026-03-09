# Carlos trabalha em um cartório e precisa validar se um CPF informado pelo cliente tem o formato correto antes de prosseguir com o atendimento. O CPF deve conter exatamente 11 dígitos numéricos. Se a entrada contiver letras ou qualquer outro caractere que não seja um número, o programa deve exibir uma mensagem de erro.
import time 

while True:
    try:
        cpf = input("Digite o número seu CPF: ")
        if not cpf.isdigit():
            raise ValueError
        break
    except ValueError:
        print(f"Número inválido, tente novamente: ")
        
# print(len(cpf))

num = len(cpf)

while True:
    try:
        if num == 11:
            print("-" * 35)
            print(f"O CPF {cpf} é válido.")
            print("-" * 35)
            print("Prosseguindo atendimento...")
            break
        else:
            raise ValueError
    except ValueError:
        print(f"O CPF informado não é válido.")
        quit()
    
#O problema aqui, é caso o usuário insira pontuação...
#Para isso, posso usar o replace