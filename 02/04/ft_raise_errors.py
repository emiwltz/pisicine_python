def check_plant_health(plant_name: str, water_level: int, sunlight_hours: int):
    if not plant_name:
        raise ValueError("Plant name cannot be empty")
    elif water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    elif water_level < 0:
        raise ValueError(f"Water level {water_level} is too low (min 0)")
    elif sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too hight (max 12)")
    elif sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    return "OK"


def test_plant_checks():
    try:
        plant = "tomato"
        check_plant_health(plant, 5, 4)
        print(f"{plant} is in good health")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        plant = ""
        check_plant_health(plant, 5, 4)
        print(f"{plant} is in good health")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        plant = "tomato"
        check_plant_health(plant, -2, 4)
        print(f"{plant} is in good health")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        plant = "tomato"
        check_plant_health(plant, 5, 29)
        print(f"{plant} is in good health")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    test_plant_checks()
