"""
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by
the British mathematician John Horton Conway in 1970."
The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or
dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the
following four rules (taken from the above Wikipedia article):
1. Any live cell with fewer than two live neighbors dies as if caused by under-population.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by over-population.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births
and deaths occur simultaneously. Given the current state of the mx n grid board, return the next state.
"""
def gameoflife(board):
    
    rows, cols = len(board),len(board[0])
    direction = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
    
    def checkneighborsum(r,c):
        neigh = 0
        for dr,dc in direction:
            if r+dr in range(rows) and c+dc in range(cols):
                neigh += board[r+dr][c+dc]
        
        return neigh
 
    change = False
    
    for row in range(rows):
        for col in range(cols):
            val = checkneighborsum(row,col)
            
            if board[row][col] == 0:
                if val == 3:
                    change = True
                    board[row][col] = 1
            if board[row][col] == 1:
                if val < 2:
                    change = True
                    board[row][col] = 0
                if val > 3:
                    change = True
                    board[row][col] = 0
            
    if change == True:
        gameoflife(board)
    
    return board
            
            
board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
#board = [[1,1],[1,0]]


for each in (gameoflife(board)):
    print(each)