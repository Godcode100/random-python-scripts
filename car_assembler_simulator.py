from random import random

class CarAssembler:
    def __init__(self):
        self.operating = False
    def check_success(self):
        if random() < 0.99:
            return True
        return False
            
    def build_engine(self):
        if self.check_success:
            print("Added engine")
        else:
            print("Failure in adding engine")
            self.operating = False
            
    def build_gearbox(self):
        if self.check_success:
            print("Built the Gear Box")
        else:
            print("Failure in bulding the gear box")
            self.operating = False
    def start_carAssembling(self):
        self.operating = True
        cars_built = 0
        while self.operating:
            cars_built+= 1
            print(f"Building Car Number: {cars_built}")
            self.build_engine()
            self.build_gearbox()
        print("Failure in the Car Assembler")
        print(f"{cars_built - 1} cars built so far")
Moto_car_plant = CarAssembler()
Moto_car_plant.start_carAssembling()
