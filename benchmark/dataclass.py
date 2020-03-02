#!/usr/bin/env python3

import sys
from dataclasses import dataclass

count = int(sys.argv[1])

@dataclass
class DataClassFruit:
    name: str
    price: int
    colour: str

def fruit_as_dataclass():
    return DataClassFruit('mango', 123, 'red')

basket = [fruit_as_dataclass() for _ in range(count)]

total_price = sum((f.price for f in basket))

print(total_price)
