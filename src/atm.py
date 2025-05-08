class InvalidPinException(Exception):
    pass

class InsufficientFundsException(Exception):
    pass

class ATM:
    def __init__(self):
        self._pin = 1234
        self._balance = 0.0

    def check_balance(self, pin: int) -> float:
        if pin != self._pin:
            raise InvalidPinException("Nieprawidłowy PIN")
        return self._balance

    def deposit(self, pin: int, amount: float) -> float:
        if pin != self._pin:
            raise InvalidPinException("Nieprawidłowy PIN")
        if amount <= 0:
            raise ValueError("Kwota musi być większa od zera")
        self._balance += amount
        return self._balance

    def withdraw(self, pin: int, amount: float) -> float:
        if pin != self._pin:
            raise InvalidPinException("Nieprawidłowy PIN")
        if amount <= 0:
            raise ValueError("Kwota musi być większa od zera")
        if amount > self._balance:
            raise InsufficientFundsException("Niewystarczające środki")
        self._balance -= amount
        return self._balance
