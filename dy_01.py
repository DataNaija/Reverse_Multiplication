# Can you modify our multiplication table program in dy_0.py,
# so that we get a multiplication table from 10 to 1 instead of 1 to 10.

number = int(input("Enter a number: "))
i = 10

while i >= 1:
    product = number * i
    print(number, "x", i, "=", product)
    i = i - 1