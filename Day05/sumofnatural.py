# Sum of Natural numbers

try:

    natural_numbers = input("Enter numbers spearated by coma : ")
    number_split = natural_numbers.split(",")
    sum = 0
    for numb in number_split:
        sum = sum + int(numb.strip())

    print(sum)
except Exception as e:
    print(f"An error occurred: {e}")



