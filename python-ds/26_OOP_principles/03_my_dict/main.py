# TODO здесь писать код

class MyDict(dict):

    def __init__(self):
        super().__init__()

    def get(self, index):
        if index in self:
            return self[index]
        else:
            return 0

md = MyDict()
md['asd'] = 12
print(md)
print(md.get('asd'))
print(md.get('qw'))
