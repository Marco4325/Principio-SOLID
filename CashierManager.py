import ENUM
from ICashierValidator import ICashierValidator
from CashierEntry import CashierEntry

class CashierManager:

    def __init__(self, validator: ICashierValidator):
        self.__ENTRIES = []
        self.__CashierValidator = validator

    def addEntry(self, paymentMethod: ENUM.VALID_PAYMENT_METHODS, ITEM_ID: ENUM.ITEMS_IDS, itemQuantity: int):
        newEntry = CashierEntry(paymentMethod, ITEM_ID, itemQuantity)
        validation = self.__CashierValidator.validateEntry(newEntry)
        if validation.value:
            self.__ENTRIES.append(newEntry)

    def printEntries(self):
        for entry in self.__ENTRIES:
            print(entry.getITEM_ID())