from logic import *

people = ["Golderoy","Pomona","Minerva","Horace"]
houses = ["Gryffindor","Hufflepuff","Ravenclaw","Slytherin"]

symbols = []

for person in people:
    for house in houses:
        symbols.append(Symbol(f"{person}{house}"))

print(symbols)

knowledge = And()

for person in people:
    knowledge.add(Or(
        Symbol(f"{person}Gryffindor"),
        Symbol(f"{person}Hufflepuff"),
        Symbol(f"{person}Ravenclaw"),
        Symbol(f"{person}Slytherin"),
    )
    )

for person in people:
    for h1 in houses:
        for h2 in houses:
            if h2 != h2:
                knowledge.add(
                    Implication(Symbol(f"{person}{h1}"),Not(Symbol(f"{person}{h2}")))
                )

