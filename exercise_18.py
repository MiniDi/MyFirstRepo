class BankAccount:
    def __init__(self, balance, owner):
        self._balance = balance
        self._owner = owner

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"{amount} добавлено на счет.")
        else:
            print("Сумма должна быть положительной.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Сумма должна быть положительной.")
        elif amount > self._balance:
            print("Недостаточно средств на счете.")
        else:
            self._balance -= amount
            print(f"{amount} снято со счета.")

    def get_balance(self):
        return self._balance

    def get_owner(self):
        return self._owner