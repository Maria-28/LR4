#!/usr/bin/env python3
# -*- кодировка: utf-8 -*-
# Дано предложение. Напечатать все символы, расположенные между первой и второй
# запятыми. Если второй запятой нет, то должны быть напечатаны все символы,
# расположенные после единственной имеющейся запятой.

if __name__ == '__main__':
    a = "s, abbvbvb, b"
    def printbetween(s):
        m = s.split(',')
        print(m[1])
    printbetween(a)