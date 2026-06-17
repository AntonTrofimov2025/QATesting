class SimpleMath:
    """Simple mathematical operations class."""
    def square(self, x: int | float):
        """
        Calculate the square of a number.

        :param x: The number to be squared.
        :return: Returns the square of the number.
        """
        return pow(x, 2)

    def cube(self, x: int | float):
        """
        Calculate the cube of a number.

        :param x: The number to be cubed.
        :return: Returns the cube of the number.
        """
        return pow(x, 3)

    def mul(self, a: int | float, b: int | float):
        """
        Multiplies the values of an a and b.

        :param a: First value.
        :param b: Second value.
        :return: Returns result after multiplying.
        """
        return a * b

    def div(self, a, b):
        """
        Divides the value of an a by b.

        :param a: First value.
        :param b: Second value.
        :return: Returns result after division.
        """
        if b == 0:
            raise ArithmeticError("Division by zero is impossible!!")
        return a / b