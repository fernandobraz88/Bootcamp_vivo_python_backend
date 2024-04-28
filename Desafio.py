from abc import ABC, abstractproperty, abstractmethod
from datetime import datetime

class Cliente:
    pass


class PessoaFisica(Cliente):
    pass

class Conta:
    pass

class ContaCorrente(Conta):
    pass

class Historico:
    pass

class Transacao(ABC):
    pass