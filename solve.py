import numpy as npy

from getBoards import getBoard



def valid(x, y, num,board):
	for i in range(0,9):
		if board[x][i] == num:
			return False
	for j in range(0,9):
		if board[j][y] == num:
			return False
	xbox = (x // 3) * 3
	ybox = (y // 3) * 3
	for i in range(0,3):
		for j in range(0,3):
			if board[xbox+i][ybox+j] == num:
				return False
	return True


def solve(board):
	for i in range(9):
		for j in range(9):
			if board[i][j] == 0:
				for k in range(1,10):
					if valid(i,j,k,board):
						board[i][j] = k
						solve(board)
						board[i][j] = 0
				return
	print(npy.matrix(board))

def getLevel():
	while True:
		try:
			level = int(input("What level of the NYTimes sudoku would you like solved? (1, 2 or 3)"))

		except ValueError:
			print("Please enter only 1, 2 or 3")
			continue

		if level < 1 or level > 3:
			print("Please enter only 1, 2 or 3")
			continue
		else:
			break


	return level-1


if __name__ == '__main__':
	# print(valid(0,2,3))

	solve(getBoard(getLevel()))

