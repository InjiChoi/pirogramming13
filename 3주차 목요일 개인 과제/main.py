import random

class Account:
    account_count=0
    
    def __init__(self, name, balance):
        self.deposit_count =0

        self.deposit_list = []
        self.withdraw_list = []
        
        self.bank = 'sc은행'
        self.name = name
        self.balance = balance
        # acount number
        num1 = random.randint(0,999)
        num1 = str(num1).zfill(3)
        num2 = random.randint(0,99)
        num2 = str(num2).zfill(2)
        num3 = random.randint(0,999999)
        num3 = str(num3).zfill(6)
        self.account_num = num1 + '-' + num2 + '-' + num3

        #account_count
        Account.account_count += 1
        
    @classmethod
    def get_account_num(cls):
        print(cls.account_count)

    # 입금 메서드
    def deposit(self, money):
        if money>=1:
            self.balance += money
            self.deposit_list.append(money)
            self.deposit_count += 1
            if self.deposit_count % 5 == 0:
                self.balance *= 1.01 
            
    # 출금 메서드
    def withdraw(self, money):
        if self.balance >= money:
            self.balance -= money
            self.withdraw_list.append(money)

    # 정보 출력 메서드
    def display_info(self):
        self.balance = format(self.balance, ',')
        print('은행이름:', self.bank)
        print('예금주:', self.name)
        print('계좌번호:', self.account_num)
        print(f'잔고:{self.balance}원')

    # 입금 내역 출력 메서드
    def deposit_history(self):
        for money in self.deposit_list:
            print(money)
            
    # 출금 내역 출력 메서드
    def withdraw_history(self):
        for money in self.withdraw_list:
            print(money)
    
piro = Account("피로", 100342432)
gram = Account("그램", 123231)
ming = Account("밍", 1265336)

accounts = []
accounts.append(piro)
accounts.append(gram)
accounts.append(ming)

# 잔고 100만원 이상 고객 출력
for account in accounts:
    if account.balance >= 1000000:
        account.display_info()



