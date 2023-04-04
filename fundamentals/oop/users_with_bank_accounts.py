class BankAccount:
    # don't forget to add some default values for these parameters!
    int_rate = 0
    accounts = []


    def __init__(self, int_rate, name, checking = 0, savings = 0): 
        self.int_rate = int_rate
        self.name = name
        self.checking_balance = checking
        self.savings_balance = savings
        self.__class__.accounts.append(self)
        
    
    def deposit(self, amount, type):
        if type == "checking":
            self.checking_balance += amount
        elif type == "savings":
            self.savings_balance += amount
        else:
            print("Invalid account type, please select checking or savings.")
        return self

    def withdraw(self, amount, type):
        if type == "checking":
            if self.checking_balance >= amount:
                self.checking_balance -= amount
            else:
                print("Insufficient balance :-(")
        elif type == "savings":
            if self.savings_balance >= amount:
                self.savings_balance -= amount
            else:
                print("Insufficient balance :-(")
        else:
            print("Invalid account type, please select checking or savings.")
        return self
    
    def display_account_info(self):
            print(f"Checking :{self.checking_balance}\nSavings:{self.savings_balance}")
            return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
            return self
        else:
            print("Cannot yield interests.")
            return self
        
    def money_transfer(self, amount, type, other_user, ou_type):
        if type == "checking":
            if ou_type == "checking":
                self.checking_balance -= amount
                other_user.account.checking_balance += amount
            elif ou_type == "savings":
                self.checking_balance -= amount
                other_user.account.savings_balance += amount
            else:
                print("Invalid account type, please select checking or savings.")
            return self
        elif type =="savings":
            if ou_type == "checking":
                self.savings_balance -= amount
                other_user.account.checking_balance += amount
            elif ou_type == "savings":
                self.savings_balance -= amount
                other_user.account.savings_balance += amount
            else:
                print("Invalid account type, please select checking or savings.")
            return self
        else: 
            print("Invalid account type, please select checking or savings.")
            return self


class User:
        def __init__(self, name, email, int_rate, type_of_account, balance):
            self.name = name
            self.email = email
            self.account = BankAccount(int_rate, name, type_of_account, balance)

        def make_deposit(self, amount, type):
            self.account.deposit(amount, type)
            return self

        def withdraw(self, amount, type):
            self.account.withdraw(amount, type)
            return self

        def account_balance(self):
            self.account.display_account_info()
            return self
        
        def transfer_money(self, amount, type, other_user, ou_type):
            self.account.money_transfer(amount, type, other_user, ou_type)
            return self


J = User("Jimmy John", "jjohn123@email.com", .02, 300, 200)
B = User("Billy Bob", "bbob123@email.com", .02, 4300, 1200)

B.transfer_money(200, "checking", J, "savings")

J.account_balance()
B.account_balance()


