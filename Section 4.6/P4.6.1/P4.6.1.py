from bank_account import BankAccount, CurrentAccount, SavingsAccount
from customer import Customer

my_customer = Customer('John Doe', '123 Street S', '1999-01-01')
my_account = BankAccount(my_customer, 12121412412, 200, 1000.0)

my_account.withdraw(2000.0)







