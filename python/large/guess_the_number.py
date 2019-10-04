import random
print ("I am thinking of a number between 1 and 10.")
guess = 0
i = 0
again = "Y"
while again == "Y" :
    secret = random.randint(1,10)
    while guess != secret and i < 5:
        guess = int(input("What's the number? "))
        if guess > secret:
            print(f'{guess} is too high.')
        if guess < secret:
            print(f'{guess} is too low.')
        elif guess == secret :
            print("Yes! You Win!")
            break
        i +=1
        if i== 5:
            print("You ran out of guesses!")
        
    again = ""
    while again != "Y" and again != "N" :
        again = input("Do you want to play again (Y or N)? ")
        if again == "Y": 
            i = 0
        elif again == "N":
            print("Bye!")
            