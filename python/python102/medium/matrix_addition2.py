list1 = []
list2 = []
list3 = []
#num = int(input("Enter the length of lists : "))
n = int(input("Please enter the number of rows : "))
m = int(input("Please enter the number of columns : "))
for i in range(n):
	temp = []
	for j in range(m):
		number=int(input("Enter a number for [{}, {}] in the first matrix: ".format(i,j))) 
		temp.append(number)
	list1.append(temp) 

for i in range(n):
	temp = []
	for j in range(m):
		number=int(input("Enter a number for [{}, {}] in the second matrix: ".format(i,j)))
		temp.append(number)
	list2.append(temp)


for i in range(n):
	temp = []
	for j in range(m):
		x = list1[i][j] + list2[i][j]
		temp.append(x)
	list3.append(temp)

print("The first matrix is : ", list1)
print("The second matrix is : ", list2)
print("Result is : ", list3)

