class Animal {
    private String name;
    private int _age;
    private String _color;  // Atributo privado color

    public Animal(String name) {
        this.name = name;
        this._age = 0;
        this._color = null;
    }

    public void speak() {
        throw new UnsupportedOperationException("Subclass must implement abstract method");
    }

    public String comer() {
        return name + " is eating.";
    }

    public void setColor(String color) {
        this._color = color;
    }

    public String getColor() {
        return this._color;
    }

    public void setAge(int age) {
        this._age = age;
    }

    public int getAge() {
        return this._age;
    }

    public String getName() {
        return this.name;
    }
}

class Dog extends Animal {
    public Dog(String name) {
        super(name);
    }

    @Override
    public void speak() {
        System.out.println(getName() + " says Woof!");
    }

    @Override
    public String comer() {
        return getName() + " is eating dog food.";
    }
}

class Cat extends Animal {
    public Cat(String name) {
        super(name);
    }

    @Override
    public void speak() {
        System.out.println(getName() + " says Meow!");
    }

    @Override
    public String comer() {
        return getName() + " is eating cat food.";
    }
}

// Nueva clase derivada: Fish
class Fish extends Animal {
    public Fish(String name) {
        super(name);
    }

    @Override
    public void speak() {
        System.out.println(getName() + " doesn't speak. It swims silently.");
    }

    @Override
    public String comer() {
        return getName() + " is eating fish food.";
    }
}

// Nueva clase derivada: Bird
class Bird extends Animal {
    public Bird(String name) {
        super(name);
    }

    @Override
    public void speak() {
        System.out.println(getName() + " says Chirp!");
    }

    @Override
    public String comer() {
        return getName() + " is eating bird seed.";
    }
}

public class Main {
    public static void main(String[] args) {
        Dog dog = new Dog("Rex");
        Cat cat = new Cat("Whiskers");
        Fish fish = new Fish("Goldie");
        Bird bird = new Bird("Tweety");

        // Establecer colores
        dog.setColor("Brown");
        cat.setColor("Black");
        fish.setColor("Gold");
        bird.setColor("Yellow");

        System.out.println(dog.getName() + " says: " + dog.comer());
        System.out.println(cat.getName() + " says: " + cat.comer());
        System.out.println(fish.getName() + " says: " + fish.comer());
        System.out.println(bird.getName() + " says: " + bird.comer());

        // Métodos de edad y color
        dog.setAge(3);
        cat.setAge(5);
        System.out.println(dog.getName() + " age: " + dog.getAge());
        System.out.println(cat.getName() + " age: " + cat.getAge());

        System.out.println(dog.getName() + " color: " + dog.getColor());
        System.out.println(cat.getName() + " color: " + cat.getColor());
        System.out.println(fish.getName() + " color: " + fish.getColor());
        System.out.println(bird.getName() + " color: " + bird.getColor());
    }
}
