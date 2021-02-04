from abc import ABC,abstractmethod

#Creating abstract Person class that has get_gender abstract method
class Person(ABC):
    #creating abstract method
    @abstractmethod
    def get_gender(self):
        pass

#Below are two classes that inherit the Person class and implementing get_gender() method
class Male(Person):
    def get_gender(self):
        print("Male")

class Female(Person):
    def get_gender(self):
        print("Female")

try:
    #creating objects of Male and Female Class and calling get_gender method
    objmale = Male()
    objfemale = Female()
    objmale.get_gender()
    objfemale.get_gender()
except Exception as e:
    print(e)

#now throwing error for Person class by creating instance of Person class
try:
    objperson = Person()
except Exception as e:
    print(e)