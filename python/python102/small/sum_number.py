list = []
num = int(input("How many number to enter? : "))
sum=0

for i in range(1,num+1):
	number=int(input("Enter a number: ")) 
	list.append(number) 

	sum = sum + number 

print("Sum of the numbers is : ", sum)
