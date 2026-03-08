#!/usr/bin/env python3

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def check_plant(days_without_water: int) -> None:
    if days_without_water > 7:
        raise PlantError("The tomato plant is wilting!")


def check_water_tank(liters: int) -> None:
    if liters < 10:
        raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")

    print("Testing PlantError.")
    try:
        check_plant(10)
    except PlantError as error:
        print(f"Caught PlantError: {error}")

    print("Testing WaterError.")
    try:
        check_water_tank(5)
    except WaterError as error:
        print(f"Caught WaterError: {error}")

    print("Testing catching all garden errors...")
    try:
        check_plant(10)
    except GardenError as error:
        print(f"Caught a garden error: {error}")

    try:
        check_water_tank(5)
    except GardenError as error:
        print(f"Caught a garden error: {error}")

    print("All custom error types work correctly!")


def main() -> None:
    test_custom_errors()


if __name__ == "__main__":
    main()
