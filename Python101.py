__author__ = 'pramasamy'

print '************************ 4 - Modules & Functions ***************************'

# Usage:    module.function

def mod1():
    import math  # module
    # var = input("Enter a sq root value: ")    # Use this to get raw input
    var = 9
    sq = math.sqrt(var)  # module.function
    print "Using str fn " + str(var) + " is :" + str(sq)        # str(var) - type conversion
    print "Using repr() " + repr(var) + " is :" + str(sq)       # repr function
    print "Using backticks `` " + `var` + " is :" + str(sq)     # replacing str(var) with backticks ``

mod1()

print '************************ 6 - Strings ************************************'

print "Paddu said,\"Holy Cow\" and walked away" # Escape character '\' - fwd slash

a = 'Paddu '
b = 'Priya '
c = 'Maaran'
d = 23

print a + b + c     # Joining strings
print a*10          # String Multi  :   Multiplying/Repeating 10 times
print [2]*10        # Int Multi     :   Int 2 multiplied 10 times. 2 enclosed by []

print '************************ 9 - Sequences & Lists ************************************'

family = ['paddu', 'priya', 'maaran', 'bubbles']    # Index is 0,1,2,3 ..
print family[2]
print family[-3]        # starts from -1, -2, -3 from end of list
family.append('coco')
family.pop(3)
family.extend('ira')    # adds i r a as sep letters to the end of list
family.remove('paddu')  # removes an element by name
del family[0]           # removes by index
family.sort()           # sorts the list in place

family2 = ['str', 'tam', 'ananth', 'bhu', 'sham', 'hamsh']

print family.__add__(family2)
print family
print family.index('i') # prints the position of 'i'
family.reverse()
print family.__len__()  # counts number of elements
print len(family)
print max(family), min(family)
print list('Maaran')    # converts any string to list
print sorted('maaran')    # converts to a list and sorts it in place
print sorted(family)
print family
print 'sham' in family  # to check if an element exists in list
family[0] = 'Raa'       # replacing an element
print family
del family[0]
family[0]
print family

# TODO: Check other list functions

print '************************ 10 - Slicing ************************************'

ex_slice = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print ex_slice[2:5]
print ex_slice[:5]
print ex_slice[5:]
print ex_slice[-2]
print ex_slice[:]                   # Print entire list
print ex_slice[1:9:3]               # Start @ 1 : End @ 9 : Inc by 3
print ex_slice[10:0:-2]
print [11, 22, 33] + [44, 55, 66]   # concat lists
print ex_slice[-5:]
print ex_slice[:5]
print ex_slice[:]
print ex_slice[::2]
print 'Maaran '*10

print '************************ 16 - Tuples ************************************'

ex_tuple = (4, 1, 7, 9)
print ex_tuple
print ex_tuple.__len__()

print '************************ 17 - Strings & stuff ************************************'

message = 'Hey %s Hows your %s'
var = ('Paddu', 'Bike')
print message % var

varb = ('Paddu', 'Work')
print message % varb

message = 'Hey %s Hows your %i'     # Mixing string and integer
varc = ('paddu', 5)
print message % varc

message = 'Hey Paddu Hows your Bike'
print message.find('Bike')      # finds the index value of 'B' in Bike
print message.replace('Bike', 'Cycle')

message = ['Hey', 'Paddu', 'Hows', 'your', 'Bike']
sep = '|'
print sep.join(message)         # joins every element by sep

print '************************ 19 - Dictionary ************************************'

dictex = {'Dad':'Paddu', 'Mom':'Priya', 'Baby': 'Maaran'}

print dictex
print dictex['Baby']        # dictionary of key prints value

dictex2 = dictex.copy()
print dictex2

print dictex.has_key('Baby')    # checking for a key in dict

print '************************ 20 - If statement ************************************'

Bike = 'Harley'
Model = 48
if Bike == 'Ducati':
    print "Ducati"
elif Bike == 'Honda':
    print "Its Honda"

elif Bike == 'Harley':
    if Model == 48:             # Nesting if statement
        print "Its HD 48!"
elif Bike == 'Harley' and Model == 48:  # using and condition - err!
        print "Its HD 2!"
else:
    print "Unknown"

print '************************ 25 - while & for statement ************************************'

