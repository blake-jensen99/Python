class BankAccount:
    # don't forget to add some default values for these parameters!
    int_rate = 0
    balance = 0
    accounts = []

    def __init__(self, int_rate, balance, first_name, last_name): 
        self.int_rate = int_rate
        self.balance = balance
        self.first_name = first_name
        self.last_name = last_name
        self.__class__.accounts.append(self)
    
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self
        else:
            print("Insufficient balance :-(")
            return self
    
    def display_account_info(self):
        print(f"{self.balance} \n{self.first_name} {self.last_name}")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
            return self
        else:
            print("Cannot yield interests.")
            return self
        
    @classmethod
    def print_all(cls):
        all = ""
        for index in cls.accounts:
            all += f"{index.balance}"
            all += "\n"
            all += index.first_name + " " + index.last_name
            all += "\n"
        return all


benni = BankAccount(.10, 0, "Ben", "Thing")
todd = BankAccount(.50, 0, "Todd", "Phil")


benni.deposit(500).deposit(1500).deposit(2000).withdraw(1000).yield_interest().display_account_info()
todd.deposit(10000).deposit(101).withdraw(1234).withdraw(23).withdraw(323).yield_interest().display_account_info()


print(BankAccount.print_all())