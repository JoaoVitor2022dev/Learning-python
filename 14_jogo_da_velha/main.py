# jogo da velha 

# tabuleiro
tabuleiro = ['' for _ in range(9)]


# exibir o tabuleiro
def exibir_tabuleiro():  
    print()
    print(f'  {tabuleiro[0]} | {tabuleiro[1]}  | {tabuleiro[2]}')
    print(f'---|---|---')
    print(f'  {tabuleiro[3]} | {tabuleiro[4]}  | {tabuleiro[5]}')
    print(f'---|---|---')
    print(f'  {tabuleiro[8]} | {tabuleiro[7]}  | {tabuleiro[8]}')
    print()

# programando a jogada 
def jogada(jogador):
    while True:
        try:
            posicao = int(input(f'Jogador: {jogador}, escolha uma posição (1-9) ')) - 1 
            if posicao < 0 or posicao > 8:
                print("Posição inválida! Escolha um número entre 1 e 5.")
            elif tabuleiro[posicao] != ' ': 
                print("Posição já  ocupada! Escolha outra posição.")   
            else:
                tabuleiro[posicao] = jogador 
                break
        except ValueError:
            print("Entrada inválida! Por Favor, insira um número entre 1 e 9.")        


# Verificar Vitoria

def verificar_vitoria(jogador):
    combinacoes = [
        [0,1,2], [3,4,5], [6,7,8], # Linhas
        [0,3,6], [1,4,7], [2,5,8], # Colunas 
        [0,4,8], [2,4,6]         # Diagonais  
        ]             
    for combinacao in combinacoes:
        if tabuleiro[combinacao[o]] == tabuleiro[combinacao[1]] == tabuleiro[combinacao[2]] == jogador:
            return True
    return False


def jogar_jogo():
    jogador_atual = 'x'
    for turno in range(9):
        exibir_tabuleiro()
        jogada(jogador_atual)
        if verificar_vitoria(jogador_atual):
            exibir_tabuleiro()
            print(f'Jogador {jogador} venceu!')
            return
        jogador_atual = 'O' if jogador_atual == x else 'x'
        exibir_tabuleiro()
        print('Empate!')

jogar_jogo()        
 