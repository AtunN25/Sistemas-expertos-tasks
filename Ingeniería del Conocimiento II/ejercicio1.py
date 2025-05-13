from logic import *

people = ["Gilderoy","Pomona","Minerva","Horace"]
houses = ["Gryffindor","Hufflepuff","Ravenclaw","Slytherin"]

symbols = []

for person in people:
    for house in houses:
        symbols.append(Symbol(f"{person}{house}"))

conocimiento = And()

for person in people:
    conocimiento.add(Or(
        Symbol(f"{person}Gryffindor"),
        Symbol(f"{person}Hufflepuff"),
        Symbol(f"{person}Ravenclaw"),
        Symbol(f"{person}Slytherin")
    ))

#solo una persona por casa   
for person in people:
    for h1 in houses:
        for h2 in houses:
            if h1 != h2 :
                conocimiento.add(
                    Implication(Symbol(f"{person}{h1}"),Not(Symbol(f"{person}{h2}")))
                )

conocimiento.add(
    Symbol("MinervaHufflepuff")
)

conocimiento.add(Or(
    Symbol("GilderoyHufflepuff"),
    Symbol("GilderoyRavenclaw")
))

conocimiento.add(
    Not(Symbol("PomonaGryffindor"))
)


for symbol in symbols:
    if model_check(conocimiento,symbol):
        print(f"{symbol}:VERDADERO")
    elif model_check(conocimiento,Not(symbol)):
        print(f"{symbol}:FALSO")
    else:
         print(f"{symbol}: QUIZAS")

