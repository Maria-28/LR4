#!/usr/bin/env python3
# -*- кодировка: utf-8 -*-
# Даны три слова. Напечатать только те буквы слов, которые есть лишь в одном из слов.
# Рассмотреть два варианта:
# повторяющиеся буквы каждого слова рассматриваются;
# повторяющиеся буквы каждого слова не рассматриваются.

import itertools

if __name__ == '__main__':
    a = 'привет'
    b = 'это'
    c = 'слова'

    al = list(a)
    bl = list(b)
    cl = list(c)

    for (i, l, x) in zip(al, bl, cl):
        if i != l and x != i and x != l:
            print(i, l, x)