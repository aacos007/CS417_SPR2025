import math
#h = 1/2, 1/4, 1/8, ... 1/2^30
#h 2^-n...while n < 31...

n = 32

#hardcoded input values & functions; f(x) & x 
x = 1
#renaming f(x) as function
f = math.sin(x)


known_func = math.cos(1) #aka cos(1)


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
    h = pow(2, -i)
    approx_func = (math.sin(x + h) - f)/h
    abs_error = abs(approx_func - known_func)
    print("|" + ("2^-" + str(i)).center(9) + "|" + str(x).center(9) + "|" + str(approx_func).center(26) + "|" + str(known_func).center(23) + "|" + str(abs_error).center(24) + "|") 
    #print("|  h  |    x    |    approx f'(x)    |    known f'(x)    |    abs. error    |")
    
print("\n")

#Precision Estimation Pseudocode
#let a ← 4.0 / 3.0
#let b ← a - 1
#let c ← b + b + b
#return |1 - c|

a = 4.0 / 3.0
b = a - 1
c = b + b + b
estimated_precision = abs(1 - c)
print("Estimated Precision (esp): " + str(estimated_precision))
#approximated eps using the Cleve Moler Algorithm

print("Root of Estimated Precision (\u221Aesp): " + str(math.sqrt(estimated_precision)))
#approximated (eps)^1/2



print("\n")

print("After examining the graph, the minimum value for the magnitude of the error is 5.455107476848298e-10 at h = 2^-27 and 2^-28")
print("\n")
print("This is only about 3.67% of the square root of estimated precision (\u221Aesp). This means that we have a good approximation and that our calculation is accurate.")