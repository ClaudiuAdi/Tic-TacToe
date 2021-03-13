def display_table(board):
    #Displaying the board

    #I: board - the board which we want to display
    #E: the board being desplayed every time someone makes a move

    print(board[0]+"|"+board[1]+"|"+board[2])
    print(board[3]+"|"+board[4]+"|"+board[5])
    print(board[6]+"|"+board[7]+"|"+board[8])

def players_deciding():
    #this program decides which player is X and which is 0

    p1=input("Player 1 will be: ")
    while p1 not in ["X","0"]:
        p1=input("Choose between X and 0: ")

    print("Player 1 will be {}".format(p1))
    if p1=="X":
        print("Player 2 is 0")
    else:
        print("Player 2 is X")

def position_board():
    #getting the position for the player to put his input

    #E: the position(casted to int) to be then substractracted - 1 in the main function because
    # we count from 0 in this programming world

    pos=input("Enter the position you want to occupy(1-9): ")

    while pos.isdigit==False or int(pos) not in range(1,10):

        pos=input("Please enter a valid number: ")
        if pos.isdigit()==False or int(pos) not in range(1,10):
            print("Sorry! Enter a number on the board!")

    return int(pos)



def outcome(board,nr):
    #Here the function outputs,depending on who and/or if someone wins

    #I: board - the board with the positions and contents of the game
    #   nr - the number of moves made
    #E: if/which player(X or 0) won
    #   pass if the game is still on and neither of the players won

    if board[0]==board[1]==board[2]:
        return "{} won!".format(board[0])
    elif board[3]==board[4]==board[5]:
        return "{} won!".format(board[3])
    elif board[6]==board[7]==board[8]:
        return "{} won!".format(board[6])
    elif board[0]==board[3]==board[6]:
        return "{} won!".format(board[0])
    elif board[1]==board[4]==board[7]:
        return "{} won!".format(board[1])
    elif board[2]==board[5]==board[8]:
        return "{} won!".format(board[2])
    elif board[0]==board[4]==board[8]:
        return "{} won!".format(board[0])
    elif board[2]==board[4]==board[6]:
        return "{} won!".format(board[2])
    elif nr == 9:
        return "Tie! No one won!"
    else:
        pass

def tic_tac_toe():
    #the main game

    #E: outputs which player won(X or 0) or if neither of them won

    print("WELCOME TO THE TIC-TAC-TOE GAME!")
    print("--------------------------------")
    response="Y"

    #made it to be able to play in consecutive rounds(or until you get bored)
    while response=="Y":
        board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

        display_table(board)
        players_deciding()
        #the ok is used for getting out of the while function
        ok=False
        #nr is used to count how many moves were made
        nr=0
        #here i used res to store the output from the function outcome, you will see why
        res=""

        #here we go through all the moves
        while nr!=9 and ok==False:
            pos=position_board()
            board[pos-1]=input("Introduce the letter:")
            #count with nr until 9 and then all the spaces were used and no player won at that point
            nr+=1
            display_table(board)
            res=outcome(board,nr)
            #in this if i compared the type of the res, which is string if one of the players won, with a simple string
            if type(res)==type("A simple string"):
                #if yes, i made ok True to be able to go out of the while
                ok=True


        print(res)
        response = input("Do you want to play another game?(Y/N): ")
        if response=="N":
            print("Thank you for playing!!")


if __name__=='__main__':
    tic_tac_toe()






