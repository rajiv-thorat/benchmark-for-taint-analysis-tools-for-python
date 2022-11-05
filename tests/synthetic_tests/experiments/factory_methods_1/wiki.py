from abc import ABC, abstractmethod


class CommandExecution(ABC):
    def __init__(self) -> None:
        print('In command execution')

    def evaluate_command(self) -> None:
        print(self.get_class_name())
        eval(self.command) 

    @abstractmethod
    def get_class_name(self):
        raise NotImplementedError("You should implement this!")


class ClassA(CommandExecution):
    def get_class_name(self, command) -> "ClassA1":
        return ClassA1(command)


class ClassB(CommandExecution):
    def get_class_name(self, command) -> "ClassB1":
        return ClassB1(command)


class AbstractClass(ABC):
    def __init__(self) -> None:
       print('In abstract class') 


class ClassA1(AbstractClass):
    def __str__(self) -> str:
        return "Magic room"


class ClassB1(AbstractClass):
    def __str__(self) -> str:
        return "Ordinary room"


instanceB = ClassB('command')
instanceB.evaluate_command()

instanceA = ClassA('command')
instanceA.evaluate_command()