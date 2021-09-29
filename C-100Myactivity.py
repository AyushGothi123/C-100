class Car:
    colour = "red"
    seater = 4
    name = "maruti"
    
    def __init__(self,colour,name,seater):
        self.colour = colour
        self.seater = seater
        self.name = name

    def ready(self):
        print("You have ordered",self.name," its a",self.seater," colour is",self.colour)

c1 = Car("purple","kia",6)
c1.ready()

c2 = Car("yellow","hundai",2)
c2.ready()


        



