from copy import deepcopy
def createBoard(n):
    board = []
    for i in range(n):
        board.append(["."] * n)
    return board
n = 4
col = set()
posDiag = set()  # (r + c)
negDiag = set()  # (r - c)
board = createBoard(n)
res = []
def backtrack(r):
    #base condition
    if r == n:
        copy = deepcopy(board)
        res.append(copy)
        return
    # try placing in each position in row (r)
    for c in range(n):
        if c not in col and (r + c) not in posDiag and (r - c) not in negDiag:
            #add        
            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = "Q"

            #try next row
            backtrack(r + 1)

            # adding done, backtrack
            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = "_"


backtrack(0)

# print(len(res))
for i in range(len(res)):
    # print(i+1, ":")
    for row in res[i]:
        print(*row)
    print()
    print()
