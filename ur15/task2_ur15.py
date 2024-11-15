# Create a class Dog with class attribute 'age_factor' equals to 7. Make __init__() which takes values for a dog’s age.
# Then create a method `human_age` which returns the dog’s age in human equivalent.

class Dog:
    age_factor = 7

    def __init__(self, age):
        self.age = age

try:
    dog_age = Dog(int(input("Enter dog`s age: ")))


    def human_age():
        age_human = dog_age.age_factor * dog_age.age
        print(f'In human`s age, this dog is {age_human} years old.')


    human_age()
except ValueError:
    print("Enter only whole numbers")


