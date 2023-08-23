"""life cycle of a bank card."""

from datetime import datetime
import random
import string


class BankCard:
    """The class of bank card description."""

    def __init__(self, card_num, name, surname, end_date, cvv, pin):
        self.card_num = card_num
        self.name = name
        self.surname = surname
        self.end_date = end_date
        self.cvv = cvv
        self.pin = pin
        self.is_blocked = False

    @classmethod
    def generate_card_num(cls):
        # Generate a random 16-digit card number
        card_num = ''.join(random.choice(string.digits) for _ in range(16))
        return card_num

    @staticmethod
    def is_valid_end_date(date):
        # Check if the provided end date is valid
        try:
            end_date = datetime.strptime(date, '%m/%y')
            current_date = datetime.now()
            return end_date > current_date
        except ValueError:
            return False

    def block_card(self):
        self.is_blocked = True
        print("Card has been blocked.")

    def unblock_card(self):
        self.is_blocked = False
        print("Card has been unblocked.")

    def is_blocked(self):
        return self.is_blocked

    # Getters and setters
    def get_card_num(self):
        return self.card_num

    def set_card_num(self, new_card_num):
        self.card_num = new_card_num

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_surname(self):
        return self.surname

    def set_surname(self, new_surname):
        self.surname = new_surname

    def get_end_date(self):
        return self.end_date

    def set_end_date(self, new_end_date):
        if self.is_valid_end_date(new_end_date):
            self.end_date = new_end_date
        else:
            print("Invalid end date format or expired.")

    def get_cvv(self):
        return self.cvv

    def set_cvv(self, new_cvv):
        self.cvv = new_cvv

    def get_pin(self):
        return self.pin

    def set_pin(self, new_pin):
        self.pin = new_pin


if __name__ == '__main__':
    card_num = BankCard.generate_card_num()
    card = BankCard(card_num, "John", "Doe", "08/25", "123", "9876")

    print("Card number:", card.get_card_num())
    print("Card holder:", card.get_name(), card.get_surname())
    print("Card end date:", card.get_end_date())

    card.block_card()
    print("Is card blocked?", card.is_blocked)
    card.unblock_card()
    print("Is card blocked?", card.is_blocked)

    new_end_date = "12/27"
    card.set_end_date(new_end_date)
    print("New card end date:", card.get_end_date())
