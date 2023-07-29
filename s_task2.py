""" Создайте функцию аналог get для словаря.
Помимо самого словаря функция принимает ключ и значение по умолчанию.
При обращении к несуществующему ключу функция должна возвращать дефолтное значение.
Реализуйте работу через обработку исключений. """

def get_from_dict(dictionary, key, default_value=None):
    try:
        return dictionary[key]
    except KeyError:
        return default_value

if __name__ == "__main__":
    my_dict = {"apple": 1, "banana": 2, "orange": 3}
    print(get_from_dict(my_dict, "banana", "Not Found"))
    print(get_from_dict(my_dict, "grape", "Not Found"))
