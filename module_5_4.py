# Домашняя работа по уроку "Различие атрибутов класса и экземпляра."
# Цель: понять разницу между атрибутами объекта и класса, дополнив уже существующий класс. Применить метод __new__.
# Задача "История строительства":
# Для решения этой задачи будем пользоваться решением к предыдущей задаче "Перегрузка операторов".
# В классе House создайте атрибут houses_history = [], который будет хранить названия созданных объектов.
# Правильней вписывать здание в историю сразу при создании объекта, тем более можно удобно обращаться к атрибутам класса
# используя ссылку на сам класс - cls.
# Дополните метод __new__ так, чтобы:
# Название объекта добавлялось в список cls.houses_history.
# Название строения можно взять из args по индексу.
# Также переопределите метод __del__(self) в котором будет выводиться строка:
# "<название> снесён, но он останется в истории"
# Создайте несколько объектов класса House и проверьте работу методов __del__ и __new__,
# а также значение атрибута houses_history.


class House:
    houses_history = []

    def __new__(cls, *args):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        int(new_floor)
        if new_floor > self.number_of_floors or new_floor <= 0:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, other):
        if not isinstance(other, int) or isinstance(other, House):
            print("Неправильный ввод данных")
        else:
            return self.number_of_floors + other

    def __radd__(self, other):
        if not isinstance(other, int) or isinstance(other, House):
            return self.number_of_floors + other

    def __iadd__(self, other):
        if not isinstance(other, int) or isinstance(other, House):
            return self.number_of_floors + other

    def __del__(self):
        print((f'{self.name} снесён, но он останется в истории'))


h1 = House('ЖК Эльбрус', 20)
print(House.houses_history)
h2 = House('ЖК Горский', 30)
print(House.houses_history)
h3 = House('ЖК Домик в деревне', 5)
print(House.houses_history)

del h3
del h2

print(House.houses_history)
del h1
print(House.houses_history)