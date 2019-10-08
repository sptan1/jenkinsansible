num = int(input("How many numbers or strings you want to enter? "))
lists=[]
new_s = []
for i in range(1,num+1):
        s=input("Enter a number or a string: ")
        lists.append(s)

for i in range(num):
	if lists[i] not in new_s :
		new_s.append(lists[i])

#new_s = "".join(new_s)
print("Result of remove duplicate values: ", new_s)
