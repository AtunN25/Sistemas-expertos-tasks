from logic import *

people = ["Golderoy","Pomona","Minerva","Horace"]
houses = ["Gryffindor","Hufflepuff","Ravenclaw","Slytherin"]

symbols = []

for person in people:
    for house in houses:
        symbols.append(Symbol(f"{person}{house}"))

#print(symbols)

conocimiento = And()

conocimiento.add(Or(Symbol("GilderoyGryffindor"),Symbol("GilderoyRavenclaw")))

conocimiento.add(Not(Symbol("PomonaSlytherin")))

conocimiento.add(Symbol("MinervaGryffindor"))

for symbol in symbols:
    if model_check(conocimiento,symbol):
        print(symbol)

                 