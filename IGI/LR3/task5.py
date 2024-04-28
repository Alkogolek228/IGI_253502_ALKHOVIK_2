from misc import input_list, print_list, process_list, initialize_list

def task5():
    """
    Executes task 5.

    This function prompts the user to choose between manually inputting a list or generating a list.
    If the user chooses to input the list manually, it calls the input_list() function to get the list from the user.
    If the user chooses to generate the list, it prompts the user to enter the length of the list and calls the initialize_list() function to generate the list.
    After obtaining the list, it prints the list using the print_list() function.
    Then, it processes the list using the process_list() function to calculate the product of elements with even indices and the sum of elements between the first and last zero elements.
    Finally, it prints the calculated values or appropriate messages.

    Parameters:
    None

    Returns:
    None
    """
    choice = input("Enter '1' to input list manually, '2' to generate list: ")
    if choice == '1':
        lst = input_list()
    elif choice == '2':
        n = int(input("Enter list length: "))
        lst = initialize_list(n)
    else:
        print("Invalid choice. Exiting.")
        return

    print_list(lst)
    product, sum_between_zeros = process_list(lst)
    print(f"Произведение элементов с четными номерами: {product}")
    if sum_between_zeros is not None:
        print(f"Сумма элементов, расположенных между первым и последним нулевыми элементами: {sum_between_zeros}")
    else:
        print("В списке нет двух нулевых элементов.")