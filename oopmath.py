import math

class Math:
    def __init__(self, num):
        self.num = num

    def add(self, num):
        return self.num + num

    def subtract(self, num):
        return self.num - num

    def multiply(self, num):
        return self.num * num

    def divide(self, num):
        return self.num / num

    def power(self, num):
        return self.num ** num

    def square(self):
        return self.num ** 2

    def cube(self):
        return self.num ** 3

    def square_root(self):
        return self.num ** 0.5

    def cube_root(self):
        return self.num ** (1/3)

    def absolute(self):
        return abs(self.num)

    def factorial(self):
        return math.factorial(self.num)

    def log(self, base=10):
        return math.log(self.num, base)

    def sin(self):
        return math.sin(self.num)

    def cos(self):
        return math.cos(self.num)

    def tan(self):
        return math.tan(self.num)

def main():
    math = Math(10)
    print(math.add(10))
    print(math.subtract(10))
    print(math.multiply(10))
    print(math.divide(10))
    print(math.power(10))
    print(math.square())
    print(math.cube())
    print(math.square_root())
    print(math.cube_root())
    print(math.absolute())
    print(math.factorial())
    print(math.log())
    print(math.sin())
    print(math.cos())
    print(math.tan())

 
if __name__ == "__main__":
    main()