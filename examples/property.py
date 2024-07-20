class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # "Внутренний" атрибут

    def get_balance(self):
        print('get balance:')
        return self._balance

    def set_balance(self, new_balance):
        if new_balance >= 0:
            self._balance = new_balance
        else:
            print("Error: Balance cannot be negative!")

    balance = property(get_balance, set_balance)


# Создаем объект класса BankAccount
account = BankAccount(1000)

# Используем свойство для получения и установки баланса
print(account.balance)  # Выведет: 1000

# account.balance = 1500
# print(account.balance)  # Выведет: 1500

# account.balance = -500  # Ошибка: Balance cannot be negative!
