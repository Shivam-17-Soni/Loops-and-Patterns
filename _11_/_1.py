class C2dvec:
    def __init__(self, i, j):
        self.icap=i
        self.jcap=j

    def stm(self):
        return f"{self.icap}i + {self.jcap}j"

class C3dvec(C2dvec):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.kcap=k

    def stm(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"

v2d=C2dvec(1,5)
v3d=C3dvec(1,56,5)
print(v2d.stm())
print(v3d.stm())
