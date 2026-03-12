from flask import Flask, request, jsonify

app = Flask(__name__)

def check(board,p):
    w=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for a,b,c in w:
        if board[a]==board[b]==board[c]==p:
            return True
    return False

def minimax(board,ismax):
    if check(board,"O"):
        return 1
    if check(board,"X"):
        return -1
    if "" not in board:
        return 0
    if ismax:
        best=-100
        for i in range(9):
            if board[i]=="":
                board[i]="O"
                score=minimax(board,False)
                board[i]=""
                best=max(score,best)
        return best
    else:
        best=100
        for i in range(9):
            if board[i]=="":
                board[i]="X"
                score=minimax(board,True)
                board[i]=""
                best=min(score,best)
        return best

def best_move(board):
    best=-100
    move=-1
    for i in range(9):
        if board[i]=="":
            board[i]="O"
            score=minimax(board,False)
            board[i]=""
            if score>best:
                best=score
                move=i
    return move

@app.route("/move",methods=["POST"])
def move():
    board=request.json["board"]
    m=best_move(board)
    return jsonify({"move":m})

if __name__=="__main__":
    app.run(host="0.0.0",port=5000)