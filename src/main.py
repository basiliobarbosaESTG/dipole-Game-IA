# DIPOLE GAME
from games.dipole.players.greedy import GreedyDipolePlayer
from games.dipole.players.human import HumanDipolePlayer
from games.dipole.players.minimax import MinimaxDipolePlayer
from games.dipole.players.random import RandomDipolePlayer
from games.dipole.simulator import DipoleSimulator
from games.game_simulator import GameSimulator


def run_simulation(desc: str, simulator: GameSimulator, iterations: int):
    print(f"----- {desc} -----")

    for i in range(0, iterations):
        simulator.run_simulation()

    print("Resultados do jogo:")
    simulator.print_stats()


def main():
    print("ESTG IA Dipole Game Simulator")

    while True:
        print("\n----- MENU DO JOGO -----\n")
        print("1. Jogar Dipole")
        print("2. Dipole regras")
        print("0. Fechar programa")
        choice = input("Introduza a opção: ")

        if choice == "1":
            while True:
                print("\n----- JOGAR DIPOLE -----\n")
                print("1. Human VS Human")
                print("2. Human VS Computer")
                print("3. Computer VS Computer")
                print("0. Voltar")
                game_option = input("Introduza a opção: ")

                if game_option == "1":
                    run_simulation("Dipole - Human VS Human", DipoleSimulator(HumanDipolePlayer("Human 0"), HumanDipolePlayer("Human 1")), 1)
                elif game_option == "2":
                    while True:
                        print("\n----- SELECIONE A DIFICULDADE -----\n")
                        print("1. Random")
                        print("2. Greedy")
                        print("3. Minimax")
                        print("0. Voltar")
                        difficulty_option = input("Introduza a opção: ")

                        if difficulty_option == "1":
                            player = RandomDipolePlayer("Random")
                        elif difficulty_option == "2":
                            player = GreedyDipolePlayer("Greedy")
                        elif difficulty_option == "3":
                            player = MinimaxDipolePlayer("Minimax")
                        elif difficulty_option == "0":
                            break
                        else:
                            print("Opção inválida, tente novamente.")
                            continue

                        run_simulation(f"Dipole - Human VS {player.get_name()}", DipoleSimulator(HumanDipolePlayer("Human"), player), 1)
                        break
                elif game_option == "3":
                    while True:
                        print("\n----- SELECIONE A DIFICULDADE -----\n")
                        print("1. Random vs Random")
                        print("2. Greedy vs Greedy")
                        print("3. Minimax vs Minimax")
                        print("4. Random vs Greedy")
                        print("5. Random vs Minimax")
                        print("6. Greedy vs Minimax")
                        print("0. Voltar")
                        difficulty_option = input("Introduza a opção: ")

                        if difficulty_option == "1":
                            player1 = RandomDipolePlayer("Random 1")
                            player2 = RandomDipolePlayer("Random 2")
                        elif difficulty_option == "2":
                            player1 = GreedyDipolePlayer("Greedy 1")
                            player2 = GreedyDipolePlayer("Greedy 2")
                        elif difficulty_option == "3":
                            player1 = MinimaxDipolePlayer("Minimax 1")
                            player2 = MinimaxDipolePlayer("Minimax 2")
                        elif difficulty_option == "4":
                            player1 = RandomDipolePlayer("Random")
                            player2 = GreedyDipolePlayer("Greedy")
                        elif difficulty_option == "5":
                            player1 = RandomDipolePlayer("Random")
                            player2 = MinimaxDipolePlayer("Minimax")
                        elif difficulty_option == "6":
                            player1 = GreedyDipolePlayer("Greedy")
                            player2 = MinimaxDipolePlayer("Minimax")
                        elif difficulty_option == "0":
                            break
                        else:
                            print("Opção inválida, tente novamente.")
                            continue
                        
                        print("\n----- SELECIONE O NÚMERO DE ITERAÇÕES -----\n")
                        iterations = int(input("Introduza o número de iterações: "))
                        
                        run_simulation(f"Dipole - {player1.get_name()} VS {player2.get_name()}", DipoleSimulator(player1, player2), iterations)
                        break
                elif game_option == "0":
                    break
                else:
                    print("Opção inválida, tente novamente.")
        elif choice == "2":
            print("\n----------------------------------------------------- REGRAS DIPOLE -----------------------------------------------------\n")
            print(f"1 - Este jogo consiste num jogo de tabuleiro de 8x8 com um conjunto de peças.")
            print(f"2 - A primeira jogada é feita pelo jogador com as peças pretas(B), de seguida o jogador com as brancas(W).")
            print(f"3 - Uma jogada consiste em colocar uma peça num dos espaços vazios no tabuleiro.")
            print(f"4 - Uma vez introduzidas no jogo, as peças podem ser capturadas pelo oponente e removidas do tabuleiro.")
            print(f"5 - O número de quadrados que uma pilha é movida deve ser igual ao número de peças na pilha movida.")
            print(f"6 - O jogador pode mover a pilha inteira ou apenas uma porção desta. Pode ainda passar a sua vez de jogar para o oponente.")
            print(f"7 - Uma pilha pode capturar apenas uma pilha inimiga inteira, que deve ser de tamanho igual ou menor que a pilha de captura.")
            print(f"8 - Vence o jogador que seja o primeiro a eliminar todas as peças do seu oponente.")
            print("\n----------------------------------------------------- REGRAS DIPOLE -----------------------------------------------------\n")
        elif choice == "0":
            print("A terminar jogo...")
            break
        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()
