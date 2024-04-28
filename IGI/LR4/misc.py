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

def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")

def input_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a float.")