#!/usr/bin/env python3

import sys

count = int(sys.argv[1])

class ClassFruit(object):
    def __init__(self, name, price, colour):
        self.name = name
        self.price = price
        self.colour = colour


def fruit_as_class():
    return ClassFruit('mango', 123, 'red')

basket = [fruit_as_class() for _ in range(count)]

total_price = sum((f.price for f in basket))

print(total_price)
