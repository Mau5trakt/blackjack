# Nested list comprehension
matrix = [[j for j in range(5)] for i in range(3)]
 
print(matrix)

colores = ["a", "b", "c", "d"]

deck = [[j for j in colores]for i in range(1,15)]
print(deck, "\n")

deck2 = [[j for j in range (1,15)]for color in colores ]
print(deck2)