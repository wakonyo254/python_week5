class Wildnimal:
    def __init__(self, species, habitat, is_endagered):
        self.species = species
        self.habitat = habitat
        self.is_endagered = is_endagered

    def hunt(self):
        print(f"{self.species} is hunting at {self.habitat}.")

    def display_status(self):
        status = "endagered" if self.is_endagered else "not endagered"
        print(f"The {self.species} is {status}")        


    if __name__ == "__main__":
        tiger = Wildanimal('Tiger', "Masai-Mara", false)

        print(tiger.hunt())
        print(tiger.display_status)    