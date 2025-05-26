from enum import Enum

class VALIDATION(Enum):
    NON_VALIDATED = 0
    VALIDATED = 1

class VALID_PAYMENT_METHODS(Enum):
    CREDITO = 1
    DEBITO = 2
    DINHEIRO = 3
    PIX = 4

class ITEMS_IDS(Enum):
    COCA_LATA = 5758
    MAIONESE = 9324
    PIRULITO = 4545