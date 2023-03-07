"""
    This is the module that will implement Classes Person and the chield Client
    
    Person -> Client

    ABC Abstract Base Class: This is an abstract metaclass that derivates abstract methods to be implemented as concrete methods in the child class
    https://docs.python.org/pt-br/3/library/collections.abc.html#module-collections.abc

    GETTTER - it is a function in an object way to generate a full name
    SETTER - it is a function in an object to update the two protected attributes
    protected attribute. It can only be used by this class and childs dela-subclasses
"""
from dataclasses import dataclass
import accounts 

# ABC Abstract Base Class 
@dataclass
class Person:
     # protected attributes
    _first_name : str
    _last_name  : []
    _age        : int

    # GETTTER
    @property
    def full_name(self):
        return f'{self._first_name} {self._last_name}'

    # SETTER 
    @full_name.setter
    def full_name(self, fullName):
        self._first_name, *self._last_name = fullName.split()

    # GETTTER
    @property
    def age(self):
        return self._age

    # SETTER
    @age.setter
    def age(self, age):
        _age = age

    def __init__(self, fullName, age):
        self._age        = age
        self.full_name  = fullName

    
@dataclass(init=False)
class Client(Person):
    """
        Client is child of Person. It inherits from Person the main attributes  
        Client Aggregates Account since a client has one account
    """
    def __init__(self, person_name, person_age):
        super().__init__(person_name, person_age)
        self.account : accounts.Account | None=None # Agreagation