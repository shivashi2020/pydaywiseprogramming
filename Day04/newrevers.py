#10. Python program to display the given integer in a reverse manner

try:
    integervalue = input("Enter Integer Value \n")
    if int(integervalue) != 0:
        print(integervalue[::-1])
    else:
        print("Given value is Zeror")
except ValueError:
    print("Enter valid value")
