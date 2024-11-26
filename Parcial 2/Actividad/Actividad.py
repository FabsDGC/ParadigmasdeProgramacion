class Animal:
    def __init__(self, name):
        self.name = name
        self._age = 0
        self._color = None  # Atributo privado color

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def comer(self):
        return f"{self.name} is eating."

    def setColor(self, color):
        self._color = color

    def getColor(self):
        return self._color

    def set_age(self, age):
        self._age = age

    def get_age(self):
        return self._age

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"
    
    def comer(self):
        return f"{self.name} is eating dog food."

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"
    
    def comer(self):
        return f"{self.name} is eating cat food."

# Nueva clase derivada: Fish
class Fish(Animal):
    def speak(self):
        return f"{self.name} doesn't speak. It swims silently."
    
    def comer(self):
        return f"{self.name} is eating fish food."

# Nueva clase derivada: Bird
class Bird(Animal):
    def speak(self):
        return f"{self.name} says Chirp!"
    
    def comer(self):
        return f"{self.name} is eating bird seed."

# Ejemplo de uso
dog = Dog("Rex")
cat = Cat("Whiskers")
fish = Fish("Goldie")
bird = Bird("Tweety")

# Establecer colores
dog.setColor("Brown")
cat.setColor("Black")
fish.setColor("Gold")
bird.setColor("Yellow")

print(dog.speak())  # Rex says Woof!
print(cat.speak())  # Whiskers says Meow!
print(fish.speak())  # Goldie doesn't speak. It swims silently.
print(bird.speak())  # Tweety says Chirp!

# Métodos comer
print(dog.comer())  # Rex is eating dog food.
print(cat.comer())  # Whiskers is eating cat food.
print(fish.comer())  # Goldie is eating fish food.
print(bird.comer())  # Tweety is eating bird seed.

# Métodos de edad y color
dog.set_age(3)
cat.set_age(5)
print(dog.get_age())  # 3
print(cat.get_age())  # 5

print(dog.getColor())  # Brown
print(cat.getColor())  # Black
print(fish.getColor())  # Gold
print(bird.getColor())  # Yellow
