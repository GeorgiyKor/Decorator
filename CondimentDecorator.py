from abc import ABC, abstractmethod
from Beverage import Beverage

class CondimentDecorator(Beverage, ABC)
    @abstractmethod
    def getDescription(self) -> str:
        return self._description