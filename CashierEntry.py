import ENUM
from PaymentMethod import PaymentMethod

class CashierEntry:
    def __init__(self, paymentMethod: ENUM.VALID_PAYMENT_METHODS, ITEM_ID: ENUM.ITEMS_IDS, itemQuantity: int):
        self.__paymentMethod = PaymentMethod(paymentMethod)
        self.__ITEM_ID = ITEM_ID
        self.__totalValue = ITEM_ID.value * itemQuantity

    def getITEM_ID(self):
        return self.__ITEM_ID