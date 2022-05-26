from Board import Board
from Solver import SearchMethod
import copy, time, os
def getUserInput(first_time):
    if first_time is False:
        print("A paper/pencil game\nPlease choose the first player and Algorithm.")
        print('[player] choose if AI is player “1” or player “2”')
        print('[searchmethod] can be MM (for minimax) or AB (for minimax with alpha- beta pruning)')
    print("[player] [searchmethod]: ", end="")
    user_input = input()
    cmd = user_input.split(" ")
    algorithm = ["MM","AB"] 
    if (len(cmd) == 2):
        player = cmd[0]
        algo = cmd[1]
        
        if (player != "1" and player != "2"):
            print("\tPlease choose 1 or 2 for [player]")
        elif (algo not in algorithm):
            print("\tPlease choose MM or AB for [searchmethod]")
        else:
            return (int(player),algo)
    
    else:
        print("\tWrong input. Example: 1 AB")
    return -1
    
def getUserMove(b_x,b_y):
    user_input = input("[x] [y]: ")
    pos = user_input.split(" ")
    if len(pos) == 2:
        x,y = pos[0], pos[1]
        if x.isdigit() and y.isdigit():
            if int(x) <= b_y + 1 and int(y) <= b_x + 1:          
                return (int(x), int(y)) 
            else:
                print("\tMust be numbers.")
    print("\tWrong input.")
    return -1
        


if __name__ == "__main__":
    searchmethod = SearchMethod()
    board = Board(7,6)
    first_time = False
    report = {
        "max_depth": 5,
        "node": list(),
        "depth": 0
    }
    #get input for first move and search method
    while (True):
        user_input = getUserInput(first_time)
        first_time = True
        if user_input != -1:
            break
    board.set_player(user_input[0])
    method = user_input[1]
    while (True):
        if board.get_current_player() == "Human":
            user_move = getUserMove(board.y, board.x)
            if user_move != -1:
                board.set_move(user_move[0],user_move[1])
                board.print_board()
            #AI vs AI
            # if method == "MM":
            #     x,y,r = searchmethod.minimax(board, report["max_depth"])
            # else:
            #     x,y,r = searchmethod.ab(board, report["max_depth"])
            # board.set_move(x,y)
            # board.print_board()
        else:
            #
            if method == "MM":
                x,y,r = searchmethod.minimax(board, report["max_depth"])
            else:
                x,y,r = searchmethod.ab(board, report["max_depth"])
            board.set_move(x,y)
            report.get("node").append(r.get("node"))
            if report["depth"] < r.get("depth"):
                report["depth"]= r.get("depth")
            board.print_board()
            # pass
        
        if board.check_winner() != 0:
            print("current player:{} \nhuman:{}\nAI:{}".format(board.current_player,board.human,board.AI))
            if board.check_winner() == 100:
                print("The human won.")
            else:
                print("The AI won.")
            break

    print("Board size: {}x{}".format(board.x+1,board.y+1))
    print("Algorithm: {}".format(user_input[1]))
    print("Max depth: {}".format(report["max_depth"]))
    print("Depth level for look-ahead: {}".format(report["depth"]))
    print("Expanded nodes each move: ")
    print(report["node"])

