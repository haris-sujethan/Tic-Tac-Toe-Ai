"""
Impossible to Beat Tic Tac Toe Ai

You Will Begin by placing the Letter X On a three-by-three grid, 
You Will Take Turns Marking The Spaces Against an Ai Who Will Place The Letter O,
The player who places three of their marks in a vertical, horizontal, or diagonal row is the winner,
However, No Matter How Great you play, you will only Lose or Tie against the Ai. 

"""

global Name
Name = \
    input('Welcome to Impossible Tic Tac Toe, to Begin What is Your Name: '
          )  # Asks Name Before While Loop, so if a restart takes palce the program wont ask for the name again

restart = True
while restart == True:

    User = 'X'  # Assigns the user to X
    Ai = 'O'  # Assigns the Ai to O

    Table = {
        1: ' ',
        2: ' ',
        3: ' ',
        4: ' ',
        5: ' ',
        6: ' ',
        7: ' ',
        8: ' ',
        9: ' ',
        }


    def PrintTable(Table):  # Creates Grid for Tic Tac Toe
        print ('\n')
        print (Table[1] + ' | ' + Table[2] + ' | ' + Table[3])
        print ('---------')
        print (Table[4] + ' | ' + Table[5] + ' | ' + Table[6])
        print ('---------')
        print (Table[7] + ' | ' + Table[8] + ' | ' + Table[9])
        print ('\n')


    PrintTable(Table)  # Prints the table in the console
    print ('Hello ' + Name + ", You Will be Playing as 'X' ")


    def PostionCheck(position):  # Checks if the postion on the table is empty
        if Table[position] == ' ':
            return True
        else:
            return False


    def DrawCheck():  # Checks if the game is a draw
        for key in Table.keys():
            if Table[key] == ' ':
                return False
        return True


    def PlayAgain():  # Asks the user if they want to play again
        restart = input('Would you like to play again (y/n)')
        if restart == 'y':
            print ('Restarting...')
        else:
            print ('Goodbye')
            exit()


    def WinCheck():  # Checks if the game has been won
        if Table[1] == Table[2] and Table[1] == Table[3] and Table[1] \
            != ' ':
            return True
        elif Table[4] == Table[5] and Table[4] == Table[6] and Table[4] \
            != ' ':
            return True
        elif Table[7] == Table[8] and Table[7] == Table[9] and Table[7] \
            != ' ':
            return True
        elif Table[1] == Table[4] and Table[1] == Table[7] and Table[1] \
            != ' ':
            return True
        elif Table[2] == Table[5] and Table[2] == Table[8] and Table[2] \
            != ' ':
            return True
        elif Table[3] == Table[6] and Table[3] == Table[9] and Table[3] \
            != ' ':
            return True
        elif Table[1] == Table[5] and Table[1] == Table[9] and Table[1] \
            != ' ':
            return True
        elif Table[7] == Table[5] and Table[7] == Table[3] and Table[7] \
            != ' ':
            return True
        else:
            return False


    def AddLetter(letter, position):  # Adds a letter to the table
        if PostionCheck(position):
            Table[position] = letter
            PrintTable(Table)
            if DrawCheck():
                print (Name + ' You have Drawn With The Ai')
                PlayAgain()
            if WinCheck():
                if letter == 'O':
                    print ('Bot Wins! and ' + Name + ' Lost')
                    PlayAgain()
                else:
                    print +Name + ' Wins!'
                    PlayAgain()

            return
        else:

            print ("Can't insert Here")
            position = int(input('Please enter new position (1-9):  '))
            AddLetter(letter, position)
            return


    def UserMove():  # Asks the user where to place their letter
        position = int(input("Enter the position for 'X' (1-9):  "))
        AddLetter(User, position)
        return


    def AiMove():  # Decides the best move for the Ai
        bestScore = -800
        bestMove = 0
        for key in Table.keys():
            if Table[key] == ' ':
                Table[key] = Ai
                score = minimax(Table, 0, False)
                Table[key] = ' '
                if score > bestScore:
                    bestScore = score
                    bestMove = key

        AddLetter(Ai, bestMove)
        return


    def WhichPlayerHasWon(x):  # Checks which player has won for minimax
        if Table[1] == Table[2] and Table[1] == Table[3] and Table[1] \
            == x:
            return True
        elif Table[4] == Table[5] and Table[4] == Table[6] and Table[4] \
            == x:
            return True
        elif Table[7] == Table[8] and Table[7] == Table[9] and Table[7] \
            == x:
            return True
        elif Table[1] == Table[4] and Table[1] == Table[7] and Table[1] \
            == x:
            return True
        elif Table[2] == Table[5] and Table[2] == Table[8] and Table[2] \
            == x:
            return True
        elif Table[3] == Table[6] and Table[3] == Table[9] and Table[3] \
            == x:
            return True
        elif Table[1] == Table[5] and Table[1] == Table[9] and Table[1] \
            == x:
            return True
        elif Table[7] == Table[5] and Table[7] == Table[3] and Table[7] \
            == x:
            return True
        else:
            return False


    def minimax(Table, depth, isMaximizing):  # The minimax algorithm checks every possible postion, assign scores to them, and return the best score
        if WhichPlayerHasWon(Ai):
            return 1
        elif WhichPlayerHasWon(User):
            return -1
        elif DrawCheck():
            return 0

        if isMaximizing:
            bestScore = -800
            for key in Table.keys():
                if Table[key] == ' ':
                    Table[key] = Ai
                    score = minimax(Table, depth + 1, False)
                    Table[key] = ' '
                    if score > bestScore:
                        bestScore = score
            return bestScore
        else:

            bestScore = 800
            for key in Table.keys():
                if Table[key] == ' ':
                    Table[key] = User
                    score = minimax(Table, depth + 1, True)
                    Table[key] = ' '
                    if score < bestScore:
                        bestScore = score
            return bestScore


    while not WinCheck():  # User begins than the Ai
        UserMove()
        AiMove()