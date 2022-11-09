class CreditCard(object):

    def __init__(self, customer, bank, account, limit):
        self._customer = customer
        self._bank = bank
        self._account = account
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank

    def get_account(self):
        return self._account

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

    def charge(self, price):
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        self._balance -= amount


wallet = []
wallet.append(CreditCard('Moin', 'Askari Bank', '0001', 2000))
wallet.append(CreditCard('Hamza', 'HBL Bank', '0002', 3000))
wallet.append(CreditCard('Junaid', 'Allied Bank', '0003', 5000))
print()

for val in range(1, 17):
    wallet[0].charge(val)
    wallet[1].charge(val*2)
    wallet[2].charge(val*3)


for c in range(3):
    print('Customer : ', wallet[c].get_customer())
    print('Bank     : ', wallet[c].get_bank())
    print('Account  : ', wallet[c].get_account())
    print('Limit    : ', wallet[c].get_limit())
    print('Balance  : ', wallet[c].get_balance())

    while wallet[c].get_balance() > 100:
        wallet[c].make_payment(100)
        print('New Balance : ', wallet[c].get_balance())
    print()
