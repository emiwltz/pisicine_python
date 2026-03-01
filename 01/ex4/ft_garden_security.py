#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: int, age_days: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age_days

    if name < 0:
        return("error")
    def grow(self):
        self.height = self.height + 1

    def age(self):
        self.age_days = self.age_days + 1

    def get_info(self):
        return (f"{self.name}: ({self.height}cm, {self.age_days} days)")


def main():
    names = ["Rose", "Tulipe", "Tournesol", "Cactus", "Coquelicot"]
    heights = [12, 13, 50, 120, 20]
    age_days = [4, 12, 43, 23, 40]
    garden_size = 5
    plants = [None] * garden_size
    for i in range(garden_size):
        plant = Plant(names[i], heights[i], age_days[i])
        plants[i] = plant

    print("=== Plant Factory Output ===")
    for i in range(garden_size):
        disp_info = plants[i].get_info()
        print(f"Created: {disp_info}")
    print(f"Total plant created: {garden_size}")


if __name__ == "__main__":
    main()
