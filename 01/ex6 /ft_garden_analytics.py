#!/usr/bin/env python3


class GardenManager:
    def __init__(self, gardens: list):
        self.gardens = gardens


class Garden:
    def __init__(self, name: str, plants: list) -> None:
        self.name = name
        self.plants = plants

    def add_plant(self, plant: list) -> None:
        self.plants += [plant]

    def grow_all(self):
        for plant in self.plants:
            plant.grow()

    def get_info(self):
        for plant in self.plants:
            plant.get_info()


class Plant:
    def __init__(self, name: str, height: int, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days
        self.type = "Standard"

    def grow(self):
        self.height += 1
        self.days += 1

    def get_info(self):
        print(f"{self.name} Tree: {self.height}cm")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, days: int, color: str) -> None:
        super().__init__(name, height, days)
        self.color = color
        self.type = "Flower"
        self.blooming = "Not blooming yet"
        if self.days > 7:
            self.blooming = "Blooming"

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.color} flower, ({self.blooming})")


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, days: int, color: str) -> None:
        super().__init__(name, height, days, color)
        self.prize = self.height * self.days
        self.type = "Prize Flower"

    def get_info(self):
        print(
            f"{self.name}: {self.height}cm, {self.color} flower, ({self.blooming}), Prize points: {self.prize}"
        )


# def main():
#     p1 = Plant("tulipe", 20, 10)
#     p2 = Plant("coquelicot", 20, 10)
#     p3 = Plant("tournesol", 20, 10)
#     plants = [p1, p2, p3]
#     garden1 = Garden("emi", plants)
#     print(f"{garden1.name}")
#     garden1.get_info()


def main():
    p1 = Plant("Oak", 20, 10)
    p2 = FloweringPlant("Rose", 25, 8, "red")
    p3 = PrizeFlower("Sunflower", 50, 12, "yellow")

    plants = [p1, p2, p3]
    garden1 = Garden("Emi", plants)

    print("=== Garden name ===")
    print(garden1.name)

    print("\n=== Initial state ===")
    garden1.get_info()

    print("\n=== After grow_all ===")
    garden1.grow_all()
    garden1.get_info()

    print("\n=== Add one plant ===")
    p4 = Plant("Cactus", 15, 4)
    garden1.add_plant(p4)
    garden1.get_info()


if __name__ == "__main__":
    main()
