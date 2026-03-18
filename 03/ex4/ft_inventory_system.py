import sys


def system_analysis(inventory: dict) -> None:
    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {sum(inventory.values())}")
    print(f"Unique item types: {len(inventory)}")
    print()
    print("=== Current Inventory ===")
    for item in inventory.items():
        percent = round((item[1] / sum(inventory.values()) * 100), 2)
        print(f"{item[0]}: {item[1]} units ({percent}%)")
    print()
    print("=== Inventory Statistics ===")
    max_value = 0
    max = None
    for item in inventory.items():
        if item[1] > max_value:
            max_value = item[1]
            max = item[0]
    print(f"Most abundant: {max} ({max_value} units)")
    min_value = max_value
    min = None
    for item in inventory.items():
        if item[1] < min_value:
            min_value = item[1]
            min = item[0]
    print(f"Least abundant: {min} ({min_value} units)")
    print()
    print("=== Item Categories ===")
    abondant = dict()
    moderate = dict()
    scarce = dict()
    for name, qty in inventory.items():
        if qty > 6:
            abondant.update({name: qty})
        elif qty < 4:
            scarce.update({name: qty})
        else:
            moderate.update({name: qty})
    if len(abondant) > 0:
        print(f"Abondant: {abondant}")
    if len(moderate) > 0:
        print(f"Moderate: {moderate}")
    if len(scarce) > 0:
        print(f"Scarse: {scarce}")
    print()
    print("=== Management Suggestions ===")
    restock = dict()
    for name, qty in inventory.items():
        if qty <= 1:
            restock.update({name: qty})
    if len(restock) == 0:
        print("No restock needed")
    else:
        print("Restock needed for:")
        for name in restock.keys():
            print(f" - {name}")
    print()
    print("=== Dictionary Properties Demo ===")


def parse_inventory(items: list) -> dict:
    inventory = dict()
    for item in items:
        item = item.split(":")
        try:
            item[1] = int(item[1])
        except ValueError:
            print(f"{item[1]} is not an int")
            return
        inventory.update({item[0]: item[1]})
    return inventory


def main():
    if len(sys.argv) <= 1:
        print("No argments passed")
        return
    else:
        system_analysis(parse_inventory(sys.argv[1:]))


if __name__ == "__main__":
    main()
