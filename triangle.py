class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.ab_length = (pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2)) ** 0.5
        self.ac_length = (pow(a[0] - c[0], 2) + pow(a[1] - c[1], 2)) ** 0.5
        self.bc_length = (pow(b[0] - c[0], 2) + pow(b[1] - c[1], 2)) ** 0.5

    def is_exist(self):
        f = sorted([self.ab_length, self.ac_length, self.bc_length])
        if f[2] < sum([f[0], f[1]]):
            return True
        else:
            return False

    def get_perimeter(self):
        return sum([self.ab_length, self.ac_length, self.bc_length])

    def get_area(self):
        # p = half_perimeter
        p = self.get_perimeter() * 0.5
        return (p * (p - self.ab_length) * (p - self.bc_length) * (p - self.ac_length)) ** 0.5
