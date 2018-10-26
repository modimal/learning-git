#! usr/bin/env python3
# coding: utf-8


class Calculator:
    """Calculator"""

    @staticmethod
    def add(x, y):
        try:
            return float(x) + float(y)
        except ValueError as err:
            print("\nERROR: {}\n".format(err))
