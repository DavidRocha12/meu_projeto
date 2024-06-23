from main_configuration import *


def opcao_1(nome_item, nome_valor_item):
	while True:
		produto = input("Digite o nome do produto: ")
		print()

		valor_produto = input("Digite o valor: ")
		valor_produto = float(valor_produto)

		cont = input("Quer continuar adicionando? [S/N] ")
		while cont not in "SsNn":
			cont = input("Quer continuar adicionando? [S/N] ")

		adicionando = adicionar_produto(nome_item, produto)
		adicionando_valor = adicionar_produto(nome_valor_item, valor_produto)

		print()
		if cont in "Nn":
			break


def opcao_2(nome_item, nome_valor_item):

	conta = "Contas a Pagar" 
	print(f"{conta:*^40}")
	print()

	dados_arquivo = leitura_dados(nome_item)
	dados_arquivo_item = leitura_dados(nome_valor_item)

	soma = 0
	for chave, valor in enumerate(dados_arquivo):
		print(f"{chave + 1} {dados_arquivo[chave]:.<28}{float(dados_arquivo_item[chave]):.2f}")
		soma += float(dados_arquivo_item[chave])

	print()
	print(f"Saldo total a pagar: R$ {soma:.2f}")
	print("*" * 40)
	print()


def opcao_3(nome_item, nome_valor_item):
	indice = input("Digite o número do produto que deseja ser deletado: ")
	indice = int(indice)

	deletar_dados = deletar_item(nome_item, indice-1)
	deletar_valor = deletar_item(nome_valor_item, indice-1)

	dados_atualizados = atualizar_dados(nome_item, deletar_dados)
	dados_atualizados_2 = atualizar_dados(nome_valor_item, deletar_valor)
