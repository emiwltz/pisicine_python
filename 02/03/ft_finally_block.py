#!/usr/bin/env python3


def water_plants(plant_list: list) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")

    print("Testing normal watering.")
    good_list = ["tomato", "lettuce", "carrots"]
    try:
        water_plants(good_list)
        print("Watering completed successfully!")
    except ValueError as error:
        print(f"Error: {error}")
    finally:
        print("Normal test finished.")

    print("Testing with error...")
    bad_list = ["tomato", None, "carrots"]
    try:
        water_plants(bad_list)
        print("Watering completed successfully!")
    except ValueError as error:
        print(f"Error: {error}")
    finally:
        print("Cleanup always happens, even with errors!")


def main() -> None:
    test_watering_system()


if __name__ == "__main__":
    main()
