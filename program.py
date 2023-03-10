import produto

print('Entre com os dados do produto:')
nome = input('Nome: ')
preco = float(input('Preco: '))
quantidade = int(input('Quantidade no estoque: '))
# variavel prod para instanciar a classe Produto com o construtor vinculando as variáveis locais
prod = produto.Produto(nome=nome, preco=preco, quantidade=quantidade)
# necessário  uso do .format
print('Dados do produto: {}, $ {}, Total: {}'.format(
    prod.nome, round(prod.preco, 2), prod.quantidade))
# adicionando produto
adicionar = int(input('Digite o número de produtos a ser adicionado ao estoque: '))
prod.adicionarprodutos(adicionar)

print('Dados do atualizados: {}, $ {}, Total: {}'.format(
    prod.nome, round(prod.preco, 2), prod.quantidade))
# removendo produto
retirar = int(input('Digite o número de produtos a ser adicionado ao estoque: '))
prod.removerprodutos(retirar)

print('Dados do atualizados: {}, $ {}, Total: {}'.format(
    prod.nome, round(prod.preco, 2), prod.quantidade))
