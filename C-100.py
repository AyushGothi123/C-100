class Person:
    name ="Ayush"
    age= 13

    def __init__(self,name,age):
        self.name =name
        self.age = age
        

    def adult(self):
        if(self.age>18):
            print("adult")
        else:
            print("not adult yet")



ayush = Person("ayush",13)
ayush.adult()
nisha =Person("nisha",28)
nisha.adult()