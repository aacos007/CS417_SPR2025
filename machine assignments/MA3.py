import math
#h = 1/2, 1/4, 1/8, ... 1/2^30
#h 2^-n...while n < 31...

n = 30
h = 2^-n

#hardcoded input values & functions; f(x) & x 
x = 1
#renaming f(x) as function
f = math.sin(x)

approx_func = (math.sin(x + h) - math.sin(x))/h
known_func = math.cos(1) #aka cos(1)
abs_error = approx_func - known_func / known_func


# sample output
#|  h   |       x       | Approx. f'(x) |  Known f'(x)  |  Abs. Error   |
#|:----:|--------------:|--------------:|--------------:|--------------:|
#|2^-01 |    1.00000000 |    0.31204800 |    0.54030231 |    0.22825430 |
#|2^-02 |    1.00000000 |    0.43005454 |    0.54030231 |    0.11024777 |
#|2^-03 |    1.00000000 |    0.48637287 |    0.54030231 |    0.05392943 |
#|2^-04 |    1.00000000 |    0.51366321 |    0.54030231 |    0.02663910 |


print("|    h    |    x    |       approx f'(x)       |      known f'(x)      |        abs. error       |")
print("|---------|---------|--------------------------|-----------------------|-------------------------|")
#while n < 31:
for i in range(1, n-1):
    print("|  2^-" + str(n) +"  |    " + str(x) + "    |    " + str(approx_func) + "  |   " + str(known_func) + "  |    " + str(abs_error) + "  |")
    #print("|  h  |    x    |    approx f'(x)    |    known f'(x)    |    abs. error    |")

