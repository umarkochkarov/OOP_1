class Pair:
    def __init__(self, first, second):
        if not isinstance(first, int) or not isinstance(second, float):
            raise ValueError("Некорректные значения аргументов")
        self.first = first
        self.second = second

    def multiply(self, number):
        if not isinstance(number, float):
            raise ValueError("Некорректное значение аргумента")
        self.first *= number
        self.second *= number

    def display(self):
        print("first:", self.first)
        print("second:", self.second)


def make_Pair(first, second):
    return Pair(first, second)


if __name__ == "__main__":
    p = make_Pair(3, 0.5)
    p.display()

    p.multiply(2.5)
    p.display()