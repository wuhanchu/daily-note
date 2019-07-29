# -*- coding: utf-8 -*-
from enum import Enum, unique

class Gender(Enum):
    Male = 0
    Female = 1

print(Gender.Male.name)
print(Gender.Male.code)