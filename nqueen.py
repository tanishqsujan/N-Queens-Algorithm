import time


def print_board(board, n):
	for i in range(n):
		for j in range(n):
			print(board[i][j], end = " ")
		print()

def add_sol(board, ans, n):
	temp = []
	for i in range(n):
		string = ""
		for j in range(n):
			string += board[i][j]
		temp.append(string)
	ans.append(temp)
	
	

def is_safe(row, col, board, n):
	x = row
	y = col

	while(x>=0):
		if board[x][y] == "Q":
			return False
		else:
			x -= 1
			

	x = row
	y = col
	while(y<n and x>=0):
		if board[x][y] == "Q":
			return False
		else:
			y += 1
			x -= 1

	x = row
	y = col
	while(y>=0 and x>=0):
		if board[x][y] == "Q":
			return False
		else:
			x -= 1
			y -= 1
	return True


def solveNQueens(row, ans, board, n):
	

	if row == n:
		add_sol(board, ans, n)
		return
	
	
	for col in range(n):
		
		
		if is_safe(row, col, board, n):

			board[row][col] = "Q"
			solveNQueens(row+1, ans, board, n)
			

			board[row][col] = "."
if __name__ == "__main__":
	n = 4
	board = [["." for i in range(n)] for j in range(n)]

	ans = []
	solveNQueens(0, ans, board, n)
	
	if ans == []:
		print("Solution does not exist")
	else:
		print(len(ans))
		print(f"Out Of {len(ans)} solutions is following")
		print_board(ans[0], n)
	
		
