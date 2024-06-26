class House:
    def __init__(self):
        self.number_of_floors = 0

    def set_new_number_of_floors(self, floors):
        self.number_of_floors = floors


Dom = House()

Dom.set_new_number_of_floors(45)

print(Dom.number_of_floors)
