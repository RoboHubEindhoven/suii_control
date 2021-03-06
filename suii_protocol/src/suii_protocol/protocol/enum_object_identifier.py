#! /usr/bin/env python
from enum import Enum

class ObjectIdentifierType(Enum):
   F20_20_B=1, 'Small Black Alu. Profile'
   F20_20_G=2, 'Small Grey Alu. Profile'
   S40_40_B=3, 'Large Black Alu. Profile'
   S40_40_G=4, 'Large Grey Alu. Profile'
   M20_100=5, 'Bolt'
   M20=6, 'Small Nut'
   M30=7, 'Large Nut'
   R20=8, 'Plastic Tube'
   BEARING_BOX=9, 'Bearing Box'
   BEARING=10, 'Bearing'
   AXIS=11, 'Axis'
   DISTANCE_TUBE=12, 'Distance Tube'
   MOTOR=13, 'Motor'
   CONTAINER_B=14, 'Blue Container'
   CONTAINER_R=15, 'Red Container'

   def __new__(cls, value, name):
        member = object.__new__(cls)
        member._value_ = value
        member.fullname = name
        return member

   def __int__(self):
        return self.value