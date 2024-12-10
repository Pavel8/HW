class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.penalties - []

    def add_penalty(id, penalty):
        self.penalties.append(penalty)

    def remove_penalty(self, penalty):
        self.penalties.remove(penalty)

    def update_info(self, name=None, address=None):
        if name:
            self.name = name
        if address:
            self.address = address

    def __str__(self):
        penalties = '\n'.join(str(p) for p in self.penalties)
        return f"{self.personal_id} - {self.name}, {self.address}\nPokuty:\n{penalties}"
        