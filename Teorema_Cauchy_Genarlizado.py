import cmath
from os import error
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import sympy as sp
from sympy.core.power import Pow

"""
Teorema Generalizado de Cauchy

Alumno: Sánchez Verdiguel Isaac
Materia: Matemáticas Avanzadas para la Ingeniería

"""""


def opciones():
    print("Las opciones permitidas para f(z): ")
    print("\n1.- z^m \n2.- e^z \n3.- sen(z) \n4.- cos(z) \n5.- ln(z) \n6.- i \n7.- senh(h) \n8.- cosh(z) \n9.- z^m + e^z \n10.- Combinación")


# Derivada n-ésima

z = sp.symbols('z')


def der_z(f, n):
    if n == 1:
        return f
    else:
        return der_z(f, n-1).diff(z).replace(sp.Derivative, lambda *args: f)

# switch para la elección


def options(eleccion):
    if eleccion == 1:
        m = int(input("Elija la potencia para z: "))
        funcion = z**m
    elif eleccion == 2:
        funcion = cmath.e**z
    elif eleccion == 3:
        funcion = sp.sin(z)
    elif eleccion == 4:
        funcion = sp.cos(z)
    elif eleccion == 5:
        funcion = sp.ln(z)
    elif eleccion == 6:
        funcion = 0
    elif eleccion == 7:
        funcion = sp.sinh(z)
    elif eleccion == 8:
        funcion = sp.cosh(z)
    elif eleccion == 9:
        m = int(input("Elija la potencia para z: "))
        funcion = z**m + cmath.e**z
    elif eleccion == 10:
        return 10
    else:
        print("Error")
        funcion = 0
    return funcion

# Función para graficar circunferencia y puntos complejo


def graficar(z, r, centro):
    fix, ax = plt.subplots()
    ax.set_title('Circunferencia')
    ax.set_title('TEOREMA GENERALIZADO CAUCHY')
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    # Límites de los ejes
    if(centro.real > centro.imag):
        xymin = -(r + centro.real) - 1
        xymax = r + centro.real + 1
        ax.set_xlim(xymin, xymax)
        ax.set_ylim(xymin, xymax)
    else:
        xymin = -(r + centro.imag) - 1
        xymax = r + centro.imag + 1
        ax.set_xlim(xymin, xymax)
        ax.set_ylim(xymin, xymax)

    # Circulo
    circle = Circle(xy=(centro.real, centro.imag), radius=r, fill=False)
    ax.add_artist(circle)
    ax.text(centro.real, centro.imag+0.1,
            "Centro({},{}i)".format(centro.real, centro.imag))
    plt.plot(centro.real, centro.imag, marker="o", color="red")

    # Radio
    plt.arrow(centro.real, centro.imag, r, 0, width=0.03,
              length_includes_head=True, head_width=0.2, head_length=0.2)
    box = {'facecolor': 'none',
           'edgecolor': 'green',
           'boxstyle': 'round'
           }
    ax.text(centro.real+r/2, centro.imag-0.5, "R", bbox=box)

    # Punto complejo de la integral
    if(z.real == 0 and z.imag < 0):
        ax.text(z.real, abs(z.imag)+0.1,
                "Z({},{}i)".format(z.real, abs(z.imag)))
        plt.plot(z.real, abs(z.imag), marker="o", color="blue")
    else:
        ax.text(z.real, z.imag+0.1,
                "Z({},{}i)".format(z.real, z.imag))
        plt.plot(z.real, z.imag, marker="o", color="blue")

    ax.margins(tight=True)

    plt.tight_layout()
    ax.grid()
    plt.show()

    return


# Main
print("-----------------------------Teorema Generalizado de Cauchy -----------------------------------")
print("------------Z0------------")
zx = float(input("Introduzca la parte real de z0: "))
zy = float(input("Introduzca la parte imaginaria de z0: "))
if zx < 0 and zy == 0:
    zx = abs(zx)
elif zy < 0 and zx == 0:
    zy = abs(zy)

z0 = complex(zx, zy)


print("------------CIRCUNFERENCIA------------")
r = float(input("Introduzca el radio: "))
h = float(input("Introduzca h: "))
k = float(input("Introduzca ik: "))
centro = complex(h, k)

diferencia = z0 - centro
distancia = math.sqrt(math.pow(diferencia.real, 2) +
                      math.pow(diferencia.imag, 2))

if distancia > r:
    print("No cumple con el teorema.")
    print("La integral se indetermina.")
    resultado_integral = 0
else:
    print("\nCumple con el teorema, prosigue. :D")
    n = int(input("Ingrese la potencia del denominador: "))
    print("------------------------------\n")
    opciones()
    op = int(input("\nElija la opción para f(z): "))
    if op == 10:
        opciones()
        op1 = int(input("Elija la primera expresión a combinar: "))
        f1 = options(op1)
        op2 = int(input("Elija la segunda expresión a combinar: "))
        f2 = options(op2)
        f = f1 + f2
    else:
        f = options(op)

    if f == 0:
        resultado_integral = 0
    else:
        derivada = der_z(f, n)
        resultado_integral = sp.simplify(derivada.doit().subs(
            {z: z0}) * ((2 * math.pi * 1j)/math.factorial(n-1)))
        print("\n --------- Integral ----------------")
        print("    |         ", f)
        print("    |------------------------------------ dz")
        print("    |r      (z - ", z0, ")^", n)
        print("Funcion derivada n-1 veces = ", derivada)
        print("Resultado de la integral = ", resultado_integral)

graficar(z0, r, centro)
