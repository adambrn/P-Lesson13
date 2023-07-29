#Создайте функцию, которая запрашивает числовые данные от пользователя до тех пор, пока он не введёт целое или вещественное число.
#Обрабатывайте не числовые данные как исключения.

def get_numeric_input():
    while True:
        user_input = input("Введите число: ")
        try:
            return int(user_input) if user_input.isdigit() else float(user_input)
        except ValueError:
            print("Ошибка! Введите целое или вещественное число.")

if __name__ == "__main__":
    print("Введенное число:", get_numeric_input())
