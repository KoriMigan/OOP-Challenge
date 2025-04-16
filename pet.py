# Creating pet class for use of attributes, methods and constructors

class Pet:
    def __init__(self, name):
        self.name= name 
        self.hunger= 5
        self.energy= 5
        self.happiness= 5
        self.tricks= []

    def eat(self):
        """method for pet eating"""
        self.hunger= max(0, self.hunger-3)
        self.happiness= min(10, self.happiness+1)
        print(f"{self.name} is eating! 🦴")

    def sleep(self):
        """method for pet sleeping"""
        self.energy= min(10, self.energy+5)
        print(f"{self.name} is taking a nap. Zzz... 😴")

    def play(self):
        """method for pet playing"""
        if self.energy>= 2:
            self.energy-= 2
            self.happiness= min(10, self.happiness+2)
            self.hunger= min(10, self.hunger+1)
            print(f"{self.name} is playing! 😄")
        else:
            print(f"{self.name} is too tired to play right now.😥 They should rest.")

    def get_status(self):
        """methof for getting status of pet"""
        print(f"---{self.name}'s status---")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")
        print()

    def train(self, trick):
        """method for pet tricks"""
        self.tricks.append(trick)
        print(f"{self.name} has learned a new trick: {trick}! 🎉")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows these tricks: {', '.join(self.tricks)} 🎇")
        else:
            print(f"{self.name} hasn't learned any tricks yet. 😪")