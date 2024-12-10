# BACK-END

class Livro: 
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano 

    def mostrar_informacoes(self):
        return f'Título: {self.titulo}, Autor: {self.autor}, Ano: {self.ano}'    


class Biblioteca: 
    def __init__(self):
        self.livros = [] 

    def adicionar_livros(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        if not self.livros:
            print("Nenhum livro cadastrado.")
        for livro in self.livros:
            print(livro.mostrar_informacoes())

    def salvar_livros_em_arquivo(self, nome_arquivo):
        with open(nome_arquivo, 'w') as arquivo:
            for livro in self.livros:
                arquivo.write(f'{livro.titulo}, {livro.autor}, {livro.ano}\n')

        print(f'Livros salvos no arquivo "{nome_arquivo}" com sucesso!')

# FRONT-END

def main():
    biblioteca = Biblioteca()

    while True:
        print("\n1. Adicionar livro")
        print("2. Listar livros")
        print("3. Salvar livros")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            ano = input("Digite o ano de publicação: ")
            
            if not ano.isdigit():
                print("Ano inválido. Deve ser um número.")
                continue

            # CRIAÇÃO DO OBJETO COM OS DADOS EXTRAÍDOS PELO USUÁRIO
            livro = Livro(titulo, autor, ano)
            biblioteca.adicionar_livros(livro)
            print("Livro registrado com sucesso!")

        elif escolha == '2':
            print("\nLista de livros: ")
            biblioteca.listar_livros()

        elif escolha == '3':
            nome_arquivo = input("Digite o nome do arquivo para salvar os livros: ")
            biblioteca.salvar_livros_em_arquivo(nome_arquivo)

        elif escolha == '4':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
