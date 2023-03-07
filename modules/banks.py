"""
    This is the Class Bank
    Bank agregates with Client (inherit from Person)
    Bank aggregates with Account
    
    Withdraw is only possible with authentication true 
    Authenticate user before make changes in accounts
     
    * Check if agency in that bank account
    * Check is Client is from that Bank number 
    * Check if Account is from that Bank number
"""
from dataclasses import dataclass
import person

@dataclass
class Bank:
    agencies : list[int] | None = None
    clientList  : list[person.Person] | None = None
    accountList : list[accounts.Account] | None = None

    def _what_agency(self, thisAccount):
        if thisAccount.agency in self.agencies:
            return True # FOUND
        return False # NOT FOUND
    
    def _what_client(self, thisClient):
        if thisClient in self.clientList:
           return True # FOUND
        return False # NOT FOUND
    
    def _what_account(self, thisAccount):
        if thisAccount in self.accountList:
            return True # FOUND
        return False # NOT FOUND

    def _checa_se_conta_e_do_cliente (self, thisClient, thisAccount):
        if thisAccount is thisClient.account:
            return True # FOUND
        return False # NOT FOUND

    def autenticar(self, thisClient: person.Person, thisAccount: accounts.Account):
        return self._what_agency(thisAccount) and \
            self._what_client(thisClient) and \
            self._what_account(thisAccount) and \
            self._checa_se_conta_e_do_cliente(thisClient , thisAccount)

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencies!r}, {self.clientList!r}, {self.accountList!r})'
        return f'{class_name}{attrs}'
