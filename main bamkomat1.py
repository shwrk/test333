class BankAccount:
    balance: float = 1000

    def apdate_balance(self, amount: float):
        # a = self.balance
        self.balance += amount


class BankCard:
    balance = 100

    def withdraw_cash(self, amount: float):
        if amount > self.balance:
            print('недостаточно средств. Попытка снять:', amount,'. Баланс:', self.balance)
            return
        self.balance -= amount

    def topup_cash(self, amount: float):
        self.balance += amount

    def transfer_money(self, amount: float, to_account: BankAccount):
        if amount > self.balance:
            print('недостаточно средств. Попытка перевести:', amount, '. Баланс:', self.balance)
        self.balance -= amount
        to_account.apdate_balance(amount)

bankAcc1 = BankAccount()
bankCard1 = BankCard()

print('Исходный баланс: ', bankAcc1.balance)

bankAcc1.apdate_balance(100)

print('баланс +100: ', bankAcc1.balance)

bankAcc1.apdate_balance(-200)
print('баланс +200: ', bankAcc1.balance)

cash: float = 120
bankCard1.withdraw_cash(cash)
print('снять с карты ',cash,': ',bankCard1.balance)

cash = 80
bankCard1.transfer_money(cash, bankAcc1)
print('сумма перевода:',cash,'. Осталось на карте: ',bankCard1.balance, '. Пополненный счет:' ,bankAcc1.balance)

