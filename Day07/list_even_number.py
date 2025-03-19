def list_even_numbers():
    try:
        given_list = input("Enter list of values (comma-separated): ")
        split_list = given_list.split(",")
        new_list = []

        for value in split_list:
            value = value.strip()  # Remove extra spaces
            if value.lstrip('-').isdigit():  # Handle negative numbers
                num = int(value)  # Convert to integer
                if num % 2 == 0:
                    new_list.append(num)
            else:
                print(f"Given value '{value}' is not valid")

        return new_list

    except Exception as e:
        print(f"An error occurred: {e}")


print(list_even_numbers())