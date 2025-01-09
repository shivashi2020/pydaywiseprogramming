#Python program to check whether the given integer is a multiple of 5

def ismultipleoffive():
    try:
        givennumber = int(input("enter number \n"))
        if givennumber % 5 ==0 :
            print("{} is multiple of 5".format(givennumber))
        else:
            print("{} is not multiple of 5".format(givennumber))
    except ValueError:
        print("Enter valid number")

ismultipleoffive()
