def add_to_inv(where: list, to: dict):
    for item in where:
        to.setdefault(item, 0)
        to[item] = to[item] + 1
    return to


def item_counter(eq: dict):
    items_total = 0
    for item, count in eq.items():
        print(f"{item}: {count}")
    for total in eq.values():
        items_total += total
    return f"All items: {items_total}"

