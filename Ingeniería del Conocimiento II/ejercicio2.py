from logic import *

colors = ["red","blue","green","yellow"]

symbols = []

for i in range(4):
    for color in colors:
        symbols.append(Symbol(f"{color}{i}"))

conocimiento = And()

for color in colors:
    conocimiento.add(
        Or(
            Symbol(f"{color}0"),
            Symbol(f"{color}1"),
            Symbol(f"{color}2"),
            Symbol(f"{color}3")
        )
    )

for color in colors:
    for i in range(4):
        for j in range(4):
            if i != j:
                conocimiento.add(
                    Implication(
                        Symbol(f"{color}{i}"),Not(Symbol(f"{color}{j}"))
                    )
                )

conocimiento.add(Or(
    And(Symbol("yellow0"),Symbol("red1"),Not(Symbol("blue2")),Not(Symbol("green3"))),
    And(Symbol("yellow0"),Symbol("blue2"),Not(Symbol("red1")),Not(Symbol("green3"))),
    And(Symbol("yellow0"),Symbol("green3"),Not(Symbol("red1")),Not(Symbol("blue2"))),
    And(Symbol("red1"),Symbol("blue2"),Not(Symbol("yellow0")),Not(Symbol("green3"))),
    And(Symbol("red1"),Symbol("green3"),Not(Symbol("yellow0")),Not(Symbol("blue2"))),
    And(Symbol("blue2"),Symbol("green3"),Not(Symbol("yellow0")),Not(Symbol("red1"))),
))

conocimiento.add(
    And(
        Not(Symbol("yellow0")),
        Not(Symbol("blue1")),
        Not(Symbol("red2")),
        Not(Symbol("green3"))
    )
)

for symbol in symbols:
    if model_check(conocimiento,symbol):
        print(symbol)
    


