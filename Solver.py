import sys, copy, time

class SearchMethod():
    def __init__(self) -> None:
        self.min = sys.maxsize * -1
        self.max = sys.maxsize

    def helper_minimax(self, board, depth, isMax, report:dict):
        if depth == report.get("max_depth"):
            return 0
        #save the depth
        if depth > report["depth"]:
            report["depth"] = depth
        result = board.check_winner()
        if result != 0:
            return result
        if isMax:
            best_score = self.min
            for i in range(len(board.board)):
                for o in range(len(board.board[0])):
                    #check for available spot
                    if (board.board[i][o] == "-"):
                        #make a copy of current state
                        new_board = copy.deepcopy(board)
                        #make a move
                        new_board.set_move(o+1,i+1)
                        #increment expanded nodes
                        report["node"] += 1
                        #recursion
                        score = self.helper_minimax(new_board, depth+1, False, report)
                        #get MAX
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = self.max
            for i in range(len(board.board)):
                for o in range(len(board.board[0])):
                    #check for available spot
                    if (board.board[i][o] == "-"):
                        #make a copy of current state
                        new_board = copy.deepcopy(board)
                        #make a move
                        new_board.set_move(o+1,i+1)
                        #increment expanded nodes
                        report["node"] += 1
                        #recursion
                        score = self.helper_minimax(new_board, depth+1, True, report)
                        #get MIN
                        best_score = min(score, best_score)
            return best_score

    def minimax(self,board, max_depth):
        best_score = self.min
        move = [0,0]
        report = {
            "max_depth":max_depth,
            "node": 0,
            "depth": 0
        }
        for i in range(len(board.board)):
            for o in range(len(board.board[0])):
                #check if there is an available spot
                if (board.board[i][o] == "-"):
                    new_board = copy.deepcopy(board)
                    new_board.set_move(o+1,i+1)
                    report["node"] += 1
                    score = self.helper_minimax(new_board, 0, True,report)
                    if score > best_score:
                        move[0], move[1]= o+1,i+1

        return (move[0],move[1],report)

    def ab(self,board, max_depth):
        best_score = self.min
        move = [0,0]
        report = {
            "max_depth":max_depth,
            "node": 0,
            "depth": 0
        }
        for i in range(len(board.board)):
            for o in range(len(board.board[0])):
                #check if there is an available spot
                if (board.board[i][o] == "-"):
                    new_board = copy.deepcopy(board)
                    new_board.set_move(o+1,i+1)
                    report["node"] += 1
                    score = self.helper_ab(new_board, 0, True, self.min, self.max, report)
                    if score > best_score:
                        move[0], move[1]= o+1,i+1

        return (move[0],move[1],report)

    def helper_ab(self, board, depth, isMax, alpha, beta, report:dict):
        if depth == report.get("max_depth"):
            return 0
        result = board.check_winner()

        if depth > report["depth"]:
            report["depth"] = depth
        if result != 0:
            return result
        if isMax:
            best_score = self.min
            # for i in board.available_move:
            for i in range(len(board.board)):
                for o in range(len(board.board[0])):
                    if (board.board[i][o] == "-"):

                        new_board = copy.deepcopy(board)
                        new_board.set_move(o+1,i+1)
                        report["node"] += 1
                        score = self.helper_ab(new_board, depth+1, False, alpha, beta, report)
                        best_score = max(score, best_score)
                        #pruning
                        alpha = max( alpha, best_score)
                        if beta <= alpha:
                            break
            return best_score
        else:
            best_score = self.max
            for i in range(len(board.board)):
                for o in range(len(board.board[0])):

                    if (board.board[i][o] == "-"):
                        new_board = copy.deepcopy(board)
                        new_board.set_move(o+1,i+1)
                        report["node"] += 1
                        score = self.helper_ab(new_board, depth+1, True, alpha, beta, report)
                        best_score = min(score, best_score)
                        beta = min( beta, best_score)
                        #pruning
                        if beta <= alpha:
                            break
            return best_score
