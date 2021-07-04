from abc import ABC, abstractmethod


class AbstractNode(ABC):
    @abstractmethod
    def print(self, pretty: bool, tabs: int = 0): pass


class AbstractStatement(ABC, AbstractNode):
    pass


class AbstractDefinition(ABC, AbstractNode):
    pass


class AbstractExpression(ABC, AbstractNode):
    pass


class Program:
    def __init__(self, definitions: list[AbstractDefinition]):
        self.definitions = definitions

    def print(self, pretty):
        pass
