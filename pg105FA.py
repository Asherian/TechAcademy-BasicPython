

#Parent Class, multi part pg105, pg106, 
class Organism:
    name="Unknown"
    species="Unknown"
    legs=None
    #None is its own special data type- recognized like boolean.
    arms=None
    dna="Sequence A"
    origin="Unknown"
    carbon_based=True

    def information(self):
        #Passing self allows access to variables within class
        msg= "\nName: {}\nSpecies: {}\nLegs: {}\nArms: {}\nDNA: {}\nOrigin: {}\nCarbon Based: {}".format(self.name,self.species,self.legs,self.arms,self.dna,self.origin,self.carbon_based)
        return msg
    
#child class intance
class Human(Organism):
    name = 'MacGayver'
    species = 'homosapien'
    legs = 2
    arms = 2
    origin= 'Earth'
    

    def ingenuity(self):
        msg="\nCreates a deadly weapon using only a paperclip, chewing gum, and a roll of duct tape!"
        return msg

##anotehr child class

class Dog(Organism):
    name = 'Spot'
    species = 'canine'
    legs = 4
    arms = 0
    dna = 'Sequence B'
    origin = 'Earth'

    def bite(self):
        msg="\nEmits a loud, menancing growl and bites down ferociously on its target!"
        return msg
    
#Another child class

class Bact(Organism):
    name = 'X'
    species = 'bacteria'
    legs = 0
    arms = 0
    dna = 'Sequence C'
    origin = 'Mars'

    def rep(self):
        msg = "\nThe cells begin to divide themselves into two separate organisms!"
        return msg



if __name__ == "__main__":
    human =Human()
    print(human.information())
    print(human.ingenuity())
    
    dog=Dog()
    print(dog.information())
    print(dog.bite())
    
    bacteria=Bact()
    print(bacteria())
    print(bacteria.rep())
