class Animal:
    def __init__(self, name, species, age, sound):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound
    def __str__(self):
        return (f'Specifications: {self.name} is a {self.species}. She is {self.age} years old. {self.name} can say {self.sound} :)')
    
    def make_sound(self):
        print(f'{self.name} says {self.sound}!')

lion = Animal('Leo','lion', 4, 'Ghorresh')
print(lion)
lion.make_sound()
