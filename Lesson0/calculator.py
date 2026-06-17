class Calculator:
    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            raise ArithmeticError("Impossible to divide by zero :)" )
        return a / b

    def pow(self, a, b=2):
        return pow(a, b)

    def avg(self, numbers):
        if len(numbers) == 0:
            return 0
        return self.div(sum(numbers), len(numbers))