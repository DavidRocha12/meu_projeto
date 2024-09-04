import os
from classes import Despesas

os.system("clear")

while True:
    try:
        print("Digite a opção desejada abaixo:")
        print()
        print("1 - Inserir Despesas")
        print("2 - Visualizar Despesas")
        print("3 - Apagar item da lista")
        print("4 - Sair")
        print() 
        opcao = input("Digite a opção que deseja: ")
        opcao = int(opcao)

    except (ValueError, NameError):
        print("Esse valor não existe, digite novamente!")
   


    arquivo_nome = "nome_despesas"
    arquivo_valor = "valor_despesas"

    conta = Despesas
    if opcao == 1:

        while True:
            nome_despesas = input("Digite o nome da despesa adicionar: ")
            valor_despesas = input("Digite o valor da despesa: R$")
            conta = Despesas(nome_despesas, valor_despesas)
            conta.inserir_conta_valor(arquivo_nome)
            conta.inserir_conta_valor(arquivo_valor)
            continuar = input("Quer continuar adicionando despesas? ")
            while continuar not in "SsNn":
                continuar = input("Quer continuar adicionando despesas? ")
            print()
            if continuar in "Nn":
                break

    if opcao == 2:

        try:
            nome = conta.imprimir_despesas(arquivo_nome)
            valor = conta.imprimir_despesas(arquivo_valor)
        
            print()
            print("Minhas Contas")
            print()

            soma = 0
            for indice, n in enumerate(nome):
                print(f"{indice + 1} - {n:.<40}{float(valor[indice]):.2f}")
                soma += float(valor[indice])

            if soma == 0:
                print("\033[31mNão existe nada na Lista!\033[m")

        except ValueError:
            print("\033[31mNão existe nada na Lista!\033[m")

        print()
        print(f"Total de contas a pagar: {soma}")
        print()

    if opcao == 3:
        try:
            numero = input("Digite o número do item que deseja apagar:")
            print()
            numero = int(numero) - 1

            apagar_nome = conta.apagar_item(arquivo_nome, numero)
            apagar_valor = conta.apagar_item(arquivo_valor, numero)
        except IndexError:
            print()
            print("\033[31mNão existe nada a ser apagado!\033[m")
            print()

    if opcao == 4:
        break
