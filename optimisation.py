import pulp

model = pulp.LpProblem("Maximize Profit", pulp.LpMaximize)

lemonade = pulp.LpVariable('lemonade', lowBound=0, cat='Integer')  # Кількість продукту А
juice = pulp.LpVariable('juice', lowBound=0, cat='Integer')  # Кількість продукту Б

model += lemonade + juice, "Profit"

model += 2 * lemonade + 1 * juice <= 100  # water
model += 1 * lemonade + 0 * juice <= 50  # sugar
model += 1 * lemonade + 0 * juice <= 30  # Lemon juice
model += 0 * lemonade + 2 * juice <= 40  # Fruit puree

model.solve()

print("Виробляти продуктів Лимонад:", lemonade.varValue)
print("Виробляти продуктів Фруктовий сік:", juice.varValue)
