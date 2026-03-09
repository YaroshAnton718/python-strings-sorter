import utils as ut

def main():
    """
    The main function.
    Calls one function and gets the choice to user.
    """
    while True:
        print("----------Strings Sort----------")
        ut.get_input()

        while True:
            choice = input("\nWould you like to continue (y/n)? ")
            if choice == "y" or choice == "Y":
                break
            elif choice == "n" or choice == "N":
                return
            else:
                print("Please enter y or n.")
                continue


if __name__ == '__main__':
    main()