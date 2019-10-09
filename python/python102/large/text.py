board = [[0,2,0], [0,0,0],[0,0,0]]

for row in board :
	print(row.count(row[0]))
	if row[0] ==0:
		print("End")

