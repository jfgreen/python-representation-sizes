#!/usr/bin/env python3

from sys import getsizeof
from pympler.asizeof import asizeof
from collections.abc import Mapping

# Dictionary

fruit_as_dict = dict(name='mango', price=123, colour='red')

# Named Tuple

import collections

TupleFruit = collections.namedtuple('TupleFruit', ['name', 'price', 'colour'])

fruit_as_named_tuple = TupleFruit('mango', 123, 'red')

# Typed Named Tuple

import typing

class TypedTupleFruit(typing.NamedTuple):
    name: str
    price: int
    colour: str

fruit_as_named_typed_tuple = TypedTupleFruit('mango', 123, 'red')

# Data Class

from dataclasses import dataclass

@dataclass
class DataClassFruit:
    name: str
    price: int
    colour: str

fruit_as_dataclass = DataClassFruit('mango', 123, 'red')

# Slot Data Class

from dataclasses import dataclass

@dataclass
class SlotDataClassFruit:
    __slots__ = ('name', 'price', 'colour')
    name: str
    price: int
    colour: str

fruit_as_slot_dataclass = SlotDataClassFruit('mango', 123, 'red')

# Class

class ClassFruit(object):
    def __init__(self, name, price, colour):
        self.name = name
        self.price = price
        self.colour = colour

fruit_as_class = ClassFruit('mango', 123, 'red')

# Slot Class

class SlotClassFruit(object):
    __slots__ = ('name', 'price', 'colour')
    def __init__(self, name, price, colour):
        self.name = name
        self.price = price
        self.colour = colour

fruit_as_slot_class = SlotClassFruit('mango', 123, 'red')


# Basic size calculator
# (n.b this is unlikely to work outside the examples presented here)
def get_size(root_obj):
    size = 0
    to_explore = [root_obj]
    while len(to_explore) > 0:
        obj = to_explore.pop()
        size += getsizeof(obj)
        if isinstance(obj, tuple):
            to_explore.extend(obj)
        if isinstance(obj, Mapping):
            to_explore.extend(obj.keys())
            to_explore.extend(obj.values())
        if hasattr(obj, '__dict__'):
            to_explore.append(vars(obj))
        if hasattr(obj, '__slots__'):
            to_explore.extend([getattr(obj, s) for s in obj.__slots__])
    return size



def compare_sizes(method):
    mango_size = method('mango')
    number_size = method(123)
    red_size = method('red')
    total_primitive_size = mango_size + number_size + red_size
    print('\nPrimitive sizes:')
    print(f'mango: {mango_size}')
    print(f'123: {number_size}')
    print(f'red: {red_size}')
    print(f'total:: {total_primitive_size}')

    dataclass_size = method(fruit_as_dataclass)
    slot_dataclass_size = method(fruit_as_slot_dataclass)
    class_size = method(fruit_as_class)
    slot_class_size = method(fruit_as_slot_class)
    named_tuple_size = method(fruit_as_named_tuple)
    named_typed_tuple_size = method(fruit_as_named_typed_tuple)
    dict_size = method(fruit_as_dict)

    dataclass_overhead  = dataclass_size - total_primitive_size
    slot_dataclass_overhead = slot_dataclass_size - total_primitive_size
    class_overhead  = class_size - total_primitive_size
    slot_class_overhead  = slot_class_size - total_primitive_size
    named_tuple_overhead  = named_tuple_size - total_primitive_size
    named_typed_tuple_overhead  = named_typed_tuple_size - total_primitive_size
    dict_overhead  = dict_size - total_primitive_size

    print('\nCompound sizes:')
    print(f'Data class: {dataclass_size} (overhead: {dataclass_overhead})')
    print(f'Data class (slots): {slot_dataclass_size} (overhead: {slot_dataclass_overhead})')
    print(f'Class: {class_size} (overhead: {class_overhead})')
    print(f'Class (slots): {slot_class_size} (overhead: {slot_class_overhead})')
    print(f'Named tuple: {named_tuple_size} (overhead: {named_tuple_overhead})')
    print(f'Named typed tuple: {named_typed_tuple_size} (overhead: {named_typed_tuple_overhead})')
    print(f'Dict: {dict_size} (overhead: {dict_overhead})')

print("\n---- Using get_size ----")
compare_sizes(get_size)

print("\n---- Using asizeof ----")
compare_sizes(asizeof)

