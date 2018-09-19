y= [4, 15, 24, 56]
print "El primero es", y[0], "ultimo", y[3]

print range (7)

for i in range(5):
    print "Hola"
    print "Vera"
print "Hasta luego"

y.append("Bye")
print y

def funcion(x):
    return 1.01*x

x=[100]
for i in range(50):
    x.append(1.01*x[i])
print x

def iteracion(inicial,iteracion,funcion):
    x=[inicial]
    for i in range(iteracion):
        x.append(funcion(x[i]))
    return x
iteracion(50,10,funcion)

import math
valores = iteracion(5,10,math.cos)
print valores

import matplotlib.pyplot as plt
plt.plot(valores)
plt.show(valores)

def suma(x,y):
    return x+y

suma(2,3)

def producto(x,y):
    return x*y

producto(2,3)

def operacion(x,y,f):
    return f(x,y)

operacion(2,3,suma)

import numpy as np

def diagrama(f,x0,it):
    x = [x0]
    y = [x0]
    s = np.arange(0, 1, 0.01)
    for i in range(it):
        x.append(x[2*i])
        x.append(f(x[2*i]))
        y.append(f(y[2*i]))
        y.append(f(y[2*i]))
    plt.plot(x, y, color='red')
    plt.plot(s, f(s))
    plt.plot(s, s, color='black')
    plt.show()

def logistica(x):
    return 4*x*(1-x)

diagrama(logistica, 0.1, 15000)
