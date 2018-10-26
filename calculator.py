#! usr/bin/env python3
# coding: utf-8


class Calculator:
    """Calculator"""

    @staticmethod
    def addition(x, y):
        try:
            return float(x) + float(y)
        except ValueError as err:
            print("\nERROR: {}\n".format(err))
            return False

    @staticmethod
    def division(x, y):
        try:
            return float(x) / float(y)
        except ValueError as err:
            print("\nERROR: {}\n".format(err))
            return False
        except ZeroDivisionError as err:
            print("\nERROR: {}\n".format(err))
            return False

    @staticmethod
    def subtraction(x, y):
        try:
            return float(x) - float(y)
        except ValueError as err:
            print("\nERROR: {}\n".format(err))
            return False

