#condição 
print("Bem Vindo ao Game of Legend")
print("1. Ir para a floresta!")
print("2. Dormir na casa")
print("3. Sair do jogo")

choice =  int(input("O que você quer fazer. "))

if choice == 1:
    print("Você está na floresta amaldiçoada!")
    print("1. Se esconder nas pedras!")
    print("2. Entrar em uma cavera!")
    print("3. Analisar a floresta!")
    escolha = int(input("Qual opção voce quer proseguir? "))
    if escolha == 1:
        print("Jogador esta escondido nas pedras!")
        
    elif escolha == 2:
        print("Jogador esta escondido, dentro da caverna da floresta!")

    elif escolha == 3:
        print("Joagdor esta analisando todo o campos da floresta amaldiçoada!")         

    else: 
       print("Voce foi atacado por um leão magico, demorou muito para tomar uma decisão")   
      
elif choice == 2:
    print("Você está dormindo agora!")

else:
    print("Você saiu do jogo!")
            