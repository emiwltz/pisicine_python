#!/usr/bin/env python3


class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class Plant:
    def __init__(self, name: str, water_level: int, sun_level: int) -> None:
        self.name = name
        self.water_level = water_level
        self.sun_level = sun_level


class GardenManager:
    def __init__(self) -> None:
        self.plants: list[Plant] = []

    def add_plant(self, plant: Plant) -> None:
        if not plant.name:
            raise PlantError("Plant name cannot be empty!")
        self.plants.append(plant)
        print(f"Added {plant.name} successfully")

    def water_plants(self) -> None:
        print("Opening watering system")
        try:
            for plant in self.plants:
                print(f"Watering {plant.name} - success")
                plant.water_level += 1
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant: Plant) -> str:
        if not plant.name:
            raise PlantError("Plant name cannot be empty!")
        if plant.water_level < 1:
            raise WaterError(
                f"Water level {plant.water_level} is too low (min 1)"
            )
        if plant.water_level > 10:
            raise WaterError(
                f"Water level {plant.water_level} is too high (max 10)"
            )
        if plant.sun_level < 2:
            raise PlantError(
                f"Sun level {plant.sun_level} is too low (min 2)"
            )
        if plant.sun_level > 12:
            raise PlantError(
                f"Sun level {plant.sun_level} is too high (max 12)"
            )
        return (
            f"{plant.name}: healthy "
            f"(water: {plant.water_level}, sun: {plant.sun_level})"
        )

    def check_water_tank(self, liters: int) -> None:
        if liters < 10:
            raise WaterError("Not enough water in tank")


def test_garden_management() -> None:
    print("=== Garden Management System ===")
    print()

    manager = GardenManager()
    tomato = Plant("tomato", 5, 8)
    lettuce = Plant("lettuce", 15, 8)
    empty = Plant("", 2, 3)

    print("Adding plants to garden...")
    try:
        manager.add_plant(tomato)
        manager.add_plant(lettuce)
        manager.add_plant(empty)
    except PlantError as error:
        print(f"Error adding plant: {error}")
    print()

    print("Watering plants...")
    manager.water_plants()
    print()

    print("Checking plant health...")
    for plant in manager.plants:
        try:
            print(manager.check_plant_health(plant))
        except GardenError as error:
            print(f"Error checking {plant.name}: {error}")
    print()

    print("Testing error recovery...")
    try:
        manager.check_water_tank(5)
    except GardenError as error:
        print(f"Caught GardenError: {error}")
        print("System recovered and continuing...")
    print()

    print("Garden management system test complete!")


def main() -> None:
    test_garden_management()


if __name__ == "__main__":
    main()
