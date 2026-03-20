#!/usr/bin/env python3


class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(
            f"Invalid plant name to water: '{plant_name}'"
        )
    print(f"Watering {plant_name}: [OK]")


def run_watering_test(
    first_plant: str,
    second_plant: str,
    third_plant: str,
) -> None:
    print("Opening watering system")
    try:
        water_plant(first_plant)
        water_plant(second_plant)
        water_plant(third_plant)
    except PlantError as error:
        print(f"Caught PlantError: {error}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")
    print()

    print("Testing valid plants...")
    run_watering_test("Tomato", "Lettuce", "Carrots")
    print()

    print("Testing invalid plants...")
    run_watering_test("Tomato", "lettuce", "Carrots")
    print()

    print("Cleanup always happens, even with errors!")


def main() -> None:
    test_watering_system()


if __name__ == "__main__":
    main()
