def print_tabuleiro(tabuleiro):
    for i in range(0, 9, 3):
        print(tabuleiro[i] + ' | ' + tabuleiro[i+1] + ' | ' + tabuleiro[i+2])
        if i < 6:
            print('--+---+--')
def checar_ganhador(tabuleiro, jogador):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
                      (0, 3, 6), (1, 4, 7), (2, 5, 8), 
                      (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if tabuleiro[condition[0]] == tabuleiro[condition[1]] == tabuleiro[condition[2]] == jogador:
            return True
    return False
def main():
    tabuleiro = [' ' for _ in range(9)]
    current_player = 'X'
    
    while True:
        print_tabuleiro(tabuleiro)
        move = int(input(f"Jogador {current_player}, escolha um número de 0 a 8:"))
        
        if tabuleiro[move] == ' ':
            tabuleiro[move] = current_player
        else:
            print("Posição inválida. Jogue novamente!")
            continue
        
        if checar_ganhador(tabuleiro, current_player):
            print_tabuleiro(tabuleiro)
            print(f"Jogador {current_player} ganhou!")
            break
        
        if ' ' not in tabuleiro:
            print_tabuleiro(tabuleiro)
            print("It's a draw!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'
if __name__ == "__main__":
    main()
