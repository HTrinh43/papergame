import copy
from mimetypes import init
class Board():
    def __init__(self,x,y) -> None:
        #in the empty_spot_list, (x,y) x is row, y is column
        self.board = self.generate_board(x,y)
        self.x = x-1
        self.y = y-1
        self.current_player = "O"
        self.empty_spot = x * y
        

        

    def generate_board(self,x,y):
        row = ["-"]*x
        board = list()
        for i in range(y):
            board.append(copy.copy(row))
        return board

    def print_board(self):
        print()
        print("   ",end="")
        for i in range(self.x+1):
            print(i+1, end="    ")
        print()
        for i in range(self.y+1):
            print(i+1, end="")
            print(self.board[i])


    def set_move(self,x,y):
        """
        Return 1 if set the move successfully
                -1 if failed
        """
        if self.check_input(x,y) == 1:
            if self.board[y-1][x-1] is '-':
                self.board[y-1][x-1]= self.current_player
                self.empty_spot-=1
                self.current_player = 'O' if self.current_player == 'X' else 'X' 
                self.disable_block(x-1,y-1)
                return 1
            else:
                print("This block is not available.")
                return -1

    def disable_block(self,x,y):
        for i in range(-1,2):
            for o in range(-1,2):
                if x+o>=0 and y+i>=0 and x+o<len(self.board[0]) and y+i<len(self.board) and self.board[y+i][x+o] is "-":
                    self.board[y+i][x+o] = "/"
                    self.empty_spot-=1

    def check_input(self,x,y):
        return 1

    def check_winner(self):
        if self.empty_spot == 0:
            winner = "Player" if self.human != self.current_player else "AI"
            # print("The winner is {}".format(winner))
            return 100 if winner == "Player" else -100
        return 0

    def set_player(self, i):
        """
        Set who will make the first move
        """
        self.human = "O" if i == 2 else "X"
        self.AI = "X" if i == 2 else "O"

    def get_current_player(self):
        return "Human" if self.human == self.current_player else "AI"
