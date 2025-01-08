# 4. Python program to find out the average of a set of integers

mylist = []
try:
    total_numbers = int(input("'how many numbers?  '"))
    for i in range(total_numbers):
        value = int(input("Enter {} number ".format(i)))
        mylist.append(value)

    sumoflist = sum(mylist)
    average = sumoflist/len(mylist)
    print("average of a set of integers is {}".format(average))

except ValueError:
    print("Please enter a valid numerical value.")



