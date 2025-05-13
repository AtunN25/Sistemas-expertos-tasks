from logic import *

mustard = Symbol("ColMustard");
scarlet = Symbol("MsScarlet")
kitchen = Symbol("kitchen")

knife = Symbol("knife");
wrench = Symbol("wrench")
plum = Symbol("plum")

ballroom = Symbol("ballroom");
library = Symbol("library")
revolver = Symbol("revolver")

simbolos = [mustard,scarlet,kitchen,knife,wrench,plum,ballroom,library,revolver]

conocimiento = And(Or(mustard,plum,scarlet),Or(ballroom,kitchen,library),Or(knife,revolver,wrench))

conocimiento.add(And(Not(scarlet),Not(ballroom),Not(knife)))

conocimiento.add(Or(Not(mustard),Not(library),Not(wrench)))

conocimiento.add(Not(plum))

conocimiento.add(Not(kitchen))


for simbolo in simbolos:
    if model_check(conocimiento,simbolo):
        print(f"{simbolo}:VERDADERO")
    elif model_check(conocimiento,Not(simbolo)):
        print(f"{simbolo}:FALSO")