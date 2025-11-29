import time

#print the board
def print_board(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()
        
#Joining "." and "Q"
#making combined array
#For output in designed format
def add_soln(board, ans, n):
    temp = []
    for i in range(n):
        string = ""
        for j in range(n):
            string += board[i][j]
        temp.append(string)
        
#We need to check in three directions
#1. In the same column above the current position
#2. In the left top diagonal from the given cell
#3. In the right top diagonal from the given cell

def is_safe(row, col, board, n):
    x = row
    y = col
    
    #Check for same upper col
    while(x >=0):
        if board[x][y] == "Q":
            return False
        else:
            x -= 1
            
    #Check for Upper right diagonal
    x = row
    y = col
    
    while(y<n and x>=0):
        if board[x][y] == "Q":
            return False
        else:
            y += 1
            x -= 1
            
    #Check for upper left diagonal
    x = row
    y = col
    
    while(y >= 0 and x >= 0):
        if board[x][y] == "Q":
            return False
        else:
            x -= 1
            y -= 1
            
    return True

def solveNQueens(row, ans, board, n):
    
    #Base case
    #Queen is depicted by "Q"
    #Adding solution to final answer array
    if row == n:
        add_soln(board, ans, n)
        return
    
    #Solve 1st case and rest recursion will follow
    for col in range(n):
        if is_safe(row, col, board, n):
            board[row][col] = "Q"
            solveNQueens(row + 1, ans, board, n)
            
            #Backtrack
            board[row][col] = "."
            
if __name__ == "__main__":
    
    n= 4
    
    #2D array of string will make our board which is initially all empty
    board = [["." for i in range(n)] for j in range(n)]
    
    #Store all possible answers
    ans = []
    solveNQueens(0, ans, board, n)
    
    if ans == []:
        print("Solution does not exisit")
    else:
        print(len(ans))
        print(f"Out of {len(ans)} solutions one is following")
        print_board(ans[0], n)