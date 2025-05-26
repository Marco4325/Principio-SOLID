import ENUM

class PaymentMethod:
    __paymentMethod = ''

    def __init__(self, paymentMethod: ENUM.VALID_PAYMENT_METHODS):
        for method in ENUM.VALID_PAYMENT_METHODS:
            if method == paymentMethod:
                self.__paymentMethod = paymentMethod
                return    
        print("ERROR: Invalid Payment Method")

    def getPaymentMethod(self):
        return self.__paymentMethod