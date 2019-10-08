coin =0
cont="yes"
while cont == "yes" :
    print(f'You have {coin} coins.')
    cont = input("Do you want another? ")
    coin+=1
    if cont.lower() == "no" :
        print("Bye")
        