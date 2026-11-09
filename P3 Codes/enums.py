from enum import Enum 

class Day(Enum):
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday =4
    Friday = 5
    Saturday = 6
    Sunday = 7

today = Day.Wednesday

print(today.value)