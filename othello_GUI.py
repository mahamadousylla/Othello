#Mahamadou Sylla

import tkinter
import othello_logic
import math

class game_screen:
    def __init__(self, game, root):
            '''
            The Othello Graphical User Interface
            '''
            self._game = game
            self._board = game.set_game_board(game._piece)
            self._root_window = root               
            self._row = game._row
            self._column = game._column
            self._first_piece = game._piece
            self._winner = game._winner
            self._turn = game._turn
            self._black_count = 2
            self._white_count = 2
            self._canvas = tkinter.Canvas(master = self._root_window, height = 650, width = 650, background = None)
            self._canvas.grid(row = 1, column = 0, padx = 15, pady = 15, sticky = tkinter.NSEW)
            self._info = tkinter.Frame(master = self._root_window, height = 150, width = 300, background = None)
            self._info.grid(row = 0, column = 0, sticky = tkinter.NS)
            othello_banner = tkinter.Label(master = self._info, font = ('Helvetica', 24, 'bold'), text = 'Othello: FULL')
            othello_banner.grid(row = 0, column = 2, sticky = tkinter.N)          
            self.game_info_banner()
            self._root_window.rowconfigure(0, weight = 1)
            self._root_window.columnconfigure(0, weight = 1)
            self._canvas.bind('<ButtonPress-1>', self.othello_game_click)
            self._canvas.bind('<Configure>', self.update_board)

    def create_game_board(self):
        '''
        Creates the game board
        '''
        self._canvas.delete(tkinter.ALL)
        width = self._canvas.winfo_width()/self._column
        height = self._canvas.winfo_height()/self._row                

        for col in range(self._column):
            for row in range(self._row):
                x1 = col*width
                y1 = row*height
                x2 = (col+1) * width
                y2 = (row+1) * height
                self._canvas.create_rectangle(x1, y1, x2, y2, fill = 'green', outline = 'black', tag = (width+1, height+1))
                if self._board[col][row] == 'B':
                        self._canvas.create_oval(x1, y1, x2, y2, fill = 'black')
                elif self._board[col][row] == 'W':
                        self._canvas.create_oval(x1, y1, x2, y2, fill = 'white')

        return self._board

    def game_info_banner(self):
        '''
        displays the the score
        along with whos current
        turn it is
        '''
        tkinter.Label(master = self._info, font = ('Helvetia', 20), text = 'Black: ' + str(self._black_count)).grid(row = 1, column = 0, sticky = tkinter.NSEW)
        tkinter.Label(master = self._info, font = ('Helvetia', 20), text = 'White: ' + str(self._white_count)).grid(row = 1, column = 3, sticky = tkinter.NSEW)
        tkinter.Label(master = self._info, font = ('Helvetica', 20), text = 'Turn: ' +str(self._turn)).grid(row = 1, column = 2, sticky = tkinter.NSEW)

    def count_pieces(self, string):
        '''
        keeps track how many pieces
        there are of each color in a
        string
        '''
        black = 0
        white = 0
        for disc in string:
            if disc == 'B':
                black += 1
            elif disc == 'W':
                white += 1
        return black, white

    def winner_banner(self, winner):
        '''
        takes in a winner of the game and
        prints the following depending on
        the outcome of the game
        '''
        if winner == True:
            tkinter.Label(master = self._info, text = 'Black is the Winner',
                    font = ('Helvetica', 20, 'bold')).grid(row = 3, column = 2, sticky = tkinter.NSEW)
        elif winner == False:
            tkinter.Label(master = self._info, text = 'White is the Winner',
                    font = ('Helvetica', 20, 'bold')).grid(row = 3, column = 2, sticky = tkinter.NSEW)
        elif winner == None:
            tkinter.Label(master = self._info, text = 'Tie game',
                    font = ('Helvetica', 20, 'bold')).grid(row = 3, column = 2, sticky = tkinter.NSEW)

    def extract_winner(self, string):
        '''
        finds out how the user would like
        to game to end by extracting info
        from modal dialog box
        '''
        if self._winner == 'M':
            return '>'
        elif self._winner == 'F':
            return '<'

    def othello_game_click(self, event):
         '''
         handles user selecting move, and flipping
         pieces corresponding to row and column
         '''

         try:         
             width = self._canvas.winfo_width()
             height = self._canvas.winfo_height()
             first_event = self._canvas.canvasx(event.x)
             second_event = self._canvas.canvasy(event.y)

             column_height = width / self._column
             row_width = height /self._row
             

             if self._game.check_if_any_move_exists() == True:
                 rowX = first_event/column_height
                 row = math.ceil(rowX)
                 colY = second_event/row_width
                 col = math.ceil(colY)
                 if self._game.valid_move(row-1, col-1) == True:
                     self._game.flip_pieces(row-1, col-1)
                         
                     self._turn = self._game.switch_player()
                     string = self._game.current_pieces_on_board()
                     self._black_count, self._white_count = self.count_pieces(string)
                     self.game_info_banner()

                     if self._game.check_if_any_move_exists() == False:
                         self._turn = self._game.switch_player()
                         self.game_info_banner()

                     if self._game.check_if_any_move_exists() == False:
                         self._turn = self._game.switch_player()
                         self.game_info_banner()
                         self.create_game_board()
                         determine_how_game_won = self.extract_winner(self._winner)
                         winner = self._game.winner(determine_how_game_won)
                         self.winner_banner(winner)
                         return
                     
                     self.create_game_board()

     
         except othello_logic.InvalidMoveError:
                 pass

                 
    def update_board(self, event):
        '''
        updates the game board
        '''
        return self.create_game_board()

    def GUI_start(self):
        '''
        the mainloop
        '''
        return self._root_window.mainloop()

