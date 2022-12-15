class Vehicle:
    def __init__(self,mileage,cost):
        self.mileage=mileage
        self.cost=cost
    def show_details(self):
        print("i am Vehicle")
        print("mileage of the Vehicle is:-",self.mileage)
        print("cost of the Vehicle is:-",self.cost)
v1=Vehicle(300,500)
# v1.show_details()

class car(Vehicle):
    def __init__(self, mileage, cost,tyres,hp):
        super().__init__(mileage,cost)
        self.tyres=tyres
        self.hp=hp
    def show_car_details(self):
        print("i am car")
        print("numbres of the tyres is :-",self.tyres)
        print("value of hp is :-",self.hp)
c1=car(200,15000,2,500)

# c1.show_car_details()
c1.show_details()