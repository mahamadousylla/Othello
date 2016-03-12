#Mahamadou Sylla 61549479

import othello_logic

def get_user_input():
    '''
    prompts user on how they would like to play
    their new game of Othello and returns their input
    in a list
    '''
    print('FULL')
    responses = [ ] #empty list
    num_of_rows = int(input()) #prompts user how many rows they want on the board
    num_of_columns = int(input()) #prompts user how many columns they want on the board
    who_moves_first = input() #prompts user who moves first. either 'B' for black or 'W' for white
    arrangemenet_of_cells_on_board = input() #prompts user for whos piece will be on the top left corner of center of board
    how_game_is_won = input() #prompts user how they want the winner to be determined
    responses.append(num_of_rows) #adds the number of rows user wants to reponses list
    responses.append(num_of_columns) #adds the number of columns user wants to growing responses list
    responses.append(who_moves_first) #adds who will move first to growing responses list
    responses.append(arrangemenet_of_cells_on_board) #adds how user wants arrangement of cells to be to growing responses list
    responses.append(how_game_is_won) #adds how the game is won to growing responses list
    return responses #returns this list that consists of 5 different options on how user wants their game of Othello to be played


list_of_info = get_user_input() #list of inputs from the user which contains all the information needed to for how to othello game will be played


def print_board(board):
    '''
    prints the gameboard to the console,
    based on users preference on how board
    should look on the start of the game
    '''
    count = 0 
    for sublist in board: #iterates over each row in the board
        for item in sublist: #iterates over each item in the row
            if item == 0: #if the item is 0
                print('.', end = ' ') #print a dot followed by a space
            elif item == 'B': #if the item is B
                print('B', end = ' ') #print a B followed by a space
            elif item == 'W': #if the item is W
                print('W', end = ' ') #print a W followed by a space
        count += 1
        if count == len(board):
            break
        print('\n') #prints a new line following each row              

def print_pieces(string):
    '''
    takes in a string, iterates through it and
    keep track of how many 'B' and 'W' pieces
    there are each
    '''
    black = 0
    white = 0
    for disc in string:
        if disc == 'B':
            black +=1
        elif disc == 'W':
            white += 1
    print('B: {}  W: {}'.format(black, white)) #formats to print information a specific style


def determine_winner(winner):
    '''
    takes in a winner of the game and
    prints the following depending on
    the outcome of the game
    '''
    if winner == True:
        print('WINNER: B')
    elif winner == False:
        print('WINNER: W')
    elif winner == None:
        print('WINNER: NONE')
    
def get_player_move():
    '''
    get the players move which is the row and column number
    '''
    row_column = input().strip() #prompts user to enter row followed by a space the column of where they would like to move
    row_column = row_column.split() #splits the row and the column
    row = int(row_column[0]) #saves the first index which is the row
    column = int(row_column[-1]) #saves the last index whcih is the column
    return row-1, column-1 #returns the row and column on the same line both subracted by 1 to account for the 0 index


def Othello(turn, row, column, piece, winner):
    '''
    A new game of Reversi, familiarly
    known as Othello. Goes turn by turn
    until there is a winner
    '''
    reversi = othello_logic.Othello(turn, row, column, piece, winner) #calls the Othello class from the othello_game_logic module
    board = reversi.set_game_board(piece) #calls the function in the othello_game_logic module that displays the brand new game state of the Othello game
    no_winner = False
    black_white = reversi.current_pieces_on_board()
    print_pieces(black_white)
    print_board(board) #prints the beginning game state of the Othello game
    print()
    print('TURN:', turn) #prints which player will move first
    while no_winner == False:
        try:
            if reversi.check_if_any_move_exists() == True:
                row, column = get_player_move() #calls the function that gets the users specified move
                if reversi.valid_move(row, column) == True:
                    reversi.flip_pieces(row, column)
                    board[row][column] = turn #changes the place in the board where the user specified with either a 'B' if its blacks turn or 'W' if its whites turn
                    turn = reversi.switch_player() #switches the players turn

                    black_white = reversi.current_pieces_on_board()
                    if reversi.check_if_any_move_exists() == False:
                        turn = reversi.switch_player()

                    if reversi.check_if_any_move_exists() == False:
                        no_winner = True
                        print('VALID')
                        print_pieces(black_white)
                        print_board(board) #prints the updated game board after each move
                        winner = reversi.winner(winner)
                        print()
                        determine_winner(winner)
                        return
                        
                    print('VALID')
                    print_pieces(black_white)
                    print_board(board) #prints the updated game board after each move
                    print()
                    print('TURN:', turn) #prints who current turn it is

                
        except:
            print('INVALID')


if __name__ == '__main__':
    Othello(list_of_info[2], list_of_info[0], list_of_info[1], list_of_info[3], list_of_info[4])

