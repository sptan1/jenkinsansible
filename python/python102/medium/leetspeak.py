string = input("Please enter a sentence: ")

l_string = list(string)
length = len(string)
for s in range(length) :
	if l_string[s] == "a" or l_string[s] == "A":
		l_string[s]= "4"
	elif l_string[s] == "E" or l_string[s] =="e":
		l_string[s] = "3"
	elif l_string[s] == "G" or l_string[s] =="g":
		l_string[s]="6"
	elif l_string[s]== "I" or l_string[s] =="i":
		l_string[s]="1"
	elif l_string[s] == "O" or l_string[s] =="o":
		l_string[s]="0"
	elif l_string[s]=="S" or l_string[s] =="s":
		l_string[s] = "5"
	elif l_string[s] == "T" or l_string[s] =="t":
		l_string[s] = "7"

new_string = "".join(l_string)
print("Leetspeak translation: ",new_string)
