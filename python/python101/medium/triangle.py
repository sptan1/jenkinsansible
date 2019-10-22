height = 4
w=height

for i in range (0,height) :
    for j in range ( 0, w ):
        print (end=" ")
    
    w = w -1

    for j in range (0, (2 * i + 1) ):
        print("*", end="")

    print(" ")

