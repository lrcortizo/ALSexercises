# lambdas

doble = lambda x: x * 2
factorial = lambda n: 1 if n <= 1 else \
                        n * factorial(n-1)

fibo = lambda n: [] if n < 1 else \
                    [0] if n == 1 else \
                    [0, 1] if n == 2 else \
                    fibo (n-1) + [fibo(n-1)[-1] + fibo(n-1)[-2]]

reverse =  lambda l: [] if l == [] or None else \
                        reverse(l[1:]) + [l[0]]
"""reverse =  lambda l: [] if l == [] or None else \
                        reverse(cdr(l)) + [car(l)]"""

car = lambda l: None if l  == [] or None else \
                    l[0]

cdr = lambda l: [] if l == [] or None else \
                    l[1:]

map = lambda f, l: [] if l == [] or None else \
                    [f(car(l))] + map(f, cdr(l))

filter = lambda f, l: [] if l == [] or None else \
                    [car(l)] + filter(f, cdr(l)) if f(car(l)) else \
                    filter(f, cdr(l))

reduce = lambda f, l: None if l == [] or None else \
                    car(l) if cdr(l) == [] else \
                    f(car(l), reduce(f, cdr(l)))

print("doble(4) = ", doble(4))
print("factorial(5) = ", factorial(5))
print("fibo(8) = ", fibo(8))
print("reverse([1, 2, 3, 5]) = ", reverse([1, 2, 3, 5]))
print("map(doble, range(4)) = ", map(lambda x: x*2, [1,2,3]))
print("filter(espar, range(7)) = ", filter(lambda x: x%2 == 0, [1,2,3,4,5,6]))
print("reduce(suma, range(6)) = ", reduce(lambda x, y: x + y, [1,2,3,4,5]))


