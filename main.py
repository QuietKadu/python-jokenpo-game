import random, os, time

def game():
    while True:
        print("1 - Pedra")
        print("2 - Papel")
        print("3 - Tesoura")
        try:
            option = int(input("Digite a opção que você deseja: "))
            if option > 3:
                print("\nDigite uma opção valida")
                time.sleep(5)
                os.system('cls' if os.name == 'nt' else 'clear')
                continue
            hand = ["Pedra", "Papel", "Tesoura"]
            bot = random.choice(hand)
            if option == 1:
                if bot == "Pedra":
                    print("\nEmpate")
                elif bot == "Papel":
                    print("\nVocê perdeu")
                else:
                    print("\nVocê venceu")
            elif option == 2:
                if bot == "Pedra":
                    print("\nVocê venceu")
                elif bot == "Papel":
                    print("\nEmpate")
                else:
                    print("\nVocê perdeu")
            elif option == 3:
                if bot == "Pedra":
                    print("\nVocê perdeu")
                elif bot == "Papel":
                    print("\nVocê venceu")
                else:
                    print("\nEmpate")
            choice = ""
            while choice.upper() != "S" and choice.upper() != "N":
                choice = input("\nDeseja jogar novamente [S/N]: ")
                if choice.upper() != "S" and choice.upper() != "N":
                    print("\nDigite uma opcão valida")
                    if choice.upper() == "N":
                        break
        except:
            print('\nDigite apenas os numeros descritos na tela')
            time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')
        
game()    
