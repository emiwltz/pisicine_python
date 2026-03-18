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
        return f"{self.name} ({self.height}cm, {self.age_days} days)"


def main() -> None:
    names = ["Rose", "Oak", "Cactus", "Sunflower", "Fern"]
    heights = [25, 200, 5, 80, 15]
    ages = [30, 365, 90, 45, 120]
    garden_size = 5
    plants = [None] * garden_size

    for index in range(garden_size):
        plants[index] = Plant(names[index], heights[index], ages[index])

    print("=== Plant Factory Output ===")
    for index in range(garden_size):
        print(f"Created: {plants[index].get_info()}")

    print(f"Total plants created: {garden_size}")


if __name__ == "__main__":
    main()
