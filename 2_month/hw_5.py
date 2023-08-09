class Animal:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        
    def get_name(self):
        return self._name
    
    def get_age(self):
        return self._age
    
    
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self._breed = breed
        
        
    def bark(self):
        print(f"{self._name} is barking")
        
    def get_breed(self):
        return self._breed
    
        
        
class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self._color = color
        
        
    def meow(self):
        print(f"{self._name} is meowing")
        
        
    def get_color(self):
        return self._color
    
    
dog = Dog("Haha", 3, "husky")
print(dog.get_name())
print(dog.get_age())
print(dog.get_breed())

cat = Cat("Hihi", 2, "orange")
print(cat.get_name())
print(cat.get_age())
print(cat.get_color()) 

        