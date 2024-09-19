# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 16:37:55 2023

@author: camtr
"""

# num = 7
# print(type(num))
# print(bin(num))
# print(num.bit_length())

# class Person:
#     count = 0
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Person.count += 1

# someone = Person("Bob", 19)

# print(someone.age)
# print(someone.name)
# print(someone.__dict__)

# alicePerson = Person("Alice", 23)
# bobPerson = Person("Bob", 19)
# cindyPerson = Person("Cindy", 20)

# print(Person.count)

# print(f"I am {alicePerson.name}, there are {Person.count} people.")

class Person:
    def __init__(self, name):
        self.name = name
        print("This __init__ is from class Person")
        
    def saySth(self):
        print(f"My name is {self.name}.")
        
    def doSth(self):
        print("I am taking classes")
        
class Student(Person):
    pass
    
stu = Student("Jack")
stu.saySth()    
stu = Person("still Jack")
stu.saySth()