#!/usr/bin/env python3

import sys
import collections

count = int(sys.argv[1])

TupleFruit = collections.namedtuple('TupleFruit', ['name', 'price', 'colour'])

def fruit_as_namedtuple():
    return TupleFruit('mango', 123, 'red')

basket = [fruit_as_namedtuple() for _ in range(count)]

total_price = sum((f.price for f in basket))

print(total_price)
