# TODO здесь писать код

class Water:
    def __init__(self, name='Water'):
        self.name = name
    def __add__(self, other):
        self.other = other
        return Answer()
class Air:
    def __init__(self, name='Air'):
        self.name = name
    def __add__(self, other):
        self.other = other
        return Answer()

class Fire:
    def __init__(self, name='Fire'):
        self.name = name
    def __add__(self, other):
        self.other = other
        return Answer()
class Earth:
    def __init__(self, name='Earth'):
        self.name = name
    def __add__(self, other):
        self.other = other
        return Answer()

class Answer:
    storm = 'Storm'
    steam = 'Steam'
    dirt = 'Dirt'
    lightning = "Lightning"
    dust = 'Dust'
    lava = 'Lava'


w = Water()
a = Air()
f = Fire()
e = Earth()

wa = w+a
aw = a+w
wf = w+f
fw = f+w
we = w+e
ew = e+w
af = a+f
fa = f+a
ae = a+e
ea = e+a
fe = f+e
ef = e+f

print('{} + {} = {}'.format(w.name, a.name, wa.storm))
print('{} + {} = {}'.format(a.name, w.name, aw.storm))
print('{} + {} = {}'.format(w.name, f.name, wf.steam))
print('{} + {} = {}'.format(f.name, w.name, fw.steam))
print('{} + {} = {}'.format(w.name, e.name, we.dirt))
print('{} + {} = {}'.format(e.name, w.name, ew.dirt))
print('{} + {} = {}'.format(a.name, f.name, af.lightning))
print('{} + {} = {}'.format(f.name, a.name, fa.lightning))
print('{} + {} = {}'.format(a.name, e.name, ae.dust))
print('{} + {} = {}'.format(e.name, a.name, ea.dust))
print('{} + {} = {}'.format(f.name, e.name, fe.lava))
print('{} + {} = {}'.format(e.name, f.name, ef.lava))
