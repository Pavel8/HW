import json
import pickle

class Stadium:
    def __init__(self, name, capacity, location):
        self.name = name
        self.capacity = capacity
        self.location = location

    def __str__(self):
        return f"Stadium(name: {self.name}, capacity: {self.capacity}, location: {self.location})"
    
    def to_json(self):
        stadium_dict = {
            'name': self.name,
            'capacity': self.capacity,
            'location': self.location
        }
        return json.dumps(stadium_dict)
    
    @staticmethod
    def from_json(json_data):
        data = json.loads(json_data) 
        return Stadium(data['name'], data['capacity'], data['location'])

    def to_pickle(self):
        return pickle.dumps(self)
    
    @staticmethod
    def from_pickle(pickle_data):
        return pickle.loads(pickle_data)
    

stadium = Stadium("Luzanky", 25000, "Brno")

json_data = stadium.to_json()
print("JSON Data:", json_data)

stadium_from_json = Stadium.from_json(json_data)
print("Deserialized from JSON:", stadium_from_json)

pickle_data = stadium.to_pickle()
print("Pickle Data:", pickle_data)

stadium_from_pickle = Stadium.from_pickle(pickle_data)
print("Deserialized from Pickle:", stadium_from_pickle)