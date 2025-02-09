class Amount:

    def __init__(self, amount, timestamp, transaction_type):
        self.amount = amount
        self.timestamp = timestamp
        self.transaction_type = transaction_type

    def __str__(self):
        return (f'{self.transaction_type}: {self.amount} som.')
