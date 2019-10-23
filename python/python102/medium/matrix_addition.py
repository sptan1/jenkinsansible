list1 = []
list2 = []
list3 = []
#num = int(input("Enter the length of lists : "))
dim = 2
for i in range(dim):
	temp = []
	for j in range(dim):
		number=int(input("Enter a number for {},{} in the first matrix: ".format(i,j))) 
		temp.append(number)
	list1.append(temp) 

for i in range(dim):
	temp = []
	for j in range(dim):
		number=int(input("Enter a number for {},{} in the second matrix: ".format(i,j)))
		temp.append(number)
	list2.append(temp)


for i in range(dim):
	temp = []
	for j in range(dim):
		x = list1[i][j] + list2[i][j]
		temp.append(x)
	list3.append(temp)

print("The first matrix is : ")
for row in range(dim):
	for col in range(dim):
		print(list1[row][col], end = " " )
	print()

print("The second matrix is : ")
for row in range(dim):
	for col in range(dim):
		print(list2[row][col], end = " ")
	print()

print("The result of addition is : ")
for row in range(dim) :
	for col in range(dim):
		print(list3[row][col], end = " " )
	print()
