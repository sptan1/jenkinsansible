string = input("Please enter your Encrypted sentence: ")
l_str = list(string)
length = len(string)

array1 =  {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 
        'f' : 6, 'g' : 7, 'h' : 8, 'i' : 9, 'j' : 10, 
        'k' : 11, 'l' : 12, 'm' : 13, 'n' : 14, 'o' : 15, 
        'p' : 16, 'q' : 17, 'r' : 18, 's' : 19, 't' : 20, 
        'u' : 21, 'v' : 22, 'w' : 23, 'x' : 24, 'y' : 25, 'z' : 26} 
array2 = {0 : 'z', 1 : 'a', 2 : 'b', 3 : 'c', 4 : 'd', 5 : 'e', 
        6 : 'f', 7 : 'g', 8 : 'h', 9 : 'i', 10 : 'j', 
        11 : 'k', 12 : 'l', 13 : 'm', 14 : 'n', 15 : 'o', 
        16 : 'p', 17 : 'q', 18 : 'r', 19 : 's', 20 : 't', 
        21 : 'u', 22 : 'v', 23 : 'w', 24 : 'x', 25 : 'y'} 

for i in  range(length) :
	if l_str[i] != " " :
		tmp = (array1[l_str[i]]-13+26)%26
		l_str[i] =array2[tmp] 

new_str = "".join(l_str) 

print("The plaintext is: ", new_str)
