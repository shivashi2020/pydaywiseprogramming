#Python program to find the sum of the digits of an integer using a while loop

givennumber = input("Enter an integer: ")
sum = 0
for value in givennumber:
    sum = sum + int(value)
print("Sum of digits {}".format(sum))
