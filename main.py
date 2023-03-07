"""
This is the module that will implement all classes for the Bank
Person -> Client
Account -> Savings
Account -> Checking
Bank -> Person & Account

ABC Abstract Base Class: This is an abstract metaclass that derivates abstract methods to be implemented as concrete methods in the child class
https://docs.python.org/pt-br/3/library/collections.abc.html#module-collections.abc

"""

from modules import person
from modules import accounts
from modules import banks

if __name__ == '__main__':
    # p1 = person.Person('Eliane Netto Silva Pinti', 40)
    # print(p1)
    # print(p1.full_name)
    # print(p1.age)
    # c1 = person.Client('Eliane Netto Silva Pinti', 30)
    # c1.account = accounts.Checkings(111, 222, 0, 0)
    # print(c1)
    # print(c1.account)
    # c2 = person.Client('Ana petrovisk junior', 18)
    # c2.conta = accounts.Savings(112, 223, 100)
    # print(c2)
    # print(c2.conta)
    # cp1 = Savings(111, 222)
    # cp1.withdraw(1)
    # cp1.deposity(1)
    # cp1.withdraw(1)
    # cp1.withdraw(1)
    # print('##')
    # cc1 = accounts.Checkings(111, 222, 0, 100)
    # cc1.withdraw(1)
    # cc1.deposity(1)
    # cc1.withdraw(1)
    # cc1.withdraw(1)
    # cc1.withdraw(98)
    # cc1.withdraw(1)
    # print('##')
    # cc1 = accounts.Checkings(111, 222, 0, 0)
    # c1.account = cc1
    # cp1 = accounts.Savings(112, 223, 100)
    # c2.account = cp1

    c1 = person.Client('Eliane Netto Silva Pinti', 30)
    cc1 = accounts.Checkings(111, 222, 0, 0)
    c1.conta = cc1
    c2 = person.Client('Ana petrovisk junior', 18)
    cp1 = accounts.Savings(112, 223, 100)
    c2.conta = cp1
    
    bank = banks.Bank()
    bank.clients = [c1, c2]
    bank.accounts = [cc1, cp1]
    bank.agencies = [111, 222]
    if bank.autenticar(c1, cc1):
        cc1.deposity(10)
        c1.account.deposity(100)
        print(c1.account)
