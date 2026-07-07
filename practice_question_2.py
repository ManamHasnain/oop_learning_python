class Account:
    def __init__(self, account_no, balance=0):
        # Initialize account number and balance
        self.account_no = account_no
        self.__balance = balance

    # Method to withdraw money
    def debit(self, amount):
        # Check if sufficient balance is available
        if amount > self.__balance:
            print("❌ Insufficient balance!")
        else:
            self.__balance -= amount
            print(f"✅ {amount} withdrawn from Account {self.account_no}")
            self.show_balance()

    # Method to deposit money
    def credit(self, amount):
        self.__balance += amount
        print(f"✅ {amount} deposited into Account {self.account_no}")
        self.show_balance()

    # Method to display current balance
    def show_balance(self):
        print(f"💰 Current Balance: {self.__balance}\n")


# -------------------------------
# Main Program (User Interaction)
# -------------------------------

# Creating first user account using input
balance = int(input("Enter initial balance: "))
account_no = input("Enter account number: ")

user1 = Account(account_no, balance)

withdraw_amount = int(input("Enter amount to withdraw: "))
user1.debit(withdraw_amount)

deposit_amount = int(input("Enter amount to deposit: "))
user1.credit(deposit_amount)


# Creating second user account (hardcoded example)
print("\nuser 2 transaction details")
print()
user2 = Account(9086543, 10000)

# Performing transactions for user2
user2.debit(1000)        # Withdraw money
user2.credit(500)        # Deposit money
user2.credit(90000)      # Salary credited
user2.debit(30000)       # Grocery shopping
