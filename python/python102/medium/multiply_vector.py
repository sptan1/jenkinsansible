list1 = []
list2 = []
list3 = []
num = int(input("Enter the length of lists : "))

for i in range(1,num+1):
	number=int(input("Enter a number for first list: ")) 
	list1.append(number) 

for j in range(1,num+1):
        number=int(input("Enter a number for second list: "))
        list2.append(number)

for k in range(1,num+1):
	m = list1[k-1] * list2[k-1] 
	list3.append(m)

print(list1, "x" , list2 , "=", list3)
