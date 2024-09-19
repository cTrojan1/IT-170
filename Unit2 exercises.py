#value check
xy = 5
s = "True-Expr" if xy > 0 else "False-Expr"
print(s)


print("")


#While loop repetition
spam = 0
while spam < 5:
    print("Hello, world.")
    spam = spam + 1

    
print("")


#for loop practice (list addition)
sum = 0
for item in [1, 3, 5]: 
    print(item) 
    sum = sum + item
print(sum)


print("")


#For loop max check
max = 0
for item in [1, 9, 7]: 
    if max < item:
        max = item
print(max)

    
print("")

#Range function practice (Start, Stop, Step) with odd numbers
for i in range(1, 15, 2):
    print(i)

print("")

#Range function practice (Start, Stop, Step) with even numbers
for i in range(0, 15, 2):
    print(i)
