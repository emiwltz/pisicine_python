import sys


def parse_inventory(parameters: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}

    for parameter in parameters:
        parts = parameter.split(":")
        if len(parts) != 2 or parts[0] == "" or parts[1] == "":
            print(f"Error - invalid parameter '{parameter}'")
            continue

        item_name = parts[0]
        if item_name in inventory:
            print(f"Redundant item '{item_name}' - discarding")
            continue

        try:
            quantity = int(parts[1])
        except ValueError as error:
            print(f"Quantity error for '{item_name}': {error}")
            continue

        inventory.update({item_name: quantity})
    return inventory


def get_most_abundant_item(inventory: dict[str, int]) -> str:
    item_list = list(inventory.keys())
    most_abundant_item = item_list[0]

    for item_name in item_list[1:]:
        if inventory[item_name] > inventory[most_abundant_item]:
            most_abundant_item = item_name
    return most_abundant_item


def get_least_abundant_item(inventory: dict[str, int]) -> str:
    item_list = list(inventory.keys())
    least_abundant_item = item_list[0]

    for item_name in item_list[1:]:
        if inventory[item_name] < inventory[least_abundant_item]:
            least_abundant_item = item_name
    return least_abundant_item


def print_inventory_analysis(inventory: dict[str, int]) -> None:
    item_list = list(inventory.keys())
    total_quantity = sum(inventory.values())

    print(f"Got inventory: {inventory}")
    print(f"Item list: {item_list}")
    print(
        f"Total quantity of the {len(item_list)} items: {total_quantity}"
    )

    if total_quantity > 0:
        for item_name in inventory:
            percentage = round(
                (inventory[item_name] * 100) / total_quantity,
                1,
            )
            print(f"Item {item_name} represents {percentage}%")

        most_abundant_item = get_most_abundant_item(inventory)
        least_abundant_item = get_least_abundant_item(inventory)
        print(
            "Item most abundant: "
            f"{most_abundant_item} with quantity "
            f"{inventory[most_abundant_item]}"
        )
        print(
            "Item least abundant: "
            f"{least_abundant_item} with quantity "
            f"{inventory[least_abundant_item]}"
        )
    else:
        print("Item most abundant: none")
        print("Item least abundant: none")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory = parse_inventory(sys.argv[1:])
    print_inventory_analysis(inventory)


if __name__ == "__main__":
    main()
