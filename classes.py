class Despesas:

    __slots__ = ["_conta", "_valor"]

    def __init__(self, conta, valor):
        """Atributos de classes para receber nome da despesa e 
        valor da despesa que vai ser adicionada aos arquivos."""
        self._conta = conta 
        self._valor = valor


    def inserir_conta_valor(self, nome_arquivo):
        """A função vai receber o parâmetro nome_arquivo, e através da
        da estrutura condicional, if e elif, vai ser decidido qual
        comando vai ser usado, através do nome do arquivo."""
        if nome_arquivo == "nome_despesas":
            nome_conta = self._conta
        elif nome_arquivo == "valor_despesas":
            nome_conta = self._valor
        
        arquivo = open(nome_arquivo, "a")
        arquivo.write(f"{nome_conta}\n")
        arquivo.close()


    def apagar_item(nome_arquivo, indice):
        # Leitura do arquivo
        arquivo = open(nome_arquivo, "r")
        # adicionando o que foi lido em uma lista
        produto = []
        for item in arquivo:
            produto.append(item.strip())
        arquivo.close()
        # apagando o item da lista com a função pop, a função pop apaga
        # o item da lista pelo índice.
        apagar = indice
        produto.pop(int(apagar))

        # criando um arquivo vazio:
        arquivo = open(nome_arquivo, "w")
        arquivo.close()

        # adicionando o que sobrou na lista, atravez de um for em cada
        # um de seus arquivos.
        for item in produto:
            arquivo = open(nome_arquivo, "a")
            arquivo.write(f"{item}\n")
            arquivo.close()



    def imprimir_despesas(nome_arquivo):
        arquivo = open(nome_arquivo, "r")
        produto = []
        
        for item in arquivo:
            item = item.strip()
            produto.append(item)
        
        arquivo.close()
        return produto
    