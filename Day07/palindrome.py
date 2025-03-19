# Write a Python program that checks if a given string is a palindrome.

def check_palindrome():
    try:
        given_value = input("Enter value: ")
        check_value = given_value.strip()
        check_value = check_value.lower()
        revers_value = check_value[::-1]
        if check_value == revers_value:
            print(f"Given value {check_value} is palindrome")
        else:
            print(f"Given value {check_value} is not palindrome")
    except Exception as e:
        print(f"An error occurred: {e}")


check_palindrome()
