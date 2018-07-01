import random

print("Welcome to Nim Game!")
start = input("Press 'Y' to begin: ")

if start == 'Y':
    num = random.randint(10,25)
    print("We will start with ",num)

    while num != 0:

        #UserMove
        inp = int(input("Your move! Enter a number: "))
        if inp<0 or inp >3 :
            inp = int(input("Please enter a number between 1 and 3: "))
        num = num - inp
        print("Number is",num)
        if num == 0 :
            print("You Win!")
            break

        n = random.randint(1,3)
        if num <= 3:
            n = num
        print("I choose",n)
        num = num-n
        print("Number is",num)

        if num == 0:
            print("I Win!")
            break
