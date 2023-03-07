"""
    This is the module that will implement all classes for Account. The chields Savings and Checking extand from account
    Account -> Savings
    Account -> Checking
    The checking account must have a limit 
    Account (super class) must have Agency Number and Balance
    Account (super class) must have a method to deposity and an Abstract to Withdraw
    Polimorfism -> The Abstract method withdraw is declared in the parent Account and redeclatred in the chield to be implemented

    ABC Abstract Base Class: This is an abstract metaclass that derivates abstract methods to be implemented as concrete methods in the child class
    https://docs.python.org/pt-br/3/library/collections.abc.html#module-collections.abc

"""
import abc
from dataclasses import dataclass

# ABC Abstract Base Class 
@dataclass
class Account(abc.ABC):
    agency         : int
    account_number : int
    bank_ballance  : float

    # this method is abstract because the child must implement the rules of withdraw. Saving withdraw id different of Checking withdraw
    @abc.abstractmethod
    def withdraw(self, amount: float) -> float : ...
        
    def deposity(self, amount):
        self.bank_ballance += amount
        self.ballance_detail(f'Deposity of {amount}')

    def ballance_detail(self, msg: str = '') -> None:
        print(f' The total ballance is {self.bank_ballance} {msg}')


class Savings(Account):
    """
        Savings Account must extand from account
        It must implement the polimorfic method witthdraw 
    """
    def withdraw(self, amount: float) -> float:
        after_withdraw = self.bank_ballance - amount

        if after_withdraw >= 0:
            self.bank_ballance -= amount
            self.ballance_detail(f'(WITHDRAW {amount})')
            return self.bank_ballance

        print('Não foi possível sacar o valor desejado')
        self.ballance_detail(f'(SAQUE NEGADO {amount})')
        return self.bank_ballance 


class Checkings(Account):
    """
        Checking account must have an extra limit
        It must extand Class Account
        Implement the polimorfic method withdraw
    """

    def __init__(self, agency : int, account_number : int, bank_ballance : float = 0, limit: float = 0):
        super().__init__(agency, account_number, bank_ballance)
        self.limit = limit
        
    def withdraw(self, amount: float) -> float:
        after_withdraw = self.bank_ballance - amount
        max_limit = -self.limit

        if after_withdraw >= max_limit:
            self.bank_ballance -= amount
            self.ballance_detail(f'(Withdraw {amount})')
            return self.bank_ballance

        print(f'Your ballance is {-self.limit:.2f}')
        self.ballance_detail(f'(WITHDRAW DENIED {amount})')
        return self.bank_ballance 

# to test the module here uncomment below
# if __name__ == '__main__':
#     ...