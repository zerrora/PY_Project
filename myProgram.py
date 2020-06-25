class Computer:
    def __init__(self, name):
        self.name = name

class Computer:
    def __init__(self, name):
        self.name = name
    def playGame(self):
        print("The computer is now playing: %s"%(self.name))

class Laptop(Computer):
    def __init__(self, name):
        self.name = name

class Desktop(Computer):
    def __init__(self, name):
        self.name = name

game1=Laptop("Call of Duty: Modern Warfare")
game2=Desktop("Valorant")
game3=Desktop("Maplestory")
game4=Laptop("Geometry Dash")
game1.playGame()
game2.playGame()
game3.playGame()
game4.playGame()