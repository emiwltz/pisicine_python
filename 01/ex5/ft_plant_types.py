#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: int, age_days: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age_days


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        age_days: int,
        color: str,
    ) -> None:
        super().__init__(name, height, age_days)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")

    def get_info(self) -> str:
        return (
            f"{self.name} (Flower): {self.height}cm, "
            f"{self.age_days} days, {self.color} color"
        )


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        age_days: int,
        trunk_diameter: int,
    ) -> None:
        super().__init__(name, height, age_days)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        shade = round((self.height * self.trunk_diameter) / 320)
        print(f"{self.name} provides {shade} square meters of shade")

    def get_info(self) -> str:
        return (
            f"{self.name} (Tree): {self.height}cm, "
            f"{self.age_days} days, {self.trunk_diameter}cm diameter"
        )


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        age_days: int,
        harvest_season: str,
        nutritional_value: str,
    ) -> None:
        super().__init__(name, height, age_days)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self) -> str:
        return (
            f"{self.name} (Vegetable): {self.height}cm, "
            f"{self.age_days} days, {self.harvest_season} harvest"
        )

    def get_nutrition_info(self) -> str:
        return f"{self.name} is rich in {self.nutritional_value}"


def main() -> None:
    print("=== Garden Plant Types ===")
    print()

    rose = Flower("Rose", 25, 30, "red")
    tulip = Flower("Tulip", 18, 20, "yellow")
    for flower in [rose, tulip]:
        print(flower.get_info())
        flower.bloom()
        print()

    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 420, 1460, 42)
    for tree in [oak, pine]:
        print(tree.get_info())
        tree.produce_shade()
        print()

    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 35, 70, "autumn", "beta-carotene")
    for vegetable in [tomato, carrot]:
        print(vegetable.get_info())
        print(vegetable.get_nutrition_info())
        print()


if __name__ == "__main__":
    main()
