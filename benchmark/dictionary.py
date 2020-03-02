#!/usr/bin/env python3

import sys

count = int(sys.argv[1])

def fruit_as_dict():
    return dict(name='mango', price=123, colour='red')

basket = [fruit_as_dict() for _ in range(count)]

total_price = sum((f['price'] for f in basket))

print(total_price)
