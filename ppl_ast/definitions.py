# PPL definitions


class FunctionDefinition:
    def __init__(self, exported: bool, name: str):
        self.exported = exported
        self.name = name

    def print(self, pretty: bool, tabs: int = 0):
        return


class FunctionForwardDefinition:
    pass


class VariableDefinition:
    pass
