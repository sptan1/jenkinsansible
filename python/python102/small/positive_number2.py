list = []
positive=[]
num = int(input("How many number to enter? : "))

for i in range(1,num+1):
	number=int(input("Enter a number: ")) 
	list.append(number) 

for j in list:
	if j > 0 :
		positive.append(j)
print("The new list of numbers are: ", positive)
