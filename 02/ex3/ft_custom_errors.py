#!/usr/bin/env python3


class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def raise_plant_error() -> None:
    raise PlantError("The tomato plant is wilting!")


def raise_water_error() -> None:
    raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")
    print()

    print("Testing PlantError...")
    try:
        raise_plant_error()
    except PlantError as error:
        print(f"Caught PlantError: {error}")
    print()

    print("Testing WaterError...")
    try:
        raise_water_error()
    except WaterError as error:
        print(f"Caught WaterError: {error}")
    print()

    print("Testing catching all garden errors...")
    try:
        raise_plant_error()
    except GardenError as error:
        print(f"Caught GardenError: {error}")

    try:
        raise_water_error()
    except GardenError as error:
        print(f"Caught GardenError: {error}")
    print()

    print("All custom error types work correctly!")


def main() -> None:
    test_custom_errors()


if __name__ == "__main__":
    main()
