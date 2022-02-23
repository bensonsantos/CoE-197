print("hello world")
import random 

x = [random.randint(0,100) for i in range(10)]
print(x)
print("Min", min(x))
print("Max", max(x))
print("Sum", sum(x))
x.sort()
print("Sorted",x)

y =  [random.random()*100 for i in range(10)]
print(y)
y = [int(i) for i in y]
print(y)

b = "deep learning is fun"
print(b)
print(b[5:])
print(b + "!")
print(b.replace("deep","machine"))
print("learn" in b)
print(b.upper())

l = [1, 2, "hello", 3, 4, [5, 1.4, "dog"]]
print(l)
print(l[2])
m = [i for i in range(10)]
n = [i for i in range(100,110)]
print(m)
print(n)
print(m + n)
m.insert(0,-1)
print(m)

k = [i for i in range(10)]
k.append(10)
print(k)

t = [i for i in range(10)]
print(t[0:3:1])
print(t[1::])
print(t[::2])
print(t[::-1])

j = {random.randint(-10,10) for i in range(10)}
print(j)

def square_list(x):
    return[i**2 for i in x]

j = square_list(j)
print(j)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

p = Person("benson", 6)
print(p)
print(p.get_age())
print(p.get_name())

