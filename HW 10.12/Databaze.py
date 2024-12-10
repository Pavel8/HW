from Penalty_class import Penalty
from Person_class import Person

class Tax_data:
    def __init__(self):
        self.people = {}

    def add_person(self, id, name):
        if id not in self.people:
            self.people[id] = Person(id, name)
        else:
            print(f"Osoba s ID {id} již existuje.")
    
    
    def add_penalty_to_person(self, id, penalty):
        osoba = self.people.get(id)
        if osoba:
            osoba.add_penalty(penalty)
        else:
            print(f"Osoba s ID {id} nebyla nalezena.")
    
    def delete_penalty(self, id, penalty):
        osoba = self.people.get(id)
        if osoba:
            osoba.remove_penalty(penalty)
        else:
            print(f"Osoba s ID {id} nebyla nalezena.")


    def replace_person_info(self, id, name=None, address=None):
        osoba = self.people.get(id)
        if osoba:
            osoba.update_info(name, address)
        else:
            print(f"Osoba s ID {id} nebyla nalezena.")
    
    def get_person_by_id(self, id):
        return str(self.people.get(id, "Osoba nebyla nalezena."))
    
    def get_penalties_by_type(self, penalty_type):
        penalties = []
        for person in self.people.values():
            for penalty in person.penalties:
                if penalty.penalty_type == penalty_type:
                    penalties.append((person.id, penalty))
        return penalties
    
    def get_penalties_by_city(self, city):
        penalties = []
        for person in self.people.values():
            for penalty in person.penalties:
                if penalty.city == city:
                    penalties.append((person.id, penalty))
        return penalties

    def print_full_database(self):
        for person in self.people.values():
            print(person)

    def print_penalties_by_code(self, id):
        print(self.get_person_by_id(id))
    
    def print_penalties_by_type(self, penalty_type):
        penalties = self.get_penalties_by_type(penalty_type)
        for pid, penalty in penalties:
            print(f"ID: {pid} - {penalty}")
    
    def print_penalties_by_city(self, city):
        penalties = self.get_penalties_by_city(city)
        for pid, penalty in penalties:
            print(f"ID: {pid} - {penalty}")

TX1 = Tax_data()

TX1.add_person(1, "Pavel Kadlec", "Brno")
TX1.add_penalty_to_person(1, penalty1)
TX1.print_full_database()