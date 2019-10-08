list = []
num = int(input("How many number to enter? : "))

for i in range(1,num+1):
	number=int(input("Enter a number: ")) 
	list.append(number) 

print("Largest number in the list is: ", min(list))
