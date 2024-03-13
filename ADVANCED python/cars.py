class MyCars:
    def __init__(self, *my_cars) -> None:
        self.my_cars = list(my_cars)
        self._i = 0
    
    
    def add_car(self, car_name):
        self.my_cars.append(car_name)
        
    def remove_car(self, car_name):
        self.my_cars.remove(car_name)
        
    def __iter__(self):
        return self