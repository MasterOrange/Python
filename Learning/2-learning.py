#!/usr/local/bin/python3.5

# Classes
# Lesson in classes 

class myClass:
        variable = 'bleh'

        def function(self):
                print('text inside the class')

myobject = myClass() # myobject holds an object of the class myClass

myobject.variable # access the variable created within myClass

#print(myobject.variable)
#
#myobject2 = myClass()
#
#myobject2.variable = 'other'
#
#print(myobject2.variable)

class Vehicle:
        name = ''
        kind = 'car'
        color = ''
        value = 100.00
        def description(self):
                desc_str = '%s is a %s %s worth $%.2f' % (self.name, self.color, \                self.kind, self.value)
                return desc_str

# Dictionaries

#object.items()

# del object[<entry>]
# object.pop(<entry>)

# modules are .py files

# from module import * imports all objects from the module

# sys.path.append("/foo") tell interpreter where to look for modules


