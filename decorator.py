import functools
character = "SirBob"
health = 15
xp = 0
import random

def caharcter_action(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        global health
        if health <= 0:
            print(f"{character} is too weak")
            return
        result = func(*args,**kwargs)
        print(f' Health{health} | XP:{xp}')
        return result
    return wrapper
@caharcter_action
def eat_food(food):
    global health
    print(f'{character} ate {food}')
    health +=1

def fight_monster(monster,strength):
    global health,xp
    if random.randint(1,20) >=strength
    print(f'{character} wins fight')
    health +=5
    xp -= 7
    
