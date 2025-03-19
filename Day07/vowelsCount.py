# Write a Python program that counts the number of vowels in a given string.
#(a, e, i, o, u) 

def count_vowels():
    try:
        mydic = {}
        vowels = ['a','e','i','o','u']
        give_string = input("Enter string value: ")
        for val in vowels:
            if val in give_string:
                mydic[val] = give_string.count(val)
        return mydic
    except Exception as e:
        print(f"An error occurred: {e}")


print(count_vowels())