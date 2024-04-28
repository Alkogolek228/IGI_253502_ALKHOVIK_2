from misc import init_sequence_with_generator, init_sequence_with_user_input

def count_negative_numbers():
    """
    Counts the number of negative numbers in a sequence.

    The function prompts the user to choose a method for initializing the sequence.
    If the user chooses option 1, they will be asked to enter the length of the sequence
    and the sequence will be initialized using a generator.
    If the user chooses option 2, the sequence will be initialized by taking input from the user.
    After initializing the sequence, the function counts the number of negative numbers in the sequence
    and prints the result.

    Args:
        None

    Returns:
        None
    """
    sequence = []
    while True:
        choice = input("Выберите способ инициализации последовательности (1 - генератор, 2 - ввод пользователя): ")
        if choice == '1':
            n = int(input("Введите длину последовательности: "))
            sequence = init_sequence_with_generator(n)
            break
        elif choice == '2':
            sequence = init_sequence_with_user_input()
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите 1 или 2.")
    
    negative_numbers = sum(num < 0 for num in sequence)
    print(f"Количество отрицательных чисел в последовательности: {negative_numbers}")