class Othello_Menu:
    def __init__(self):
        '''
        Creates the a modal dialog box and asks user for options of Othello game
        '''
        self._root = tkinter.Tk()
        self._window = tkinter.Toplevel(master = self._root)
        self._window.title('Othello')

        greeting = tkinter.Label(self._window, text = 'Game Options', font = ('Helvetica', 16, 'bold'))
        greeting.pack()

        select_rows = tkinter.Label(self._window, text = 'Choose amount of rows', font =  ('Helvetica', 14))
        select_rows.pack()
        self._row = tkinter.Spinbox(master = self._window, values = (4,6,8,10,12,16), font = ('Helvetica', 14))
        self._row.pack()

        select_columns = tkinter.Label(self._window, text = 'Choose amount of columns', font =  ('Helvetica', 14))
        select_columns.pack()
        self._column = tkinter.Spinbox(master = self._window, values = (4,6,8,10,12,16), font = ('Helvetica', 14))
        self._column.pack()

        who_moves_first = tkinter.Label(self._window, text = 'Which player moves first', font = ('Helvetica', 14))
        who_moves_first.pack()
        self._who_moves_first = tkinter.Spinbox(master = self._window, values = ('B', 'W'), font = ('Helvetica', 14))
        self._who_moves_first.pack()

        top_left_piece = tkinter.Label(self._window, text = 'Choose top left piece', font = ('Helvetica', 14))
        top_left_piece.pack()
        self._top_left_piece = tkinter.Spinbox(master = self._window, values = ('B', 'W'), font = ('Helvetica', 14))
        self._top_left_piece.pack()

        winner = tkinter.Label(self._window, text = 'How would you like the game to end', font = ('Helvetica', 14))
        winner.pack()
        self._winner = tkinter.Spinbox(master = self._window, values = ('Most pieces on the board', 'Fewest pieces on the board'))
        self._winner.pack()

        start_button = tkinter.Button(master = self._window, text = 'GO!', font = ('Helvetica', 16), command = self.get_info)
        start_button.pack()


    def get_info(self):
        '''
        gets the info from the modal dialog box before it is destroyed
        '''
        self._rows = self._row.get()
        self._columns = self._column.get()
        self._turn = self._who_moves_first.get()
        self._first_piece = self._top_left_piece.get()
        self._how_winner = self._winner.get()[0]
        self._window.destroy()

    def othello(self):
        '''
        Initializes the Othello game
        '''
        return othello_logic.Othello(self._turn, (int(self._rows)), (int(self._columns)), self._first_piece, self._how_winner)


    def start(self):
        '''
        starts modal dialog box, which asks user for game options
        '''
        self._root.withdraw()
        self._window.wait_window()
        self._root.deiconify()


if __name__ == '__main__':
    game_options = Othello_Menu()
    game_options.start()
    game = game_options.othello()
    root = game_options._root
    othello_game = game_screen(game, root)
    othello_game.GUI_start()

                
