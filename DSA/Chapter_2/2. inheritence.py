from .creditclass import CreditCard

class PredatoryCreditCard(CreditCard):

    def __init__(self, customer, bank, account, limit, apr):

        super().__init__(customer, bank, account, limit)
        self._apr = apr

    def charge(self, price):

        succes = super().charge(price)
        if not succes:
            self._balance += 5
        return succes