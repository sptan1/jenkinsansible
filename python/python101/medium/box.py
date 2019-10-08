witdh = int (input("Width? "))
height = int(input("Height? "))
i=1
while i <= height :
    if i == 1 or i == height :
        print("*" * witdh)
    else:
        w=1
        while w <= witdh :
            if w == 1 :
                print("*", end ="")
            elif w == witdh :
                print("*")
            else:
                print(" ", end=""),
            w+=1

    i+=1