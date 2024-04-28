from misc import repeat_function
from task1 import task_1
from task2 import task_2
from task3 import task_3
from task4 import task_4
from task5 import task_5

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
        if choice == "1":
            repeat_function(lambda: task_1())
        elif choice == "2":
            repeat_function(lambda: task_2())
        elif choice == "3":
            repeat_function(lambda: task_3())
        elif choice == "4":
            repeat_function(lambda: task_4())
        elif choice == "5":
            repeat_function(lambda: task_5())
        elif choice == "6":
            break
        else:
            print("Неверный ввод. Попробуйте снова.")
        
        

if __name__ == "__main__":
    main()