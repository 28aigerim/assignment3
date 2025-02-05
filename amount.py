class Amount:

    def __init__(self, amount, timestamp, transaction_type):
        self.amount = amount
        self.timestamp = timestamp
        self.transaction_type = transaction_type

    def __str__(self):
        print(f'The amount in your bank account is {self.amount}')