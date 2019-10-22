list = []
num = int(input("How many number to enter? : "))

for i in range(1,num+1):
	number=int(input("Enter a number: ")) 
	list.append(number) 

print("The even numbers in the list are : ", end="")
for j in list:
	if j % 2 ==0 :
		print(j, end=" ")
print("")
