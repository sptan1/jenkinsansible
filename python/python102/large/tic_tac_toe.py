import random

board = [ [0,0,0],[0,0,0],[0,0,0]]
print("   0  1  2")
count = 0 
for row in board :
	print(count, row)
	count += 1
game = "n"

print ("")
player = 1
while game == "n": 
	x = random.randint(0,2)
	y = random.randint(0,2)

	while board[x][y] != 0:
		x = random.randint(0,2)
		y = random.randint(0,2)
	board[x][y]=player

	print("Player : ", player)
		
	for row in board :
		print(row)

	for row in board:
		if row.count(row[0]) == len(row) and row[0] != 0 :
			game = "y"

	for col in range(len(board[0])):
		check = []
		for row in board:
			check.append(row[col])
		if check.count(check[0])== len(check) and check[0] !=0:
			game = "y"
	
	if board[0][0] == board[1][1] and board[0][0]== board[2][2] and board[0][0]!=0 :
		game = "y"

	if board[0][2] == board [1][1] and board [0][2] == board[2][0] and board[0][2]!=0:
		game="y"

	if game == "y" :
		print("Player", player, "is the winner!")

	temp = 0
	if game != "y" :
		for i in range(3):
			for j in range(3):
				if board[i][j] == 0:
					temp += 1

	if player == 1 :
		player = 2
	elif player == 2:
		player = 1
	
	print("")
	if temp == 0 and game !="y" :
		print ("Game Over!!No one win!!")
		break

