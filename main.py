produto = {
    "nome": "",
    "custo_producao": 0,
    "preco_venda": 0,
    "estoque_atual": 0
}

def cadastrarProduto():
    print("\n" + "="*40)
    print("      Cadastrar Produto")
    print("="*40)
    produto["nome"] = input("Nome do produto: ")
    produto["custo_producao"] = float(input("Custo de produção: "))
    produto["preco_venda"] = float(input("Preço de venda: "))
    produto["estoque_atual"] = int(input("Estoque atual: "))


cadastrarProduto()
print(produto["nome", "custo_producao"])
