from unittest.mock import Mock

from Bank import BankAccount
import pytest
from Bank import NegativeNumberError
from stock_database import Stock


@pytest.fixture
def mybank():
    return BankAccount("Joe", 1000)

def test_can_add_money_to_bank(mybank):
    mybank.deposit(150)
    assert mybank.balance == 150


def test_cant_add_negative_money_to_bank(mybank):
    with pytest.raises(NegativeNumberError):
        mybank.deposit(-150)


def test_cant_take_negative_money(mybank):
    with pytest.raises(NegativeNumberError):
        mybank.withdraw(-150)


def test_cant_take_more_than_limit_money():
    mybank = BankAccount("Joe", 1000, 1500)
    mybank.withdraw(mybank.withdraw_limit + 1)
    assert mybank.balance == 1500


def test_cant_take_more_than_balance():
    mybank = BankAccount("Joe", 1000, 400)
    mybank.withdraw(mybank.balance + 1)
    assert mybank.balance == 400


def test_can_add_account_name(mybank):
    assert mybank.account_holder == "Joe"
    print("Add account name success")


def test_add_stock_name(mybank):
    mybank.add_stock("CSCO")
    assert "CSCO" in mybank.stocks


def test_get_total_stock_price():
    mybank = BankAccount("Joe", 1000, 1500)
    mybank.add_stock("CSCO")
    mybank.add_stock("MDT")
    stock_database = Stock()

    def mock_get_stock(stock_name):
        if stock_name == "CSCO":
            return 53.2
        if stock_name == "MDT":
            return 81.3

    stock_database.get = Mock(side_effect=mock_get_stock)
    assert mybank.get_total_stock_price(stock_database) == 187.7

    # Run the test -> pytest
# Run the a test file -> pytest QA_Automation/test_Bank.py
# Run a function inside a test file -> pytest QA_Automation/test_Bank.py::test_can_add_account_name
# Run and show prints -> pytest -s
