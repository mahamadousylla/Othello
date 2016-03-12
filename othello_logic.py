#Mahamadou Sylla

class Othello:
    def __init__(self, turn, row, column, piece, winner):
        self._turn = turn
        self._row = row
        self._column = column
        self._board = self.make_game_board()
        self._piece = piece
        self._winner = winner
        

    def get_player_move():
        '''
        get the players move which is the row and column number
        '''
        row_column = input().strip() #prompts user to enter row followed by a space the column of where they would like to move
        row_column = row_column.split() #splits the row and the column
        row = int(row_column[0]) #saves the first index which is the row
        column = int(row_column[-1]) #saves the last index whcih is the column
        return row-1, column-1 #returns the row and column on the same line both subracted by 1 to account for the 0 index

    def make_game_board(self):
        '''
        Creates a new game board.
        User specifies the rows and
        columns they want the gameboard
        to be
        '''
        board = [ ] #empty list
        NONE = 0

        for col in range(self._column): #for every iteration in the amount of columns the user wants
            board.append([ ]) #append an empty list to the local list 'board'
            for row in range(self._row): #for every iteration of in the amount of rows the user wants
                board[-1].append(NONE) #append 0's to each sublist in the board list
        return board


    def set_game_board(self, start_disc):
        '''
        user specifies what peices should be
        where on the new game board
        '''
        if start_disc == 'B': #if the user wants the 'black' piece to be at top left corner on the middle of the board
            col = len(self._board) / 2 #finds the length of the board and divides by two to find the middle of the board by columns
            row = len(self._board[0]) / 2 #finds how many items in a row then divides by two to find the middle of the board by rows
            other_col = col - 1 #moves us back one column
            other_row = row - 1 #moves us back one row
            self._board[int(row)][int(col)] = 'B' #changes the middle of the board's piece to 'B'
            self._board[int(row)][int(other_col)] = 'W' #on the orginal row and one column to the left changes the board's piece to 'W'
            self._board[int(other_row)][int(other_col)] = 'B' #one row back and one column to the left changes the board's piece to 'B'
            self._board[int(other_row)][int(col)] = 'W' #one row back and on the original column changes the board's piece to 'W'

        elif start_disc == 'W': #if the user wants the 'white' piece to be at the top left corner on the middle of the board
            col = len(self._board) / 2 #finds the length of the board and divides by two to find the middle of the board by columns
            row = len(self._board[0]) / 2 #finds how many items in a row then divides by two to find the middle of the board by rows
            other_col = col -1 #moves us back one column
            other_row = row - 1 #moves us back one row
            self._board[int(row)][int(col)] = 'W' #changes the middle of the board's piece to 'B'
            self._board[int(row)][int(other_col)] = 'B' #on the orginal row and one column to the left changes the board's piece to 'W'
            self._board[int(other_row)][int(other_col)] = 'W' #one row back and one column to the left changes the board's piece to 'B'
            self._board[int(other_row)][int(col)] = 'B' #one row back and on the original column changes the board's piece to 'W'

        return self._board
    

    def switch_player(self):
       '''
       given the player who's turn it is,
       returns the opposite player
       '''
       if self._turn == 'B': #if it is black players turn
           self._turn = "W" #now it is white players turn
           return  self._turn #return as white players turn
       else:
           self._turn = 'B' #otherwise if it isn't black players turn now it is
           return self._turn #return as black players turn

        
    def current_pieces_on_board(self):
        '''
        keeps track of the amount of pieces that are currently on the board
        '''
        black_white = ' '
        for col in range(len(self._board)): #for every number in the amount of columns
            for row in range(len(self._board[0])): #for every number in the amount of rows
                if self._board[col][row] == 'B': #if there is a B on the board
                    black_white += 'B' #add 1 to the 'black' count
                elif self._board[col][row] == 'W': #if there is a W on the board
                    black_white += 'W' #add 1 to the 'white' count
        return black_white
                                    
            
    def winner(self, how_game_is_won):
        '''
        Takes input how to determine the winner of a game.
        counts how many current pieces there are
        on the board for each player and uses that information
        '''
        black = 0
        white = 0
        for col in range(len(self._board)): #for every number in the amount of columns on the board
            for row in range(len(self._board[0])): #for every number in the amount of row on the board
                if self._board[col][row] == 'B': #if there is a B on the board
                    black += 1 #add 1 to the 'black' count
                elif self._board[col][row] == 'W': #if there is a W on the board
                    white += 1 #add 1 to the 'white' count
        if how_game_is_won == '>': #if user specifies this is how they want the game to be won
            if black > white: #if the 'black' count is greater than the 'white' count
                return True
            elif white > black: #if the 'white' count is greater than the 'black' count
                return False
            elif black == white: #if the 'black' and 'white' count is equal
                return None
        elif how_game_is_won == '<': #if user specifies this is how they want the game to be won
            if black < white: #if the 'black' count is less than the 'white' count
                return True
            elif white < black: #if the 'white' count is less than the 'black' count
                return False
            elif black == white: #if the 'black' and 'white' count is equal
                return None


    def valid_move(self, user_row, user_column):
        '''
        checks if users move is valid or not
        '''
        if self._check_if_valid_move(user_row, user_column) == False:
            raise InvalidMoveError()
        else:
            return True


    def check_if_any_move_exists(self):
        '''
        checks if theres is valid move on the board. Returns True if there is,
        otherwise returns False.
        '''
        count = 0
        result = [ ]
        for row in range(self._row): #for every column on the board
            for col in range(self._column): #for every row on the board
                if self._check_if_valid_move(row, col) == True: #if this row and this column is a valid move that can be made on the board
                    count += 1
        if count >= 1:
            return True
        else:
            return False

    def flip_pieces(self, row, column):
        check_right = self.flip_tothe_right(row, column)
        check_left = self.flip_tothe_left(row, column)
        check_above = self.flip_above(row, column)
        check_below = self.flip_below(row, column)
        check_top_right = self.flip_top_right(row, column)
        check_top_left = self.flip_top_left(row, column)
        check_bottom_right = self.flip_bottom_right(row, column)
        check_bottom_left = self.flip_bottom_left(row, column)

    def flip_tothe_right(self, user_row, user_column):
          '''
          takes in a valid move and flips pieces to the right if possible
          '''
          if self._turn == 'B': #if it is black players turn
              if self._check_right(user_row, user_column) == True:
                    for num in range(self._column):
                        if self._board[user_row][user_column+num+1] == 'W':
                            num +1
                            self._board[user_row][user_column+1+num] = 'B'
                            self._board[user_row][user_column] = 'B'
                        else:
                            break
                        
          if self._turn == 'W': #if it is white players turn
              if self._check_right(user_row, user_column) == True:              
                    for num in range(self._column):
                        if self._board[user_row][user_column+num+1] == 'B':
                            num +1
                            self._board[user_row][user_column+1+num] = 'W'
                            self._board[user_row][user_column] = 'W'
                        else:
                            break
            
          return self._board


    def flip_tothe_left(self, user_row, user_column):
          '''
          takes in a valid move and flips pieces to the left if possible
          '''

          if self._turn == 'B': #if it is black players turn
              if self._check_left(user_row, user_column) == True:
                    for num in range(self._column):
                        if self._board[user_row][user_column-num-1] == 'W':
                            num +1
                            self._board[user_row][user_column-num-1] = 'B'
                            self._board[user_row][user_column] = 'B'
                        else:
                            break              

          if self._turn == 'W': #if it is white players turn
              if self._check_left(user_row, user_column) == True:
                    for num in range(self._column):
                        if self._board[user_row][user_column-num-1] == 'B':
                            num +1
                            self._board[user_row][user_column-num-1] = 'W'
                            self._board[user_row][user_column] = 'W'
                        else:
                            break
                        
          return self._board


    def flip_above(self, user_row, user_column):
          '''
          takes in a valid move and flips pieces above if possible
          '''
          if self._turn == 'B': #if it is black players turn
              if self._check_up(user_row, user_column) == True:
                    for num in range(self._row):
                        if self._board[user_row-num-1][user_column] == 'W':
                            num +1
                            self._board[user_row-num-1][user_column] = 'B'
                            self._board[user_row][user_column] = 'B'
                        else:
                            break

          if self._turn == 'W': #if it is white players turn
              if self._check_up(user_row, user_column) == True:
                    for num in range(self._row):
                        if self._board[user_row-num-1][user_column] == 'B':
                            num +1
                            self._board[user_row-num-1][user_column] = 'W'
                            self._board[user_row][user_column] = 'W'
                        else:
                            break

          return self._board


    def flip_below(self, user_row, user_column):
          '''
          takes in a valid move and flips pieces below if possible
          '''

          if self._turn == 'B': #if it is black players turn
              if self._check_down(user_row, user_column) == True:
                    for num in range(self._row):
                        if self._board[user_row+num+1][user_column] == 'W':
                            num +1
                            self._board[user_row+num+1][user_column] = 'B'
                            self._board[user_row][user_column] = 'B'
                        else:
                            break
                        
          if self._turn == 'W': #if it is whites players turn
              if self._check_down(user_row, user_column) == True:
                    for num in range(self._row):
                        if self._board[user_row+num+1][user_column] == 'B':
                            num +1
                            self._board[user_row+num+1][user_column] = 'W'
                            self._board[user_row][user_column] = 'W'
                        else:
                            break

          return self._board

    def flip_top_right(self, user_row, user_column):
          '''
          takes in a valid move and flip pieces in the top right direction if possible
          '''

          if self._turn == 'B': #if it is black players turn
              if self._check_top_right(user_row, user_column) == True:
                    for num in range(self._row):
                        if self._board[user_row-num-1][user_column+num+1] == 'W':
                            num +1
                            self._board[user_row-num-1][user_column+num+1] = 'B'
                            self._board[user_row][user_column] = 'B'
                        else:
                            break

          if self._turn == 'W': #if it is white players turn
              if self._check_top_right(user_row, user_column) == True:
                    for num in range(self._row):
                        if self._board[user_row-num-1][user_column+num+1] == 'B':
                            num +1
                            self._board[user_row-num-1][user_column+num+1] = 'W'
                            self._board[user_row][user_column] = 'W'
                        else:
                            break

          return self._board


    def flip_top_left(self, user_row, user_column):
          '''
          takes in a valid move and flips piece if the top left direction if possible
          '''

          if self._turn == 'B': #if it is black players turn
              if self._check_top_left(user_row, user_column) == True:
                    for num in range(self._row):
                        if self._board[user_row-num-1][user_column-num-1] == 'W':
                            num +1
                            self._board[user_row-num-1][user_column-num-1] = 'B'
                            self._board[user_row][user_column] = 'B'
                        else:
                            break

          if self._turn == 'W': #if it is white players turn
              if self._check_top_left(user_row, user_column) == True:
                    for num in range(self._row):
                        if self._board[user_row-num-1][user_column-num-1] == 'B':
                            num +1
                            self._board[user_row-num-1][user_column-num-1] = 'W'
                            self._board[user_row][user_column] = 'W'
                        else:
                            break

          return self._board


    def flip_bottom_right(self, user_row, user_column):
          '''
          takes in a valid move and flips pieces in the bottom right direction if possible
          '''

          if self._turn == 'B': #if it is black players turn
              if self._check_bottom_right(user_row, user_column) == True:
                    for num in range(self._row):
                        if self._board[user_row+num+1][user_column+num+1] == 'W':
                            num +1
                            self._board[user_row+num+1][user_column+num+1] = 'B'
                            self._board[user_row][user_column] = 'B'
                        else:
                            break

          if self._turn == 'W': #if it is white players turn
              if self._check_bottom_right(user_row, user_column) == True:
                    for num in range(self._row):
                        if self._board[user_row+num+1][user_column+num+1] == 'B':
                            num +1
                            self._board[user_row+num+1][user_column+num+1] = 'W'
                            self._board[user_row][user_column] = 'W'
                        else:
                            break
    

          return self._board


    def flip_bottom_left(self, user_row, user_column):
          '''
          takes in a valid move and flips pieces to the bottom left if possible
          '''

          if self._turn == 'B': #if it is black players turn
              if self._check_bottom_left(user_row, user_column) == True:
                    for num in range(self._row):
                        if self._board[user_row+num+1][user_column-num-1] == 'W':
                            num +1
                            self._board[user_row+num+1][user_column-num-1] = 'B'
                            self._board[user_row][user_column] = 'B'
                        else:
                            break

          if self._turn == 'W': #if it is white players turn
              if self._check_bottom_left(user_row, user_column) == True:
                    for num in range(self._row):
                        if self._board[user_row+num+1][user_column-num-1] == 'B':
                            num +1
                            self._board[user_row+num+1][user_column-num-1] = 'W'
                            self._board[user_row][user_column] = 'W'
                        else:
                            break
                        
          return self._board


    def _opp_player_turn(self):
        '''returns opposite players turn'''
        if self._turn == 'B':
            return 'W'
        else:
            return 'B'


    def _check_if_valid_move(self, user_row, user_column):
        '''
        takes in a row and column checks whether it is a possible valid move. Returns True if there is,
        otherwise returns False
        '''
        no_piece = False
        valid_move = None
        if self._board[user_row][user_column] == 0:
            no_piece = True
        if self._check_right(user_row, user_column) or self._check_left(user_row, user_column) or self._check_up(user_row, user_column) or self._check_down(user_row, user_column) or self._check_top_right(user_row, user_column) or self._check_top_left(user_row, user_column) or self._check_bottom_right(user_row, user_column) or self._check_bottom_left(user_row, user_column) == True:
            valid_move = True
        if no_piece == valid_move:
            return True
        if no_piece != valid_move:
            return False  
        

    def _check_right(self, user_row, user_column):
        '''
        checks if a valid move can be made to right
        '''
    
        opposite_player_turn = self._opp_player_turn()
        if user_column+1 == self._column: #if the users move is at the last column, we cannot check right since we are at the end of the board
            return False #return False
        elif self._board[user_row][user_column+1] == 0: #if theres is an empty space to the right 
            return False
        elif self._board[user_row][user_column+1] == opposite_player_turn: #if the space to the right is the opposite players turn
            for col in range(user_column+1, self._column): #for every column 1 to the right from where the user specified to the amount of columns there are on the board
                if self._board[user_row][col] == opposite_player_turn: #if the piece to the right is the opposite players piece
                    pass #do nothing
                elif self._board[user_row][col] == 0: #if the piece to the right is not occupied by neither player
                    return False #return False
                elif self._board[user_row][col] == self._turn: #if the peice to the right is the current players tur, we have a valid move
                    return True #return True
                elif col == self._column: #if the col is equal to amount of columns on the board, meaning we are at the end of the board
                    return False #return False
               
                   
    def _check_left(self, user_row, user_column):
        '''
        check if a valid move can be made to the left
        '''
        opposite_player_turn = self._opp_player_turn()
        if user_column <= 1: #if the column where the user wants to go is the first or second column on the board, we cannot have a valid move in the left direction
            return False #return False
        elif self._board[user_row][user_column-1] == 0: #if the space to the left is not occupied by neither player
            return False #return False
        elif self._board[user_row][user_column-1] == opposite_player_turn: #if the space to the left belongs to the opposite player
            for col in range(user_column-1, -1, -1): #for every column starting one to the left of where the user specified, to the beginning of the board which is 0
                if self._board[user_row][col] == opposite_player_turn: #checks to the left if there is an opposite players piece
                    pass #do nothing
                elif self._board[user_row][col] == 0:
                    return False
                elif self._board[user_row][col] == self._turn: #as we are moving to the left, if we encounter a piece that belongs to the current player, we have a valid move
                    return True #return True
                elif col == 0: #if we have not see the opposite players piece or the current players piece, check if there is an empty spot
                    return False #return False


    def _check_up(self, user_row, user_column):
        '''
        checks if a valid move can be made in the upward direction
        '''
        opposite_player_turn = self._opp_player_turn()
        if user_row <= 1: #if the user specifies a row that is either the 1st or 2nd row, there is no way to have a valid move in the upward direction
            return False #return False
        elif self._board[user_row-1][user_column] == 0: #if the row and column directly above specified move is empty
            return False #return False
        elif self._board[user_row-1][user_column] == opposite_player_turn: #if the row and column directly above players specified move is occupied by the opposite player
            for row in range(user_row-1, -1, -1): #for every row beginning from the users row up until the first row of the board
                if self._board[row][user_column] == opposite_player_turn: #for this row and the users specified column, checks if there is a piece that is occupied by the opposite player
                    pass #do nothing
                elif self._board[row][user_column] == 0: #for the row and the users specified column, if there is a space that is empty, we do not have a valid move
                    return False #return False
                elif self._board[row][user_column] == self._turn: #for the row and the users specified column, if there is a piece belonging to the current player, we have a valid move
                    return True #return True
                elif row == 0: #if none of the above cases are reached, we are now at the first row and have not seen a current players piece, meaning we cannot move any further
                    return False #return False


    def _check_down(self, user_row, user_column):
        '''
        checks if a valid move can be made in the downward direction
        '''
        opposite_player_turn = self._opp_player_turn()
        if user_row + 1 == self._row: #if the users specified row is the same as the amount of rows on the board, we have reached the end of the board and cannot check down
            return False #return False
        elif self._board[user_row+1][user_column] == 0: #if the row and column directly below players specified move is empty
            return False #return False
        elif self._board[user_row+1][user_column] == opposite_player_turn: #if the row and column directly below players specified move is occupied by the opposite player
            for row in range(user_row+1, self._row): #for every row beginning from the users specified row up until the last row on the board
                if self._board[row][user_column] == opposite_player_turn: #if this row and the users specified column has a piece belonging to the opposite player
                    pass #do nothing
                elif self._board[row][user_column] == 0: #if this row and the users specified column is empty, we do not have a valid move
                    return False #return False
                elif self._board[row][user_column] == self._turn: #if this row and the users specified column contains a piece belonging to the current players turn, we have a valid move
                    return True #return True
                elif row == self._row: #if none of the above cases are reached, that means we must be at the end of the board and have not seen a current players piece, meaning we cannot move any further
                    return False #return False


    def _check_top_right(self, user_row, user_column):
       '''
       checks if a valid move can be made in the top right direction
       '''
       opposite_player_turn = self._opp_player_turn()
       if user_column + 1 == self._column: #if user specifies the last column there is no way to check the top right space
              return False #return False
       elif user_row == 0: #if the users specified row is the 1st row on the board we cannot check the top right space
           return False #return False
       elif self._board[user_row-1][user_column+1] == 0: #if the row and column one row up and one column over is not occupied by any player
              return False #return False
       elif self._board[user_row-1][user_column+1] == opposite_player_turn: #if the row and column one row up and one column over has a piece that belongs to the opposite player
              row = user_row-1 #subtract one from the users row. this is the row we start checking for opposite players piece
              for col in range(user_column+1, self._column): #for every column beginning from 1 above the users specified column all the way to the amount of columns on the board
                     if self._board[row][col] == opposite_player_turn: #if the piece at this row and column belongs to the opposite player
                            pass #do nothing
                     elif self._board[row][col] == 0: #if this row and column is empty we do not have a valid move
                            return False #return False
                     elif self._board[row][col] == self._turn: #if the piece at this row and column belong to the current player. we have found a valid move
                            return True #return True
                     elif row == 0 and col == self._column: #if none of the above cases are reaches, we are at the first row and final column of the board
                            return False #return False
                     row -= 1 #move back another row


    def _check_top_left(self, user_row, user_column):
       '''
       checks if a valid move can be made in the top left direction
       '''
       opposite_player_turn = self._opp_player_turn()
       if user_column == 0: #if the users specified column is the first column on the board, it is impossible to check top left
              return False #return False
       elif user_row == 0: #if the users specified row is the first row on the board it is impossible to check top left
              return False #return False
       elif self._board[user_row-1][user_column-1] == 0: #checks if the piece one row back and one column to the left is empty
              return False #return False
       elif self._board[user_row-1][user_column-1] == opposite_player_turn: #checks if the piece one row back and one column to the left belongs to the opposite player
              row = user_row-1 #subtracts one from the row
              for col in range(user_column-1, -1, -1): #for every column beginning one to the left from the users specified to column to the first column of the board
                     if self._board[row][col] == opposite_player_turn: #if at this row and this column there is an opposite players piece
                            pass #do nothing
                     elif self._board[row][col] == 0: #if this row and column is empty we do not have a valid move
                            return False #return False
                     elif self._board[row][col] == self._turn: #if at this row and col there is a piece belonging to the current player
                            return True #return True
                     elif row == 0:
                         return False
                     elif col == 0:
                        return False #return False
                     row -= 1


    def _check_bottom_right(self, user_row, user_column):
       '''
       checks if a valid move can be made in the bottom right direction
       '''
       opposite_player_turn = self._opp_player_turn()
       if user_column + 1 == self._column: #if the column the user specified is equal to the amount of columns on the board, we cannot move any further to the right
              return False #return False
       elif user_row + 1 == self._row: #if the row the use specified is equal to the amount of rows on the board, we cannot move any more rows down
              return False #return False
       elif self._board[user_row+1][user_column+1] == 0: #if the row and column to the bottom right of the users specified move contain an empty spot
              return False #return Fasle
       elif self._board[user_row+1][user_column+1] == opposite_player_turn: #if the row and column to the bottom right of the users specified move contains a piece belonging to the opposite player
              row = user_row + 1 #move one row down
              for col in range(user_column+1, self._column): #for every column beginning one to the right from the users specified column up until the last column on the board
                     if row == self._row: #if we are at the last row, there is no way to one row further down
                            return False #return False
                     elif col == self._column: #if we are at the last column, there is no way to go one column to the right
                            return False #return False                    
                     elif self._board[row][col] == opposite_player_turn: #checks if this row and column contains a piece belonging to the opposite player
                            pass #do nothing
                     elif self._board[row][col] == 0: #if this row and column is empty we do not have a valid move
                            return False #return False
                     elif self._board[row][col] == self._turn: #checks if this row and column contains a piece belonging to the current player, if so we have a valid move
                            return True #return True
                     row += 1


    def _check_bottom_left(self, user_row, user_column):
       '''
       checks if a valid move can be made in the bottom left direction
       '''
       opposite_player_turn = self._opp_player_turn()
       if user_column - 1 == 0: #if user's specified column is the first column on the board, we cannot move 1 column to the left
              return False #return False
       elif user_row + 1 == self._row: #if the user's specified row is the last row on the board, we cannot move 1 row down
              return False
       elif self._board[user_row+1][user_column-1] == 0: #if the row and column at the bottom left of the user's specified move is empty
              return False #return False
       elif self._board[user_row+1][user_column-1] == opposite_player_turn: #if the row and column at the bottom left of the user's specified move belongs to the opposite player
              row = user_row + 1 #moves one row down
              for col in range(user_column-1, -1, -1): #for every column beginning 1 column to the left from the users specified colum up until the first column on the board
                     if row == self._row:
                         return False
                     elif col == 0: #if we are at the first column, we cannot move one column to the left
                            return False #return True
                     elif self._board[row][col] == opposite_player_turn: #if the piece at this row and column belongs to the opposite player
                            pass #do nothing
                     elif self._board[row][col] == 0: #if this row and column is empty we do not have a valid move
                            return False #return False
                     elif self._board[row][col] == self._turn: #if the piece at this row and column belongs to the current player, we have a valid move
                            return True #return True
                     row += 1



class InvalidMoveError(Exception):
    pass

class GameOverError(Exception):
    pass
