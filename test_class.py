a = 100
b = 5


class Calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def multi(self):
        c = self.a * self.b
        print(c)


if __name__ == "__main__":
    calcu = Calc(a, b)
    calcu.multi()
