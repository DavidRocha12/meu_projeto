from menu import *
import os

os.system("clear")

nome_item = "nome_item.txt"
nome_valor_item = "valor_item.txt"

while True:

	print(f"Escolha uma das opções:\n\
(1) Adicionar item\n\
(2) Mostra dados\n\
(3) apagar item\n\
(4) Sair")

	opcao = input("Digite uma das opções: ")
	opcao = int(opcao)
	print()

	if opcao > 0 and opcao <= 4:
		if opcao == 1:
			#Lógica para marcar o produto:
			opcao_1(nome_item, nome_valor_item)

		elif opcao == 2:
			opcao_2(nome_item, nome_valor_item)

		elif opcao == 3:
			opcao_3(nome_item, nome_valor_item)
			
		elif opcao == 4:
			print("Fechando Programa!")
			break
	else:
		print("Opção incorreta, escolha a opção correta!")
