class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"

class B:
    def __init__(self):
        super().__init__()
        self.bar = "bar"

class C(A, B):
    def __init__(self):
        super().__init__()

    def showprops(self):
        print(self.foo)
        print(self.bar)

c = C()