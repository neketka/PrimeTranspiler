from abc import ABC, abstractmethod


class AbstractNode(ABC):
    @abstractmethod
    def print(self, pretty: bool, indents: str = ""): pass


class AbstractStatement(AbstractNode, ABC):
    pass


class AbstractDefinition(AbstractNode, ABC):
    pass


class AbstractExpression(AbstractNode, ABC):
    pass


class PrimeProgram:
    def __init__(self, definitions: list[AbstractDefinition]):
        self.definitions = definitions

    def print(self, pretty):
        return ("\n" if pretty else "").join(map(lambda df: df.print(pretty), self.definitions))
