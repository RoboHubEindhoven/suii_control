#! /usr/bin/env python
from enum import Enum

class LocationIdentifierType(Enum):
   SH=1, 'Shelf'
   WS=2, 'Workstation'
   CB=3, 'Conveyor Belt'
   WP=4, 'Way Point'
   PP=5, 'Precision Platform'
   ROBOT=6, 'Robot'
   EX=100, 'Exit'
   RT = 404, 'Rotating Table'      

   def __new__(cls, value, name):
        member = object.__new__(cls)
        member._value_ = value
        member.fullname = name
        return member

   def __int__(self):
        return self.value