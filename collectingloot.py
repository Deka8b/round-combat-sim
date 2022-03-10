def add_to_inv(where: list, to: dict):
    for item in where:
        to.setdefault(item, 0)
        to[item] = to[item] + 1
    return to


eq = {"gold coins": 58, "arrows": 120, "silver coins": 12, "dagger": 2, "boots": 4}

# print(f"eq before: {eq}")
def item_counter(eq: dict):
    items_total = 0
    for item, count in eq.items():
        print(f"{item}: {count}")
    for total in eq.values():
        items_total += total
    return f"All items: {items_total}"

#killed dragon
dragon_loot = ["gold coins", "small sapphire", "gold coins",
               "dragons tongue", "dragons scales", "gold coins", "dragons claws"]

#collect loot
# add_to_inv(dragon_loot, eq)
# print(item_counter(eq))