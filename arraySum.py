a = [1,6,5,2,3]
i = 0
print(len(a))
j = len(a) - 1
my_sum = 8
finded_numbers = ()
iterations = 0
OK=True
while(OK):
    iterations += 1
    if (i < j):
        i += 1
    if (i == j):
        if (i == 0):
            OK = False
            break
        i = 0
        j -= 1
    if (a[i] + a[j] == my_sum):
        finded_numbers = (a[i], a[j])
        OK = False
print (finded_numbers)
print (iterations)