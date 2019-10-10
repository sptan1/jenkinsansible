def smallest(list1) :
	return (min(list1))

list = []
num = int(input("How many number to enter? : "))

for i in range(1,num+1):
        number=int(input("Enter a number: "))
        list.append(number)

print("The list is: {}".format(list))
print("The smallest number in the list is :",smallest(list))