b = 1
while b <= 10:
    print b
    b += 1

family = ['paddu', 'priya', 'maaran', 'bubbles']            # looping a list
for i in family:
    print "Hello: " + i

dictex = {'Dad':'Paddu', 'Mom':'Priya', 'Baby': 'Maaran'}   # looping a dict
for i in dictex:
    print i, dictex[i]

'''
while 1:
    var = raw_input("Enter name: ")                         # infinite loop
    if var == 'q':
        break
'''

print '************************ 27 - Functions & Parameters ************************************'

# Super Imp!!

def fn(x='Maaran', y=10):                   # default value Maaran stored
    print "Hey " + x + str(y)
fn('paddu')
fn(y=20)                                    # prints Maaran(default) and 20


def fn2(name, *ages):                       # passing multi values
    print name
    print ages

# passing multi values to * converts into a tuple
fn2('paddu', 20, 21, 22, 23)    # prints a TUPLE (20, 21, 22, 23) - Imp!

def fn3(**items):
    print items                 # prints dict instead of tuple {'Dad': 'paddu', 'Baby': 1, 'Mom': 35}

fn3(dad='paddu', mom=35, baby=1)

def profile(first, last, *ages, **items):
    print first, last
    print ages      # returns tuple
    print items     # returns dict

profile('paddu', 'rams', 20, 30, 30, 50, mom=35, baby=1)  # mixing everything

a = (20, 30, 30, 50)
dict = {'mom': 35, 'baby': 1}

profile('paddu', 'rams', *a, **dict)  # passing tuple and dict as parameters

print '************************ 32 - OOP ************************************'

'''
a) Object has data & methods
b) Objects as built-in attributes which desc it (Ex - obj.attributes - maaran.cute)
c) Objects also has methods/fns that u can call (Ex - obj.action() - maaran.runs(), maaran.cries())
d) We need a class before we define objects
e) Class is like a blue print for your objects. Your obj is based on the class
'''

class ex:
    eyes='blue'     # these are attributes
    age=22          # attributes
    def d(self):
        print 'Inside method!'

print ex            # creates class in memory
obj = ex()          # creates objects
obj.d()             # calls method

class c:
    def m(self, name):
        print name
        self.name = name    # self.name = obj.name. 'self' is a placeholder for obj

    def m1(self):
        print self.name

obj1 = c()
obj2 = c()
obj1.m('paddu')
obj1.m1()
obj2.m('priya')

print '************************ 34 - Sub & SuperClass ************************************'

class parent1:
    var1 = "I'm var1"
    var2 = "I'm var2"

class parent2:
    var3 = "I'm parent2"

class child(parent1, parent2):
    var1 = 'var1 updated in child'  # overwriting value in child

cobj = child()
pobj = parent1()

print cobj.var1
print cobj.var2
print pobj.var1
print cobj.var3

print '************************ 37 - Constructors ************************************'

class a:
    def __init__(self):
        print "Constructor!"

obj = a()       # prints when obj is created. No explicit calling needed

print '************************ 38 - Import,Reload, Modules info ************************************'

'''
a) create a function and store it under python2.6 as .py file   - check this location for mac
b) from your program 'import sampleimport.py'
c) u can access the method by sampleimport.<method_name>
d) from your idle, you can reload modules by reload(sampleimport)
e) your idle wont show updates to sampleimport unless you reload it
f) Import <mod_name>, mod_name.func(), dir(mod_name) - this shows all the methods inside a mod
g) mod_name.__doc__ - mod documentation

'''

print '************************ 41 - working with files ************************************'

''' writing to a file
fobj = open('/Users/pramasamy/sample', 'w')
fobj.write('Hi Paddu')
fobj.close()
'''

fobj = open('/Users/pramasamy/sample', 'r')
# print fobj.read(2)             # reads 10 bytes
# print fobj.read()               # reads rest of the file
# print fobj.readline()
newlist = fobj.readlines()           # reads rest of the lines and stores as a list
print newlist
newlist[0] = 'Hi Maaran\n'
print newlist
fobj = open('/Users/pramasamy/sample', 'w')
fobj.writelines(newlist)
fobj.close()

# loop reading a file
fobj = open('/Users/pramasamy/sample', 'r')
for line in fobj.readlines():
    print "lineloop: " + line