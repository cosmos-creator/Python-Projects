def board(pos):
    print(f"{pos[0]} | {pos[1]} | {pos[2]}")
    print("——————————")
    print(f"{pos[3]} | {pos[4]} | {pos[5]}")
    print("——————————")
    print(f"{pos[6]} | {pos[7]} | {pos[8]}")

def won(board):
    winningBoard = [[0,1,2],
                    [3,4,5],
                    [6,7,8],
                    [0,3,6],
                    [1,4,7],
                    [2,5,8],
                    [0,4,8],
                    [2,4,6]]
    for i in winningBoard:
        if (board[i[0]] == board[i[1]]) and (board[i[1]] == board[i[2]]):
            return True
    return False

def ifDraw(i):
    if (i==9):
            print("Good Game, thats a draw!")
            exit(0)

def ttt():
    from time import sleep 
    from os import system as clear
    i = 0
    positions = list(range(0,9))
    while ( i < 9 ):
        board(positions)
        print("Player 1's turn.")
        p1 = int(input("Enter a position to replace with X : "))
        if p1 in positions and positions[p1] != "O" and positions[p1] != "X":
            positions[positions.index(p1)] = "X"
            i += 1
            clear('cls')
            if won(positions):
                board(positions)
                print("Player 1 wins!")
                exit(1)
            board(positions)
            ifDraw(i)
            while True:
                clear('cls')
                print("Player 2's turn.")
                board(positions)
                p2 = int(input("Enter a position to replace with O : "))
                if (p2 in positions) and positions[p2] != "O" and positions[p2] != "X":
                    positions[positions.index(p2)] = "O"
                    i += 1
                    if won(positions):
                        clear('cls')
                        print("Player 2 wins!")
                        exit(2)
                    clear('cls')
                    break
                else:
                    print("Invalid position. Try Again.")
                    sleep(5)
                    clear('cls')
                    continue
        else:
            print("Invalid position. Try Again.")
            sleep(5)
            clear('cls')    

ttt()