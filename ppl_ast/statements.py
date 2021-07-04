# PPL Statements
from node import *


class LocalStatement(AbstractStatement):
    def __init__(self, name: str, value: AbstractExpression):
        self.name = name
        self.value = value

    def print(self, pretty: bool, indents: str = ""):
        return indents + "local " + self.name + (" := " if pretty else ":=") + self.value.print(pretty) + \
               (";\n" if pretty else ";")


class IfStatement:
    pass


class CaseStatement:
    pass


class IfErrStatement:
    pass


class WhileStatement:
    pass


class BreakStatement:
    pass


class ContinueStatement:
    pass


class AssignmentStatement:
    pass


class ReturnStatement:
    pass


class KillStatement:
    pass


class FunctionCallStatement:
    pass
