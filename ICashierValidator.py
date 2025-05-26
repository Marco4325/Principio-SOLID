from abc import ABC, abstractmethod
from CashierEntry import CashierEntry
import ENUM

class ICashierValidator(ABC):

    @abstractmethod
    def validateEntry(self, entry: CashierEntry) -> ENUM.VALIDATION:
        pass