print("HI THERE","HOW ARE YOU?")


# response = input("> ")

# print(f"You said \"{response}\"")

orders = {
    "Root Beer" : 1,
}

# print(orders["Root Beer"])

response = input("> ")

orders[response] = f"you ordered {response}"

print(orders)

