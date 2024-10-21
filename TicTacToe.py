#function to display the board/grid.
def board(pos):    
    print(f"{pos[0]} | {pos[1]} | {pos[2]}")
    print("——————————")
    print(f"{pos[3]} | {pos[4]} | {pos[5]}")
    print("——————————")
    print(f"{pos[6]} | {pos[7]} | {pos[8]}")
#function to check if any user has won the game.
def won(board):
    #A list of conditions where the user wins.
    winningBoard = [[0,1,2],
                    [3,4,5],
                    [6,7,8],
                    [0,3,6],
                    [1,4,7],
                    [2,5,8],
                    [0,4,8],
                    [2,4,6]]
    #loop to check the board with the conditons
    for i in winningBoard:
        #check if the marks are in a sequence of 3, either in rows, columns or diagonals
        if (board[i[0]] == board[i[1]]) and (board[i[1]] == board[i[2]]):
            return True
    return False
# function to check if the game is a draw when it's completed.
def ifDraw(i):
    if (i==9):
            print("Good Game, thats a draw!")
            exit(0)

def tictactoe():
    from time import sleep #sleep function to add delay in the clearing of the board.
    from os import system as clear #to clear the terminal screen off the board,
    i = 0                          #clear alias it's a bit more intuitive.
    positions = list(range(0,9))
    while ( i < 9 ): # loop to run for 9 turns.
        board(positions) # pass the positions in the function and print the board.
        print("Player 1's turn.")
        p1 = int(input("Enter a position to replace with X : ")) 
        # validate the position
        # if true then change the values in the positions list w.r.t to the entered index.
        if p1 in positions and positions[p1] != "O" and positions[p1] != "X":
            positions[positions.index(p1)] = "X"
            i += 1
            clear('cls') # clear the terminal window
            if won(positions): # check for win
                board(positions)
                print("Player 1 wins!")
                exit(1)
            board(positions) # print the board for the second user's turn
            ifDraw(i) # check for draw i.e check if the game has been played 9 times.
            while True: # loop for the second users turn.
                clear('cls') # clear the screen for the second user
                print("Player 2's turn.")
                board(positions) # print board
                p2 = int(input("Enter a position to replace with O : ")) # take index value for the input
                # validate the input
                if (p2 in positions) and positions[p2] != "O" and positions[p2] != "X":
                    positions[positions.index(p2)] = "O"
                    i += 1 # increment after every successful turn

                    #check if user has won
                    if won(positions):
                        clear('cls')
                        print("Player 2 wins!")
                        exit(2)
                    clear('cls')
                    break
                    
                # if invalid input, ask for their input again untill a valid input is entered.
                else:
                    print("Invalid position. Try Again.")
                    sleep(2)
                    clear('cls')
                    continue
        else:
            print("Invalid position. Try Again.")
            sleep(2)
            clear('cls')    
# play the game :)
tictactoe()
