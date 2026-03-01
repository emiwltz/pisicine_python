#!/usr/bin/env python3
class BasePlant:
    def __init__(self, name: str, height: int, age_days: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age_days
        self.type = "Undefined"


class Tree(BasePlant):
    def __init__(self, name: str, height: int, age_days: int, diameter: int) -> None:
        super().__init__(name, height, age_days)
        self.diameter = diameter
        self.type = "Tree"

    def produce_shade(self) -> None:
        shade = self.diameter / self.height
        print(f"{self.name} provides {shade} square meters of shade")

    def get_info(self) -> str:
        return (f"{self.name} ({self.type}) {self.height}cm, {self.age_days}days, {self.diameter}cm")


class Flower(BasePlant):
    def __init__(self, name: str, height: int, age_days: int, color: str) -> None:
        super().__init__(name, height, age_days)
        self.color = color
        self.type = "Flower"

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")

    def get_info(self) -> str:
        return (f"{self.name} ({self.type}) {self.height}cm, {self.age_days}days, {self.color}color")


class Vegetable(BasePlant):
    def __init__(self, name: str, height: int, age_days: int, harvest_season: str, nutritional_value: str) -> None:
        super().__init__(name, height, age_days)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        self.type = "Vegetable"

    def get_info(self) -> str:
        return (f"{self.name} ({self.type}) {self.height}cm, {self.age_days}days, {self.harvest_season}harvest\n{self.name} is rich in {self.nutritional_value}")


def main():
    print("=== Garden Plant Types ===\n")
    oak = Tree("oak", 34, 23, 18)
    oak.produce_shade()
    print(oak.get_info())
    banana_tree = Tree("banana_tree", 110, 240, 50)
    print(banana_tree.get_info())
    banana_tree.produce_shade()
    print("\n")

    tulipe = Flower("tulipe", 12, 20, "rouge")
    print(tulipe.get_info())
    tulipe.bloom()
    coquelicot = Flower("coquelicot", 30, 4, "rouge")
    print(coquelicot.get_info())
    coquelicot.bloom()
    print("\n")

    tomato = Vegetable("tomato", 10, 30, "winter", "vitamine c")
    print(tomato.get_info())
    eggplant = Vegetable("eggplant", 10, 30, "summer", "vitamine b")
    print(eggplant.get_info())


if __name__ == "__main__":
    main()
