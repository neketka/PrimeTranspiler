# PPL Expressions
from node import *


class NumberExpression(AbstractExpression):
    def __init__(self, value: float):
        self.value = value

    def print(self, pretty: bool, indents: str = ""):
        return str(self.value)
