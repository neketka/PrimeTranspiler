from ppl_ast.definitions import *
from ppl_ast.expressions import *
from ppl_ast.statements import *


def main():
    prog = PrimeProgram([
        FunctionDefinition(True, "MyExportedFunction", ["my_arg", "arg2"], [
            LocalStatement("my_num", NumberExpression(0.5))
        ])
    ])
    print(prog.print(pretty=True))
    print(prog.print(pretty=False))


if __name__ == "__main__":
    main()

