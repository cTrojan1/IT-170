print("Data structure practice")

aSet = {1,2,3}

aDict = {"k1":10, "k2":20, "k3":30}
#Left side is the key name, the right side is the key (pair of values)

aList = [1,2,3]
#lists are most flexible data structures (mutable)

aTuple = (1,"2", [1,2,3])
#Can put strings, floats, booleans, etc (immutable)
#tup[0] = 2 (does not work because tuple is immutable
aTuple[2].append(4)
#this works because lists are mutable, even in an immutable type


#Tuple unpacking
print("TUPLE UNPACKING")
x,y,z = aTuple
print(x) #attached to value 1
print(y) #attached to value "2"
print(z) #attached to value [1,2,3,4]
print("UNPACKING CONT.")
x,y,(z, z1, z2, z3) = aTuple
print(z) #attached to value 1
print(z1) # attached to value 2 
print(z2, z3) #attached to values 3 & 4
print()
print("UNPACKING WITH ITERATION")
#Unpacking with iteration
seq = [(1,2,3), (4,5,6), (7,8,9)]
for a, b, c in seq:
    print("a={0}, b={1}, c={2}".format(a,b,c))
print()

aString = "Data"

a = aList[0]
print(a)
print(aList)
print(type(a))
print("")

iterator = iter(aSet)
for item in iterator:
    print(item)
