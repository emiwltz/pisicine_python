#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: int, age_days: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age_days

    def grow(self) -> None:
        self.height += 1

    def age(self) -> None:
        self.age_days += 1

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age_days} days old"


def main() -> None:
    plant_1 = Plant("Tulipe", 23, 12)
    plant_2 = Plant("Tournesol", 34, 12)
    plant_3 = Plant("Coquelicot", 5, 34)
    plants = [plant_1, plant_2, plant_3]
    start_height = plant_1.height

    print("=== Day 1 ===")
    for plant in plants:
        print(plant.get_info())

    for _ in range(6):
        for plant in plants:
            plant.grow()
            plant.age()

    print("=== Day 7 ===")
    for plant in plants:
        print(plant.get_info())

    growth = plant_1.height - start_height
    print(f"Growth this week: +{growth}cm")


if __name__ == "__main__":
    main()
