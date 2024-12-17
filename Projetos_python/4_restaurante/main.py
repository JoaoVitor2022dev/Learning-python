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


## FRONT END 

def main():
    restaurante = Restaurante()
 
    #Adicionar produtos ao menu 
    restaurante.AdicionarProdutoMenu(Produto("Hanburguer", 15.50))
    restaurante.AdicionarProdutoMenu(Produto("Pizza", 90.50))
    restaurante.AdicionarProdutoMenu(Produto("Refrigerante", 5.50))
    restaurante.AdicionarProdutoMenu(Produto("Suco", 9.0))

    pedido = restaurante.CriarPedido()
     
    while True:
        print("\n1. Mostrar Menu") 
        print("2. Adicionar Produto ao pedido") 
        print("3. Mostrar pedido e total") 
        print("4. Sair") 
        escolha = input("Escolhe um opção: ")

        if escolha == '1':
            print("\nMenu:")
            restaurante.listarMenu()
        elif escolha == '2':
            nome_produto = input("Digite o nome do produto que deseja adicionar ao pedido: ")
            for produto in restaurante.menu:
                if produto.nome.lower() == nome_produto.lower():
                    pedido.AdicionarProdutos(produto)
                    print(f"{produto.nome} adicionar ao pedido.") 
                    break
            else:
                print("Produto não encontrado no menu")
        elif escolha == "3":
            print("\nResumo do pedido:")
            print(pedido.MostrarInformacao())
        elif escolha == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()


           