class Penalty:
    def __init__(self, penalty_type, city, date, amount):
        self.penalty_type = penalty_type
        self.city = city                 
        self.date = date                 
        self.amount = amount

    def __str__(self):
        return f"{self.penalty_type}, {self.city}, {self.date}, {self.amount}"   
        