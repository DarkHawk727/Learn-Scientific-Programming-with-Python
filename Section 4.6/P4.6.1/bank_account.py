class BankAccount:
    """ An abstract base class representing a bank account."""
    currency = '$'

    def __init__(self, customer, account_number, overdraft, balance=0):
        """
        Initialize the BankAccount class with a customer , account number
        and opening balance (which defaults to 0.)
        """

        self.customer = customer
        self.account_number = account_number
        self.balance = balance


    def set_account_num(self, account_number):
        if not self.verify_account_num:
            raise ValueError('INVALID ACCOUNT NUMBER!')

        self.account_number = account_number


    def validate_account_num(self, account_number):
        ccl = [int(digit) for digit in str(account_number) if digit not in ('-', ' ')]

        for i in range(len(ccl)-2, 0, -2):
            ccl[i] *= 2
            if ccl[i] > 9:
                ccl[i] = 1 + (ccl[i] - 10)
        checksum = sum(ccl) % 10
        return not checksum


    def deposit(self, amount):

        """ Deposit amount into the bank account."""
        if amount > 0:
            self.balance += amount
        else:
            print('INVALID DEPOSIT AMOUNT:', amount)


    def withdraw(self, amount):

        """
        Withdraw amount from the bank account , ensuring there are sufficient
        funds.
        """
        if amount > 0:
            if amount > self.balance:
                print('INSUFFICIENT FUNDS!')
            else:
                self.balance -= amount
        else:
            print('INVALID WITHDRAWAL AMOUNT: ', amount)
    

    def check_balance(self):
        """" Print a statement of the account balance. """
        print('The balance of of account number {:d} is {:s}{:0.2f}'.format(self.account_number, self.currency, self.balance))


class CurrentAccount(BankAccount):
    """ A class representing a current (checking) account. """
    def __init__(self , customer , account_number, annual_fee, transaction_limit, overdraft, balance=0):
        """ Initialize the current account. """
        self.overdraft = overdraft
        self.annual_fee = annual_fee
        self.transaction_limit = transaction_limit
        super().__init__(customer , account_number , balance)


    def withdraw(self , amount):
        """
        Withdraw amount if sufficient funds exist in the account and amount
        is less than the single transaction limit.
        """
        if amount  <= 0:
            print('INVALID WITHDRAWAL AMOUNT: ', amount)
            return

        if amount > self.balance + self.overdraft:
            print('INSUFFICIENT FUNDS!')
            return

        if amount > self.transaction_limit:
            print('{0:s}{1:.2f} exceeds the single transaction limit of'
            ' {0:s}{2:.2f}'.format(self.currency , amount ,
            self.transaction_limit))
            return
            
        self.balance -= amount


    def apply_annual_fee(self):
        """ Deduct the annual fee from the account balance. """
        self.balance = max(0., self.balance - self.annual_fee)