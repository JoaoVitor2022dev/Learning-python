""""
1 - produto: Para o representar os itens do menu, como comidas e bebidas. 
2 - Pedido: para gerenciar os itens pedidos  pelo cliente. 
3 - restaurante: Para gerenciar o menu e os pedidos
"""

# BACK AND 

class Produto: 
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def MostrarInformacao(self):
        return f'Produto: {self.nome}, {self.preco}'

class Pedido:
    def __init__(self):
        self.itens = []

    def AdicionarProdutos(self, produto):
        self.itens.append(produto)
 
    def CalcularTotal(self):
        total = sum(produto.preco for produto in self.itens)   
        return total 
    
    def MostrarInformacao(self):
        info = 'Itens do pedido:\n'
        for produto in self.itens:
            info += f'- {produto.MostrarInformacao()}\n'
        info += f'Total: R${self.CalcularTotal():.2f}'
        return info 


class Restaurante:
    def __init__(self):
        self.menu = []

    def AdicionarProdutoMenu(self, produto):
        self.menu.append(produto) 

    def listarMenu(self): 
        for produto in self.menu:
            print(produto.MostrarInformacao())

    def CriarPedido(self):
        return Pedido()





