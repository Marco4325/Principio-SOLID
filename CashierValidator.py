import ENUM
import CashierEntry
from ICashierValidator import ICashierValidator

class CashierValidator(ICashierValidator):
    __OUT_OF_STOCK = [ENUM.ITEMS_IDS.COCA_LATA]
    
    def validateEntry(self, entry: CashierEntry) -> ENUM.VALIDATION:
        for ITEM_ID in self.__OUT_OF_STOCK:
            if ITEM_ID == entry.getITEM_ID():
                return ENUM.VALIDATION.NON_VALIDATED
        return ENUM.VALIDATION.VALIDATED