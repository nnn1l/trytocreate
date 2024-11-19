class Animal:
    def talk(self):
        print('Some animals are mute and some may do different sound.')
        raise NotImplementedError('Subclasses must implement this method.')

class Dog(Animal):
    def talk(self):
        print('Bark! Bark! Woof! Grrrr....')

class Cat(Animal):
    def talk(self):
        print('Meow.. Meow... Mrrrr..')

def do_voice(animal: Animal):
    animal.talk()

do_voice(Cat())
do_voice(Dog())