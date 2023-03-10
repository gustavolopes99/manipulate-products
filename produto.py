class Produto():
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def valortotalemestoque(self):
        total = self.preco * self.quantidade
        print(total)

    def adicionarprodutos(self, qtd):
        self.quantidade += qtd

    def removerprodutos(self, qtd):
        self.quantidade -= qtd
