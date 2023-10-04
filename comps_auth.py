from COMPS import Client, AuthManager
from COMPS.CredentialPrompt import CredentialPrompt

compshost = 'https://comps.idmod.org'


class StaticCredentialPrompt(CredentialPrompt):

    def __init__(self, username, pwd):
        self._times_prompted = 0
        self._username = username
        self._password = pwd

    def prompt(self):
        self._times_prompted = self._times_prompted + 1
        if self._times_prompted > 3:
            raise RuntimeError('Failure authenticating')
        return { 'Username': self._username, 'Password': self._password }


def go( user, pwd ):
    Client.login(compshost, StaticCredentialPrompt( user, pwd ))