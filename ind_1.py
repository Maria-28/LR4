#!/usr/bin/env python3
# -*- кодировка: utf-8 -*-
# Дано предложение. Вывести «столбиком» все его буквы и, стоящие на четных местах.

if __name__ == '__main__':
    print(*(letter for i, letter in enumerate(input()) if letter == "и" and not i % 2), sep="\n")


