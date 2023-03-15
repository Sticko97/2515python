import json


class School:
    def __init__(self, filename="bcit.json"):
        self.bcit = []
        with open("filename","r") as file:
            self.bcitjson = json.load(file)
            self.bcit.append(self.bcitjson)
            
    def load_from_json(self):
        