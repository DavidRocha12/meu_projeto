def adicionar_produto(nome_arquivo, conteudo):
	"""Vai receber nome do arquivo, e vai receber nome
	do objeto para ser adicionado"""
	arquivo = open(nome_arquivo, "a")
	arquivo.write(f"{conteudo}\n")
	arquivo.close()


def leitura_dados(arquivo):
	arquivo = open(arquivo, "r")
	listas = []
	for produtos in arquivo:
		listas.append(produtos.strip())
	arquivo.close()
	return listas


def deletar_item(arquivo, indice):
	arquivo = open(arquivo, "r")
	listas = []
	for produtos in arquivo:
		listas.append(produtos.strip())
	arquivo.close()
	remover = indice
	listas.pop(int(remover))
	return listas


def atualizar_dados(arquivo, item):
	atualizar_arquivo = open(arquivo, "w")
	atualizar_arquivo.close()
	for produto in item:
		atualizado = adicionar_produto(arquivo, produto)

