class Animal :
    
    def __init__(self,name="Unknown",legs=4,color="black",specie="unknown",age=1):
        self.name = name
        self.legs = legs
        self.age = age
        self.specie=specie
        
    def move(self,distance=1):
        print("{} moved by {} units !".format(self.name,distance))
    
    def introduce(self):
        attr=vars(self)
        for var in attr:
            print("{} : {}".format(var,attr[var]))

class Cat(Animal) :
    
    def __init__(self,OOP=False,**kwargs):
        Animal.__init__(self)
        self.OOP = OOP
        self.specie="Cat"
        self.legs=4
        if 'name' in kwargs:
            self.name=kwargs['name']
        if 'color' in kwargs:
            self.color=kwargs['color']
        if 'age' in kwargs:
            self.age=kwargs['age']
    
    def is_bamboozled(self):
        if self.OOP:
            return False
        else:
            return True
    
    def react(self,meow_count=5):
        if self.is_bamboozled():
            print("Hecking Bamboozled just use OOP!")
        else:
            print("The code is alright Hooman,phew!, play some mewsic")
            play_meow(meow_count)
    
    def introduce(self):
        for var,val in vars(self).items():
            print("{} : {}".format(var,val))
    
    def move(self,distance=1):
        print("Cat",end=' ')
        super().move(distance)
    
def play_meow(count):
    for i in range(count):
        print("meow",end='\t')