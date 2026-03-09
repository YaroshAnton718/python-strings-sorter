import utils as ut

def str_sort(strings):
    """
    Sorts the strings using improved Bubble sort.

    Args:
        strings (list): list of strings
    """
    # Improved bubble sort
    n = len(strings)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if strings[j] > strings[j+1]:
                strings[j], strings[j+1] = strings[j+1], strings[j]
                swapped = True
        if not swapped:
            break

    ut.print_result(strings)