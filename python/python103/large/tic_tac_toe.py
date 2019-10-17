board = [[" "," "," "],[" "," "," "],[" "," "," "]]
cont = "yes"

def checkboard(board,location):
	return (board[location[0]][location[1]] == " ")

def validateLocation(location):
	while location[0] >2 :
		s = int(input("Wrong size for row! Please enter 0-2 only: "))
		location = (s,location[1])
	while location[1] > 2 :
		s= int(input("Wrong size for column! Please enter 0-2 only: "))
		location = (location[0],s)
	return location

def validatePlayer(player):
	while player!="Y" and  player!="X" :
		player = input("Please enter \"X\" or \"Y\": ")
	return player


def b_status(board) :
	print("   0 1 2")
	for i in range(len(board[0])):
		for j in range(len(board[0])):
			if j==len(board[0])-1 :
				print("{}|".format(board[i][j]))
			elif j == 0 :
				print("{} |{}|".format(i,board[i][j]),end="")
			else :
				print("{}|".format(board[i][j]),end="")


def inputLocation():
	x =int(input("Please enter the move for row (0-2) : "))
	y =int(input("Please enter the move for column (0-2) : "))
	
	return (x,y)

def inputPlayer():
	player = input("You are X or Y: ")
	return player

def winner(board):
	wplay = " "
	cont = "yes"
	for row in board :
		if row.count(row[0]) == len(row) and row[0] != " ":
			cont = "no"
			wplay = row[0]
	
	for col in range(len(board[0])):
		check = []
		for row in board:
			check.append(row[col])
		if check.count(check[0]) == len(check) and check[0] != " ":
			cont = "no"
			wplay = check[0]

	if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] !=" ":
		cont = "no"
		wplay=board[0][0]
	
	if board[0][2] == board[1][1] and board[0][2] == board [2][0] and board[0][2] !=" ":
		cont = "no"
		wplay=board[0][2]
	
	return (cont,wplay)

def space(board):
	temp = 0
	cont = "yes"
	for i in range(len(board[0])):
		for j in range(len(board[0])):
			if board[i][j] == " ":
				temp +=1	

	if temp == 0:
		cont = "stop"
	return cont

def move(board, location, player):
	try:
		location = validateLocation(location)
		while (not checkboard(board,location)) :
			print("The location is occupied by {}".format(board[location[0]][location[1]]))
			location = inputLocation()
			location = validateLocation(location)
		player = validatePlayer(player)
		board[location[0]][location[1]] = player
		b_status(board)
			
	except IndexError:
		print("Wrong Size! Out of range!")	

b_status(board)

while cont == "yes" :
	location = inputLocation()
	player = inputPlayer()
	move(board,location, player)
	result = winner(board)	
	cont = result[0]
	if cont == "no":
		print("Player {} is the winner!".format(result[1]))
	elif cont =="yes":
		cont=space(board)
		if cont == "stop":
			print("Game Over. No winner!")


