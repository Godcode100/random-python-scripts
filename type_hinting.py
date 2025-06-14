import random
import typing

def roll_dice(sides: int=6,dice:int=1) ->typing.Tuple[int,...]:
    return(random.randint(1,sides) for _ in range(dice))

result = roll_dice(dice = 7)
print(result)

help(typing.Optional)
print(roll_dice.__annotations__)
