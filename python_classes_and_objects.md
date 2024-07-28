# Classes and Objects

**Objects** are a representation of real world objects like cars, dogs, or bikes. 
The objects share two main characteristics: *data* and *behavior*.

Cars have data, like number of wheels, number of doors, and seating capacity They also exhibit behavior: 
they can accelerate, stop, show how much fuel is left, and so many other things.

We identify *data* as *attributes* and *behavior* as *methods* in **object-oriented programming**. 

Data → Attributes 
Behavior → Methods

**Class** is the *blueprint from which individual objects are created*. 
In the real world, we often find many objects with the same type. Like cars. 
All the same make and model (and all have an engine, wheels, doors, and so on). 
Each car was built from the same set of blueprints and has the same components.

**Python**, as an *Object-Oriented programming language*, has these concepts: **class** and **object**.

**Class** is a *blueprint*, a *model for its objects*.
**Class** is just a *model*, or *a way to define attributes and behavior*.
 
Python syntax for classes:

  class Vehicle:
      pass

**Objects** are *instances of a class*. We create an **instance** by *naming the class*.

  car = Vehicle()
  print(car)

Here car is an object (or instance) of the class Vehicle.

Here car is an object (or instance) of the class Vehicle.

Remember that our *vehicle class* has *four attributes*: 
number of wheels, type of tank, seating capacity, and maximum velocity. 
We set all these attributes when creating a vehicle object. 

So here, we *define our class* to receive data when it *initiates* it:

  class Vehicle:
      def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
          self.number_of_wheels = number_of_wheels
          self.type_of_tank = type_of_tank
          self.seating_capacity = seating_capacity
          self.maximum_velocity = maximum_velocity

We use the **init** method. We call it a *constructor method*. So when we create the *vehicle object*, 
we can *define these attributes*. Imagine that we love the Tesla Model S, and we want to *create this kind of object*. 

It has four wheels, runs on electric energy, has space for five seats, and the maximum velocity is 250km/hour (155 mph). 

Let’s create this *object*:

  tesla_model_s = Vehicle(4, 'electric', 5, 250)

All attributes are set. But how can we access these attributes’ values? 
*We send a message to the object asking about them*. We call it a **method**. 
  
It’s the *object’s behavior*. 

Let’s implement it:

  class Vehicle:
      def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tank = type_of_tank
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity

      def number_of_wheels(self):
        return self.number_of_wheels

      def set_number_of_wheels(self, number):
        self.number_of_wheels = number

This is an implementation of two methods: number_of_wheels and set_number_of_wheels. 

We call it **getter** and **setter**. 

Because the *first **gets** the attribute value*, 
and the *second **sets** a new value for the attribute*.

In Python, we can do that using **@property (decorators)** to *define getters and setters*. 

Let’s see it with code:

  class Vehicle:
    def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tank = type_of_tank
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity
    
    @property
    def number_of_wheels(self):
        return self.__number_of_wheels
    
    @number_of_wheels.setter
    def number_of_wheels(self, number):
        self.__number_of_wheels = number

________________________________________

Python is an object oriented programming language.
Almost everything in Python is an object, with its properties and methods.
A Class is like an object constructor, or a "blueprint" for creating objects.

Create a class named MyClass, with a property named x:

  class MyClass:
    x = 5

Create an object named p1, and print the value of x:

  p1 = MyClass()
  print(p1.x)

## The __init__() Function

The examples above are classes and objects in their simplest form, and are not 
really useful in real life applications.

To understand the meaning of classes we have to understand the built-in __init__() function.

All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or other operations that are necessary 
to do when the object is being created:

Create a class named Person, use the __init__() function to assign values for name and age:

  class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  p1 = Person("John", 36)

  print(p1.name)
  print(p1.age)

*The __init__() function is called automatically every time the class is being used to create a new object.*

## The __str__() Function

The __str__() function controls what should be returned when the class object is represented as a string.

If the __str__() function is not set, the string representation of the object is returned:

The string representation of an object WITHOUT the __str__() function:

  class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  p1 = Person("John", 36)

  print(p1)

The string representation of an object WITH the __str__() function:

  class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

  p1 = Person("John", 36)

  print(p1)

## Object Methods

Objects can also contain methods. Methods in objects are functions that belong to the object.

Let us create a method in the Person class:

Insert a function that prints a greeting, and execute it on the p1 object:

  class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

  p1 = Person("John", 36)
  p1.myfunc()

## The self Parameter

**Note**: The *self parameter* is a *reference to the current instance of the class*, 
and is used *to access variables that belong to the class*.

The self parameter is a reference to the current instance of the class, 
and is used to access variables that belongs to the class.

It does NOT have to be named self , you can call it whatever you like, 
but it has to be the *first parameter* of any function in the class:

Use the words mysillyobject and abc instead of self:

  class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

  p1 = Person("John", 36)
  p1.myfunc()

## Modify Object Properties

Set the age of p1 to 40:

  p1.age = 40

## Delete Object Properties

You can delete properties on objects by using the del keyword:

  del p1.age

## Delete Objects

Delete the p1 object:

  del p1

## The pass Statement

class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

  class Person:
  pass

_______________








