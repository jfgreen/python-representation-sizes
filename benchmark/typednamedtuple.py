#!/usr/bin/env python3

import sys
import typing

count = int(sys.argv[1])

class TypedTupleFruit(typing.NamedTuple):
    name: str
    price: int
    colour: str


def fruit_as_typed_namedtuple():
    return TypedTupleFruit('mango', 123, 'red')

basket = [fruit_as_typed_namedtuple() for _ in range(count)]

total_price = sum((f.price for f in basket))

print(total_price)
