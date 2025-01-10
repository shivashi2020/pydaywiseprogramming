#8. Python program to check whether the given integer is a multiple of both 5 and 7

try:
    giveint = int(input("Enter an integer value \n"))
    if giveint % 5 ==0 and giveint % 7 ==0:
        print("Given Integer {} is multiple of both 5 and 7".format(giveint))
    else:
        print("Given Integer {} is not multiple of both 5 and 7".format(giveint))
except ValueError:
    print("Enter valid Number")

