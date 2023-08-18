
class Water:
    def __add__(self, other):
        if isinstance(other, Air):
            print('Water + Air = Storm')
        elif isinstance(other, Fire):
            print('Water + Fire = Steam')
        elif isinstance(other, Ground):
            print('Water + Ground = Dirt')

class Air:
    def __add__(self, other):
        if isinstance(other, Fire):
            print('Air + Fire = Lightning')
        elif isinstance(other, Ground):
            print('Air + Ground = Dust')
        elif isinstance(other, Water):
            print('Air + Water = Storm')

class Fire:
    def __add__(self, other):
        if isinstance(other, Water):
            print('Fire + Water = Steam')
        elif isinstance(other, Air):
            print('Fire + Air = Lightning')
        elif isinstance(other, Ground):
            print('Fire + Ground = Lava')

class Ground:

    def __add__(self, other):
        if isinstance(other, Water):
            print('Ground + Water = Dirt')
        elif isinstance(other, Air):
            print('Ground + Air = Dust')
        elif isinstance(other, Fire):
            print('Ground + Fire = Lava')

w = Water()
a = Air()
f = Fire()
g = Ground()
print()
print('WATER')
w.__add__(a)
w.__add__(f)
w.__add__(g)
print()
print('AIR')
a.__add__(w)
a.__add__(f)
a.__add__(g)
print()
print('FIRE')
f.__add__(w)
f.__add__(a)
f.__add__(g)
print()
print('GROUND')
g.__add__(w)
g.__add__(a)
g.__add__(f)

