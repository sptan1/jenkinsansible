list = []
multi=[]
num = int(input("How many number to enter? : "))

for i in range(1,num+1):
	number=int(input("Enter a number: ")) 
	list.append(number) 

factor = int(input("Enter a factor number: "))

for j in list:
	m = j * factor
	multi.append(m)
print("The new list of numbers are: ", multi)
