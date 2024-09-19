list1 = [1, 3, 5]
list2 = [8, 4, 2]

max = 0
min = 100
sum = 0

for i in list1:
    if max < i:
        max = i
print(max)

for x in list2:
    if min > x:
        min = x
print(min)

sum = min + max

print(sum)
