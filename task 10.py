a = int(input())
b = int(input())
c = int(input())

sum = a + b + c
min = min(a,b,c)
max = max(a,b,c)
print(min, sum-min-max, max)