list = []
num = int(input("How many number to enter? : "))

for i in range(1,num+1):
	number=int(input("Enter a number: ")) 
	list.append(number) 

print("The positive numbers in the list are : ", end="")
for j in list:
	if j > 0 :
		print(j, end=" ")
print("")
