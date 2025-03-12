# This function is to find factorial of number

def fact(number):
    factorial = 1
    if number <= 0 :
        print("Invalid Number")
        exit()
    else:
        factorial = 1
        for num in range(number, 0 , -1):
            factorial = factorial * num
        return factorial


print(fact(3))