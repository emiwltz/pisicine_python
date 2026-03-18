#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


def main() -> None:
    plant_1 = Plant("Tulipe", 21, 60)
    plant_2 = Plant("Tournesol", 34, 12)
    plant_3 = Plant("Coquelicot", 5, 34)
    plants = [plant_1, plant_2, plant_3]

    print("=== Garden Plant Registry ===")
    for plant in plants:
        print(f"{plant.name}: {plant.height}cm, {plant.age} days old")


if __name__ == "__main__":
    main()
