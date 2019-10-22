def shortest(list1) :
	return (min(list1,key=len))

list = []
num = int(input("How many strings do you want to enter? : "))

for i in range(1,num+1):
        s=input("Enter a string: ")
        list.append(s)

print("The strings are: {}".format(list))
print("The shortest string in the list is :",shortest(list))
