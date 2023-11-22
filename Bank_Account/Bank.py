class NegativeNumberError(Exception):
    def __init__(self, message="Amount must be a positive number"):
        self.message = message
        super().__init__(self.message)


class BankAccount:
    def __init__(self, account_holder, withdraw_limit,  balance=0,stocks=[] ):
        self.account_holder = account_holder
        self.balance = balance
        self.withdraw_limit = 1000
        self.stocks = stocks

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            raise NegativeNumberError()

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.withdraw_limit:
                if amount <= self.balance:
                    self.balance -= amount
                else:
                    print(f'You cant take more than the balance which is: {self.balance}')
            else:
                print(f'You cant take more than the limit which is: {self.withdraw_limit}')
        else:
            raise NegativeNumberError()

    def check_balance(self):
        print(f"Account balance for {self.account_holder}: ${self.balance}")

    def account_info(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Balance: ${self.balance}")

    def add_stock(self, stock_name):
        self.stocks.append(stock_name)
    def get_total_stock_price(self,stock_price):
        total_price = 0
        for stock in self.stocks:
            total_price +=stock_price.get(stock)
        return total_price


