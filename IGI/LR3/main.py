from task1 import arsin_series
from task2 import count_negative_numbers
from task3 import print_str
from task4 import analyze_text
from task5 import task5
from misc import repeat_function, generate_binary_string
'''
Lab 3
Lab title: Standart data types, functions, modules in Python
Version: 1.0
Author: Alkhovik Danila
Date: 2024-03-30
'''

def main():
    while True:
        print("\nВыберите задание для выполнения:")
        print("1. Задание 1")
        print("2. Задание 2")
        print("3. Задание 3")
        print("4. Задание 4")
        print("5. Задание 5")
        print("6. Выход")
        
        choice = input("Ваш выбор: ")
        
        if choice == '1':
            repeat_function(lambda: arsin_series())
        elif choice == '2':
            repeat_function(lambda: count_negative_numbers())
        elif choice == '3':
            print("1. Введите строку")
            print("2. Сгенерировать случайную строку")
            sub_choice = input("Ваш выбор: ")
            if sub_choice == '1':
                s = input("Введите строку: ")
                repeat_function(lambda: print_str(s))
            elif sub_choice == '2':
                length = int(input("Введите длину строки: "))
                s = generate_binary_string(length)
                repeat_function(lambda: print_str(s))
            else:
                print("Некорректный ввод. Пожалуйста, введите число 1 или 2.")
        elif choice == '4':
            print("1. Введите текст")
            print("2. Использовать константный текст")
            print("3. Сгенерировать случайный текст")
            sub_choice = input("Ваш выбор: ")
            if sub_choice == '1':
                text = input("Введите текст: ")
                repeat_function(lambda: analyze_text(text))
            elif sub_choice == '2':
                text = "«so she was considering in her own mind, as well as she could, for the hot day made her feel very sleepy and stupid, whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her.» "
                repeat_function(lambda: analyze_text(text))
            elif sub_choice == '3':
                length = int(input("Введите длину текста: "))
                text = generate_binary_string(length)
                repeat_function(lambda: analyze_text(text))
            else:
                print("Некорректный ввод. Пожалуйста, введите число от 1 до 3.")
        elif choice == '5':
            repeat_function(lambda: task5())
        elif choice == '6':
            break
        else:
            print("Некорректный ввод. Пожалуйста, введите число от 1 до 6.")

if __name__ == "__main__":
    main()