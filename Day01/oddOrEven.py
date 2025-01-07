# 1. Python program to check whether the given number is even or not.


def oddoreven():
    try:
        givennumber = int(input("Enter your number \n"))
        if givennumber % 2 == 0 :
            print("Given number is EVEN")
        else:
            print("Given number is ODD")
    except ValueError:
        print("Please enter a valid numerical value.")

oddoreven()


