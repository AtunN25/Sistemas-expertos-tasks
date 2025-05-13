from logic import *

P = Symbol("P")
Q = Symbol("Q")
R = Symbol("R")

Symbols = [P,Q,R]

# Ejercicio 1

KB_1 = Implication(And(P,Not(Q)),R)
print("Resultado 01:",model_check(KB_1,R))

A = Symbol("A")
B = Symbol("B")
C = Symbol("C")

Symbols = [A,B,C]

# Ejercicio 2

KB_2 = And(Or(A,C),Or(B,Not(C)))
print("Resultado 02:",model_check(KB_2,Or(A,B)))

# Ejercicio 3

KB_3 = And(Implication(Not(P),Q),Or(Q,R),Not(And(Q,R)),R)
print("Resultado 03:",model_check(KB_3,Not(Q)))




