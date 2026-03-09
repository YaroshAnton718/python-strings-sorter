import sort as srt

def get_str(prompt, min_value, max_value):
    """
    Gets a string from the user.
    Validates the input.

    Args:
        prompt (str): The prompt to be displayed
        min_value (int): The minimum number of characters that user can enter
        max_value (int): The maximum number of characters that user can enter

    Returns:
        user_input (str): The user input
    """
    while True:
        user_input = input(prompt)
        if min_value <= len(user_input) <= max_value:
            return user_input
        else:
            print(f"Enter the number of characters between {min_value} and {max_value}.")
            continue

def get_int(prompt, min_value, max_value):
    """
    Gets an integer from the user.
    Validates the input.

    Args:
        prompt (str): The prompt to be displayed
        min_value (int): The minimum value that user can enter
        max_value (int): The maximum value that user can enter

    Returns:
        user_input (int): The user input
    """
    while True:
        try:
            user_input = int(input(prompt))
            if min_value <= user_input <= max_value:
                return user_input
            else:
                print(f"Please enter a number between {min_value} and {max_value}.")
                continue
        except ValueError:
            print("Please enter an integer number.")
            continue

def get_input():
    """
    Gets parameters user_num and user_str.
    Calls the functions get_int(), get_str() and str_sort().
    """
    user_num = get_int("Enter a number of strings [2-10]: ", 2, 10)

    strings = []
    for i in range(user_num):
        user_str = get_str(f"Enter a string {i+1} (number of characters [1; 10]): ", 1, 10)
        strings.append(user_str)

    print("Your strings:")
    for string in strings:
        print(string)

    srt.str_sort(strings)

def print_result(strings):
    """
    Prints out the results of sorting.

    Args:
        strings (list): A list of strings
    """
    print("\nSorted strings:")
    for string in strings:
        print(string)
