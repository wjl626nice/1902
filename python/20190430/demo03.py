# __iter__
class Foo(object):

    def __init__(self, sq):
        self.sq = sq
        self.name = "zs"
        self.age = 18

    def __iter__(self):
        return iter(self.sq)


obj = Foo([11, 22, 33, 44])

for i in obj:
    print(i)
