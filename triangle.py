import math


class Triangle:
    def __init__(self, A, B, C):
        # Функция вычисляет длину стороны согласно координатам точек
        def sideLen(dot1, dot2):
            return math.sqrt((dot1[0] - dot2[0]) ** 2
                             + (dot1[1] - dot2[1]) ** 2)

        self.A = A
        self.B = B
        self.C = C
        # На основании соседних координат вычисляем длину стороны AB
        self.AB = sideLen(self.A, self.B)
        self.BC = sideLen(self.B, self.C)
        self.CA = sideLen(self.C, self.A)

    # Вычисление площади треугольника по формуле Герона
    def areaTriangle(self):
        semi_perimeter = self.perimeterTriangle() / 2

        return math.sqrt(semi_perimeter
                         * (semi_perimeter - self.AB)
                         * (semi_perimeter - self.BC)
                         * (semi_perimeter - self.CA))

    # вычисляем периметр треугольника
    def perimeterTriangle(self):
        return self.AB + self.BC + self.CA

    # Вычисляем высоту треугольника
    def heightTriangle(self):
        return self.areaTriangle() / (self.AB / 2)

    def truefalseTriangle(self):
        assert self.AB + self.BC > self.CA or self.BC + self.CA > self.AB or self.AB + self.CA > self.BC, 'Треугольник не существует! '


treugolnik1 = Triangle((1, 2), (3, 4), (5, 8))

print(treugolnik1.areaTriangle())
print(treugolnik1.heightTriangle())
print(treugolnik1.perimeterTriangle())
print((treugolnik1.truefalseTriangle()))