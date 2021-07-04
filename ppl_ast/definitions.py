# PPL definitions
from node import *


class FunctionDefinition(AbstractDefinition):
    def __init__(self, exported: bool, name: str, args: list[str], body: list[AbstractStatement]):
        self.exported = exported
        self.name = name
        self.args = args
        self.body = body

    def print(self, pretty: bool, indents: str = ""):
        if pretty:
            return \
                indents + ("export " if self.exported else "") + self.name + "(" + ", ".join(self.args) + ")\n" + \
                indents + "begin\n" + \
                "\n".join(map(lambda df: indents + df.print(pretty, indents + "\t"), self.body)) + \
                indents + "end;\n"
        else:
            return \
                ("export " if self.exported else "") + self.name + "(" + ",".join(self.args) + ")begin " + \
                "".join(map(lambda df: df.print(False), self.body)) + "end;"


class FunctionForwardDefinition:
    pass


class VariableDefinition:
    pass
