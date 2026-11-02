# penguin.py
# Jayden Reutzel
# 11/1/2026
# Class representing a penguin

class Penguin:
    # initialize a new Penguin object
    def __init__(self, sample_number, species, body_mass):
        self.sample_number = sample_number
        self.species = species
        self.body_mass = body_mass
    # display this penguins attributes
    def display_info(self):
        print(f"Sample Number: {self.sample_number}")
        print(f"Species: {self.species}")
        print(f"Body Mass: {self.body_mass} g")
