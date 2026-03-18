import sys


def total_items(inventory: dict[str, int]) -> int:
    total = 0
    for quantity in inventory.values():
        total += quantity
    return total


def parse_inventory(items: list[str]) -> dict[str, int] | None:
    inventory: dict[str, int] = dict()

    for item in items:
        parts = item.split(":")
        if len(parts) != 2 or not parts[0] or not parts[1]:
            print(f"Invalid inventory entry: {item}")
            return None

        try:
            quantity = int(parts[1])
        except ValueError:
            print(f"Invalid quantity for {parts[0]}: {parts[1]}")
            return None

        inventory.update({parts[0]: quantity})

    return inventory


def system_analysis(inventory: dict[str, int]) -> None:
    total_quantity = total_items(inventory)
    most_abundant_name = ""
    most_abundant_value = -1
    least_abundant_name = ""
    least_abundant_value = -1
    abundant = dict()
    moderate = dict()
    scarce = dict()
    restock = []

    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {total_quantity}")
    print(f"Unique item types: {len(inventory)}")
    print()

    print("=== Current Inventory ===")
    for name, quantity in inventory.items():
        percentage = (quantity * 100) / total_quantity
        unit_label = "unit" if quantity == 1 else "units"
        print(f"{name}: {quantity} {unit_label} ({percentage:.1f}%)")

        if quantity > most_abundant_value:
            most_abundant_name = name
            most_abundant_value = quantity

        if least_abundant_value == -1 or quantity < least_abundant_value:
            least_abundant_name = name
            least_abundant_value = quantity

        if quantity > 5:
            abundant.update({name: quantity})
        elif quantity < 4:
            scarce.update({name: quantity})
        else:
            moderate.update({name: quantity})

        if quantity <= 1:
            restock.append(name)
    print()

    print("=== Inventory Statistics ===")
    print(
        f"Most abundant: {most_abundant_name} "
        f"({most_abundant_value} units)"
    )
    least_unit_label = "unit" if least_abundant_value == 1 else "units"
    print(
        f"Least abundant: {least_abundant_name} "
        f"({least_abundant_value} {least_unit_label})"
    )
    print()

    print("=== Item Categories ===")
    if abundant:
        print(f"Abundant: {abundant}")
    if moderate:
        print(f"Moderate: {moderate}")
    if scarce:
        print(f"Scarce: {scarce}")
    print()

    print("=== Management Suggestions ===")
    if restock:
        print(f"Restock needed: {', '.join(restock)}")
    else:
        print("No restock needed")
    print()

    print("=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {', '.join(inventory.keys())}")
    values_text = []
    for value in inventory.values():
        values_text.append(str(value))
    print(f"Dictionary values: {', '.join(values_text)}")
    print(
        "Sample lookup - 'sword' in inventory: "
        f"{inventory.get('sword') is not None}"
    )


def main() -> None:
    if len(sys.argv) <= 1:
        print(
            "No inventory provided. Usage: "
            "python3 ft_inventory_system.py item:quantity ..."
        )
        return

    inventory = parse_inventory(sys.argv[1:])
    if inventory is None:
        return

    system_analysis(inventory)


if __name__ == "__main__":
    main()
