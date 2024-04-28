import random
import string
import time

def timer_decorator(func):
    """
    A decorator function to measure the execution time of a function.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print("Execution time: {} seconds".format(end_time - start_time))
        return result
    return wrapper

@timer_decorator
def repeat_function(func):
    while True:
        func()
        repeat = input("Хотите повторить выполнение функции? (да/нет): ")
        if repeat.lower() != 'да':
            break
        
def input_x():
    while True:
        x = float(input("Enter a value for x (abs(x) < 1): "))
        if abs(x) < 1:
            break
        else:
            print("Invalid input. Please enter a value for x such that abs(x) < 1.")
    return x

def init_sequence_with_generator(n):
    """
    Initialize a sequence with random numbers using a generator.

    Args:
        n (int): The length of the sequence.

    Returns:
        list: A list of random numbers.
    """
    sequence = [next(random_number_generator()) for _ in range(n)]
    print("Сгенерированная последовательность: ", sequence)
    return sequence

def random_number_generator():
    """
    A generator function that yields a random number between -100 and 100.

    Yields:
        int: A random number between -1000 and 1000.
    """
    while True:
        yield random.randint(-1000, 1000)

def init_sequence_with_user_input():
    """
    Initializes a sequence by taking user input.

    The function prompts the user to enter numbers until the user enters 'stop'.
    Each valid input is converted to a int and added to the sequence list.
    If the user enters an invalid input, an error message is displayed.

    Returns:
        sequence (list): A list of int representing the user input sequence.
    """
    sequence = []
    while True:
        num = input("Введите число (или 'stop' для остановки): ")
        if num.lower() == 'stop' or int(num) > 100:
            break
        else:
            try:
                sequence.append(int(num))
            except ValueError:
                print("Некорректный ввод. Пожалуйста, введите число.")
    return sequence

def generate_binary_string(length):
    """
    Generate a binary string of a given length.

    Args:
        length (int): The length of the string to be generated.

    Returns:
        str: A binary string of the given length.
    """
    return ''.join(random.choice('01') for _ in range(length))

def generate_random_text(length=100):
    """
    Generates a random text of the specified length, with spaces inserted at random intervals.

    Args:
        length (int): The length of the text to generate.

    Returns:
        str: The generated text.
    """
    text = ''.join(random.choice(string.ascii_letters) for _ in range(length))
    text_with_spaces = ''
    while text:
        space_index = random.randint(0, 10)
        text_with_spaces += text[:space_index] + ' '
        text = text[space_index:]
    generated_text = text_with_spaces.strip()
    print(f"Сгенерированный текст: {generated_text}")
    return generated_text

def input_list():
    while True:
        try:
            return list(map(float, input("Введите элементы списка, разделенные пробелами: ").split()))
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите вещественные числа.")

def initialize_list(n, min_value=-100, max_value=100):
    return [random.uniform(min_value, max_value) for _ in range(n)]

def print_list(lst):
    print("Список: ", lst)

def process_list(lst):
    """
    Process a list and calculates the product of every other element in the list.
    It also calculates the sum of the elements between the first and last occurrence of zero (if any).

    Args:
        lst (list): The input list.

    Returns:
        tuple: A tuple containing the product of every other element in the list and the sum of elements between the first and last occurrence of zero (if any).
    """
    product = 1
    for i in range(0, len(lst), 2):
        product *= lst[i]

    first_zero = lst.index(0) if 0 in lst else -1
    last_zero = len(lst) - 1 - lst[::-1].index(0) if 0 in lst else -1

    if first_zero != -1 and last_zero != -1 and first_zero != last_zero:
        sum_between_zeros = sum(lst[first_zero+1:last_zero])
    else:
        sum_between_zeros = None

    return product, sum_between_zeros