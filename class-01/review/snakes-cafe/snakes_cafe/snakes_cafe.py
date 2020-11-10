# **************************************
# **    Welcome to the Snakes Cafe!   **
# **    Please see our menu below.    **
# **
# ** To quit at any time, type "quit" **
# **************************************

# Appetizers
# ----------
# Wings
# Cookies
# Spring Rolls

# Entrees
# -------
# Salmon
# Steak
# Meat Tornado
# A Literal Garden

# Desserts
# --------
# Ice Cream
# Cake
# Pie

# Drinks
# ------
# Coffee
# Tea
# Unicorn Tears

# ***********************************
# ** What would you like to order? **
# ***********************************
# >

width = 39

def print_star_line():
    print("*" * width)

def print_bordered_text(txt):
    print(f"**{txt.center(width - 4)}**")


def print_section(section_key):
    print(section_key)
    print("-" * len(section_key))

    # print out items
    items = menu[section_key]

    for item in items:
        print(item)

    print("")

menu = {
    "Appetizers": ["Wings", "Cookies", "Spring Rolls"],
    "Entrees": [
        "Salmon",
        "Steak",
        "Meat Tornado",
        "A Literal Garden",
    ],
    "Desserts": [
        "Ice Cream",
        "Cake",
        "Pie",
    ],
    "Drinks": ["Coffee", "Tea", "Unicorn Tears"],
}

def print_sections():
    for section_key in menu:
        print_section(section_key)


def print_star_box(lines):
    print_star_line()
    for line in lines:
        print_bordered_text(line)
    print_star_line()

def prompt_order():
    print_star_box(["What would you like to order?"])


def take_order():
    while True:
        order = input("> ")

        if order == "quit":
            break

        if order in orders:
            orders[order] += 1
        else:
            orders[order] = 1

        amount = orders[order]

        print_bordered_text(f"{amount} orders of {order} have been ordered.")




orders = {}

print_star_line()
print_bordered_text("Welcome to the Snakes Cafe!")
print_bordered_text("Please see our menu below.")
print_bordered_text("")
print_bordered_text("To quit at any time, type \"quit\"")
print_star_line()


print_sections()

prompt_order()

take_order()




