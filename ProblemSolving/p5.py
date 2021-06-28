
numbers = [int(n) for n in input().split()]
numbers.sort()

max_odd = 0
odd_mul = 1
even_mul = 1
for n in numbers:
    if n % 2 == 1:
        if max_odd < n: max_odd = n
        odd_mul *= n
    else:
        even_mul *= n

if odd_mul > 1: print(odd_mul)
elif max_odd > 0 : print(max_odd)
else: print(even_mul)
