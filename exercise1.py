g = ""
p = ""
d = ""
shipping_cost = 0
weight = int(input("Enter the weight of your package: "))
shipping_method = input("Choose the method for shipping, g for ground shipping, p for premium shipping, d for drone shipping: ").lower()
print(shipping_method)
if shipping_method == "g":
  if weight <= 2:
    shipping_cost = weight*1.50 + 20.00
  elif 2 < weight <= 6:
    shipping_cost = weight*3.00 + 20.00
  elif 6 < weight <= 10:
    shipping_cost = weight*4.00 + 20.00
  elif 10 < weight:
    shipping_cost = weight*4.75 + 20.00
elif shipping_method == "p":
  shipping_cost = 125.00
elif shipping_method == "d":
  if weight <= 2:
    shipping_cost = weight*4.50
  elif 2 < weight <= 6:
    shipping_cost = weight*9.00
  elif 6 < weight <= 10:
    shipping_cost = weight*12.00
  elif 10 < weight:
    shipping_cost = weight*14.25
else:
  print("You chose poorly! Enter g, p or d.")

print(f" The cost of shipping your package is: {shipping_cost} $")

