import dados
from estoque import listar_pecas
from datetime import datetime

def vender_peca():
    listar_pecas()
    id_digitado = int(input("ID: "))
    matricula = input("Matrícula: ")

    for p in dados.pecas:
        if p.id == id_digitado:
            qtd = int(input("Quantidade: "))

            if qtd > p.estoque:
                print("Estoque insuficiente!\n")
            else:
                p.estoque -= qtd
                total = qtd * p.preco
                dados.faturamento += total
                dados.salvar_json()

                print("Venda realizada!")
                print("Total:", total)
                print("Faturamento:", dados.faturamento)
                print("Data:", datetime.now(), "\n")
            return

    print("Peça não encontrada!\n")