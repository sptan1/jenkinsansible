factor = int (input("Please enter a number>> "))
print(f'The factor for {factor} are: ')
for i in range (1,factor+1):
    if factor % i == 0 :
        print(i)
