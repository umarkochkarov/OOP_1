#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Cursor:
    def __init__(self, x, y, direction, size):
        if not isinstance(x, int) or not isinstance(y, int) or not isinstance(direction, str) or not isinstance(size,
                                                                                                                int):
            raise ValueError("Некорректные значения аргументов")
        if x < 0 or y < 0 or size < 1 or size > 15:
            raise ValueError("Некорректные значения аргументов")
        if direction != "horizontal" and direction != "vertical":
            raise ValueError("Некорректное значение аргумента")
        self.x = x
        self.y = y
        self.direction = direction
        self.size = size
        self.is_visible = True

    def move(self, dx, dy):
        if not isinstance(dx, int) or not isinstance(dy, int):
            raise ValueError("Некорректные значения аргументов")
        self.x += dx
        self.y += dy

    def change_direction(self, new_direction):
        if not isinstance(new_direction, str):
            raise ValueError("Некорректное значение аргумента")
        if new_direction != "horizontal" and new_direction != "vertical":
            raise ValueError("Некорректное значение аргумента")
        self.direction = new_direction

    def change_size(self, new_size):
        if not isinstance(new_size, int):
            raise ValueError("Некорректное значение аргумента")
        if new_size < 1 or new_size > 15:
            raise ValueError("Некорректное значение аргумента")
        self.size = new_size

    def hide(self):
        self.is_visible = False

    def show(self):
        self.is_visible = True

    def display(self):
        print("x:", self.x)
        print("y:", self.y)
        print("direction:", self.direction)
        print("size:", self.size)
        print("is_visible:", self.is_visible)


def make_Cursor(x, y, direction, size):
    return Cursor(x, y, direction, size)


if __name__ == "__main__":
    c = make_Cursor(10, 5, "horizontal", 5)
    c.display()

    c.move(2, 3)
    c.display()

    c.change_direction("vertical")
    c.display()

    c.change_size(10)
    c.display()

    c.hide()
    c.display()

    c.show()
    c.display()