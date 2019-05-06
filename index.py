def polinomio(x):
    return x ** 2 + 5 + 10
print(polinomio(10))

print((lambda x: x ** 2 + 5 + 10)(10))

print((lambda x,y: (x*y)/100)(10,5))

def app(func, min, max):
    return func(min, max)

def mult(min, max):
    return (lambda min, max: min*max)(min, max)

print (app(mult, 10, 100))

#maps
def add_five(x):
    return x*10

def operations():
    fechaNacimiento=[1970, 1971, 2007, 1994, 197]
    appMap=list(map(add_five, fechaNacimiento))
    print(appMap)

operations()

def opera():
    edad=[47,46,25,24,20,11]
    fechaNaci=[1970, 1971, 2007, 1994, 197]

    result1 = list(map(lambda x: x*10, edad))
    result2 = list(map(lambda y: y + 100, fechaNaci))
    print(result1)
    print(result2)

opera()

#filter
edad=[47,46,25,24,20,11]
res=list(filter(lambda x: x < 30, edad))
print(res)

#Generator
def countdown():
    i=5
    while i > 0:
        yield i
        i -= 1

for i in countdown():
    print(i)

def number(x):
    for i in range(x):
        if i%2 == 0:
            yield i
    
print(list(number(11)))