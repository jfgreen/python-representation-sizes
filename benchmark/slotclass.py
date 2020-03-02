#!/usr/bin/env python3

import sys

count = int(sys.argv[1])

class SlotClassFruit(object):
    __slots__ = ('name', 'price', 'colour')
    def __init__(self, name, price, colour):
        self.name = name
        self.price = price
        self.colour = colour


def fruit_as_slot_class():
    return SlotClassFruit('mango', 123, 'red')

basket = [fruit_as_slot_class() for _ in range(count)]

total_price = sum((f.price for f in basket))

print(total_price)
