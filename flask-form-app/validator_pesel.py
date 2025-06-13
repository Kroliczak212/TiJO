import re
from validator import Validator
from register_form_fields import RegisterFormFields

class PeselValidator(Validator):
    def __init__(self, pesel):
        self.pesel = pesel
        # wagi do sumy kontrolnej
        self.weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]

    def is_valid(self):
        if not self.pesel or not re.fullmatch(r'\d{11}', self.pesel):
            return False

        digits = list(map(int, self.pesel))
        checksum = sum(w * d for w, d in zip(self.weights, digits))
        control = (10 - (checksum % 10)) % 10
        return control == digits[-1]

    def field_name(self):
        return RegisterFormFields.PESEL