inventory = [
    # name,       category,   unit_price, units_sold, units_left
    ["Strawberry", "Fruit",      3.50,        40,          10],
    ["Broccoli",   "Vegetable",  2.20,        25,           8],
    ["Cheddar",    "Dairy",      5.00,        18,           4],
    ["Baguette",   "Bakery",     2.80,        35,           2],
    ["Blueberry",  "Fruit",      4.00,        22,           6],
    ["Spinach",    "Vegetable",  1.80,        30,          12],
    ["Yogurt",     "Dairy",      1.20,        50,          15],
    ["Croissant",  "Bakery",     3.00,        28,           3],
]

#-------------------------------------------------------------------------------------------------------------------

total_revenue = 0
for name, category, unit_price, units_sold, units_left in inventory:
    total_revenue += unit_price * units_sold

print("Total Revenue:", total_revenue)                     # Total Revenue: 669.0

# --------------------------------------------------------------------------------------------------------------------

for name, category, unit_price, units_sold, units_left in inventory:
    if units_left < 5:     
       print(name)

# Cheddar
# Baguette
# Croissant

#---------------------------------------------------------------------------------------------------------------------
fruit = 0
vegetable = 0
dairy = 0
bakery = 0

for name, category, unit_price, units_sold, units_left in inventory:
    revenue =  unit_price * units_sold
    if category == "Fruit":
        fruit = fruit + revenue
    if category == "Vegetable":
        vegetable = vegetable + revenue
    if category == "Dairy":
        dairy = dairy + revenue
    if category == "Bakery":
        bakery = bakery + revenue

print("Fruit Revenue:", fruit)                                # Fruit Revenue: 228.0
print("Vegetable Revenue:", vegetable)                        # Vegetable Revenue: 109.0
print("Dairy Revenue:", dairy)                                # Dairy Revenue: 150.0
print("Bakery Revenue:", bakery)                              # Bakery Revenue: 182.0



