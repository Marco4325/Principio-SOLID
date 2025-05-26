import ENUM
from CashierManager import CashierManager
from CashierValidator import CashierValidator

CaixaMercado1 = CashierManager(CashierValidator())

CaixaMercado1.addEntry(ENUM.VALID_PAYMENT_METHODS.PIX, ENUM.ITEMS_IDS.COCA_LATA, 2)
CaixaMercado1.addEntry(ENUM.VALID_PAYMENT_METHODS.CREDITO, ENUM.ITEMS_IDS.MAIONESE, 1)

CaixaMercado1.printEntries()