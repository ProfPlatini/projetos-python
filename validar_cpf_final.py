# Carlos trabalha em um cartório e precisa validar se um CPF informado pelo cliente tem o formato correto antes de prosseguir com o atendimento. O CPF deve conter exatamente 11 dígitos numéricos. Se a entrada contiver letras ou qualquer outro caractere que não seja um número, o programa deve exibir uma mensagem de erro.
import time 

while True:
    try:
        cpf = input("Digite o número seu CPF: ")
        cpf = cpf.replace(".","") #Tudo o que tem ponto, fica sem nada.
        cpf = cpf.replace("-","") #Tudo o que tem -, fica sem nada.
        num = len(cpf)
        if not cpf.isdigit() or num != 11:
            raise ValueError
        if num == 11:
            print("-" * 35)
            print(f"O CPF {cpf} é válido.")
            print("-" * 35)
            print("Prosseguindo atendimento...")
        break
    except ValueError:
        print("-" * 35)
        print(f"Número inválido, tente novamente em 5 segundos.")
        print("-" * 35)
        time.sleep(5)
        