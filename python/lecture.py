# strings
#"Hello everyone"

#"""
#Hello everyone
#Hello everyone
#Hello everyone
#"""

#print('Hello World')

#type('Hello World')
#print(type("Hello World"))

#print('abc')
#print('dfg')

#print('abc'+'dfg')

#print("This is a great day. \nAnd I think that i will fly")

#print(True)
#print('True')

#print(type(True))
#print(type('True'))

# print(5+4.4)
# print(5+True)

# myVar = "Hello world"
# print(myVar)

# x =4
# y=5

# print(x, y)

# my_fir_var=23
# my_sec_var="Houston"

# print("Hello World {} {}".format(my_fir_var,my_sec_var))

# print("Hello World {1} {0} {1} {1}".format(my_fir_var,my_sec_var))

# my_var1 = "Hello"
# my_var2 = "World"
# print(f'Parameters {my_var1}:{my_var2}')

# %s = string
# %d = integer
# %f = float (decimal)
# %e = float (exponent)
# name = "Carlos"
# age = 23

# sentence = "%s is %d years old" % (name,age)
# print(sentence)

#print(isinstance(5,int))

# print(abs(-5))
# print(pow(2,4))
# print(round(5.4))

# import math
# x= math.cos(2)
# print(x)

# name =input("what is your name:")
# # print ("your name is" , name)
# print(f'user\'s name is {name}')

# year=input("your year:")
# print(f'the year of {name} is {year}')
# print(f'the data type of year is {type(year)}')
# year=int(year)
# print(f'after change,the data type of year is {type(year)}')

# test = (5 == 4)
# print(test)

# a = True
# b = False
# print("a and b is ", a and b)
# print("a or b is", a or b)
# print("not a is", not a)

# name = "Alim"

# # if name == "Alimm" :
# #     print(name)
# #     print(name)

# # print(name)

# if name == "Alim" :
#     print("your are", name)
# else:
#     print("Your are not", name)

# age_s = input("what is your age>>")
# age= int(age_s)

# if age >= 21:
#     print("You are getting a free beer!")
# elif age < 18:
#     print("what are you even doing here?")
# else:
#     print("sorry no beer for you")



# greeting = "Hello {}, it is very nice to meet you and your friend {}!"

# name_of_user = input("What is your name? ")
# length_of_name = len(name_of_user)
# if length_of_name > 0 and length_of_name < 10:
#     name_of_friend = input("What is your friend's name? ")
#     length_of_friendname = len(name_of_friend)
#     if length_of_friendname > 0:
#         print(greeting.format(name_of_user, name_of_friend))
#     else:
#         print(f'Nice to meet you {name_of_user}!')
# elif length_of_name >10:
#     short_name = input(f'Hi {name_of_user}, how to call you in short name?>>')
#     print(f'{short_name}! What a lovely name!')
# else:
#     print("OK, I'll ask again some other time.")


# x=4
# x+=2  # x = x+2 =6

# print(x)


# count =0
# while count <10 :
#     count +=1
#     print("this count",count)

# answer=""
# while answer != "when" :
#     answer = input('Say when: ')
#     answer = answer.lower()
# print("Cheese")

# while True:
#   answer = input('Say when: ')
#   if answer.lower() == 'when':
#     break
# print("Cheese")


# greeting = "Hello {}, it is very nice to meet you and your friend {}!"

# length_of_name = 0
# length_of_friendname = 0

# while length_of_name == 0:
#     name_of_user = input("What is your name? ")
#     length_of_name = len(name_of_user)
#     while length_of_name > 10 or length_of_name == 0 : 
#         short_name = input(f'Hi {name_of_user}, how to call you in short name?>>')
#         length_of_name = len(short_name)
#         if length_of_name !=0 :
#             name_of_user = short_name

# while length_of_friendname == 0:
#         name_of_friend = input("What is your friend's name? ")
#         length_of_friendname = len(name_of_friend)
        
# print(greeting.format(name_of_user, name_of_friend))


count = 0
input_string = input("How high should we count? ")
try:
    MAX = int(input_string)
    while (count < MAX):
        print(count)        
        count += 1    
except ValueError:
    print("Please run the program again and type a number!")