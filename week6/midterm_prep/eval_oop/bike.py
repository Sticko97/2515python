class Bike:
    def __init__(self):
        self.distance = 0
        self.rider = None
        
    def start_rental(self, rider):
        if self.rider == None:
            self.rider = rider
        else:
            raise RuntimeError("Ride is set")
    
    def bike(self, distance):
        if distance <= 0:
            raise AttributeError("Distance has to be a positive integer")
        if self.rider is None:
            raise RuntimeError("Rider is not set")
        self.distance += distance
        
    def end_rental(self):
        if self.rider == None:
            raise RuntimeError("Error, no rental")
        distance_rode = self.distance
        self.rider = None
        self.distance = 0
        return distance_rode
            

    
    
    
        
