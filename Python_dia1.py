#PROBLEMA DE PYTHON ONLINE
def make_day_string(day):
    x = int(day)
    a = "it is day " + str(x) + " of the month"
    if (a == "it is day " + str(x) + " of the month"):
        return a
    return


# un comentario
# una variable (u objeto) ess un nombre o referencia a un valor guardado en memoria
a = 3
b = 1000
c = 30.4
z = sum((a,b,c))
print(z)# los comentarios no son ejecutados por el interprete de Python
print(a) # si no se coloca el simbolo a, saldrá un error

# Reglas para los nombres de las variables
# Pueden tener cualquier logitud
# El primer caracter debe ser una letra o el guion bajo, no puede set un número
# Los caracteres siguientes pueden ser números. Por ejemplo: altura1, altura_1, altura1
# No pueden existir espacios en medio, por ejemplo: peso promedio
# hay diferencia entre mayusculas y minusculas, es case sensitive, Arbol y arbol son diferentes 
# Se sugiere no utilizar palabras clave o usadas por Python: int, float, print, etc...

# funcion es un bloque de código


import keyword
keyword.kwlist # para verificar todas las palabras clave

# tipos de datos

# escalares:
#Enteros
#flotantes
#complejos
#Lógicos(Booleanos)

#Secuencias:
#String
#Listas
#Tuplas
#Conjuntos
#Diccionarios


# Numeros enteros
a = 56 # número en base 10
b = 0b1000000 # número en base 2
c = 0o33523 # numero en base 0
d = 0x23AF5B # numero en base 16
i = 1_000_000_000 # se puede usar un guion bajo para mejorar la legibilidad de numeros grandes


# números flotantes

e = 1.2
E = 7.43e4 # 7.43 por 10 elevado a la 4
print(E)
f = 1.3e-3

# números complejos

g = 7 +3j
print(g)
print(type(g))
print((1+2j).real)# numero real
print((1+2j).imag)# número imaginario


# SEMANA 2 PYTHON

print(0.1+0.1+0.1)# acá hay un error de precision debida a la representacion de los valores en coma flotantes
print(1000000 + 0.00000000001)# esta 

print(int(2.32)) # int nos trunca el numero
print(float (2.32)) 
print(_)# el _ guarda el último valor
print(type(_))

print(bin(17)) # Expresamos el número 17, de base decimal en base binaria
print(bin(128))
print(oct(529)) #Pasamos 529 de base 10 a base 8
print(oct(-529))
print(hex(2569)) #Pasamos 2569 de base 10 a 16
print(hex(25))
print(hex(0b01100001110))# pasamos un numero binario de base 2 a base 16
print(int('11110000',base = 2)) # pasamos de binario a decimal

#PRINT

print("Twinlem, twinkle, litte star, \n\thow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamon in the sky. \nTwinle, littele star, \n\t How I wonder what you are!")
# \n es un salto de linea
# \t es un tabulador

#COMO MIRAR QUE VERSION TENGO DE PYTHON
import sys
print("Python version")
print(sys.version)
print("Version information: ")
print(sys.version_info)

#OBTENER FECHA Y HORA ACTUAL
import datetime
now = datetime.datetime.now()
print(now)
print("Current date and time:")
print(now.strftime("%Y-%m-%d %H:%M:%S"))

# ESCRIBIR UN PROGRAMA EN PYTHON QUE ACEPTE EL RADIO DE UN CIRCILO Y CALCULE SU AREA

from math import pi
radio = float(input("Input the radius of the circle: "))
print("The area of the circle with radius " + str(radio) + "is: " + str(pi * radio ** 2))

# ESCRIBIR UN PROGRAMA QUE PIDA LA BASE Y LA ALTURA DE UN TRIANGULO, Y CALCULE SU AREA

print("VALOR DEL AREA DEL TRIANGULO")
base = int(input("Escribe el valor de la base: "))
altura = int("Escribe el valor de la altura: ")
print("El valor del triangulo es: ", (base * altura)/2)

# FORMA DE YOUTUBE

#split() se refiere a "b" y "h" para separar los valores// si colocaras split(",") separa los valores por comas
b, h = input("Ingresa el valor de la base y la altura del triangulo: ").split()
b = float(b)
h = float(h)
A = b*h/2
print(f"El area del triangulo es {A}")

# Nombre Y Apellido en order inverso

fname = input("Input your First Name: ")
fname2 = input("Input your Second Name: ")
lname = input("Input your Last Name: ")
lname2 = input("Input your last second name: ")
print("Hola,",lname2,lname,fname,fname, "¿Cómo estás?")

name = input("Input your name: ")
age = int(input("Input su edad: "))
year = 100-age+2022
print(name + f', usted cumplira 100 años en el año {year}')

# LISTA Y TUPLAS

#EScribe un progra

values = input("Input some comma separeted numbers: ")
print(values)
list = values.split(",")
tuple = tuple (list)
print('List: ' ,list)
print('tuple', tuple)