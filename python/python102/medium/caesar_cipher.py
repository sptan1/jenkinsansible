message = input("Please enter a sentence to encript: ")
l_mes = list(message)
length_mes = len(message)

for i in range(length_mes) :
	if l_mes[i] != " " :
		tmp = ord(l_mes[i])+13
		if tmp > ord('z') :
			tmp = tmp - 26
		l_mes[i] = chr(tmp)
new_mes = "".join(l_mes)

print("The encrypted message are : ", new_mes)

string = input("Please enter your Encrypted sentence: ")
l_str = list(string)
length = len(string)

for i in  range(length) :
	if l_str[i] != " " :
		tmp = ord(l_str[i]) -13
		if tmp < ord('a') :
			tmp = tmp+26
		l_str[i] =chr(tmp) 

new_str = "".join(l_str) 

print("The plaintext is: ", new_str)
