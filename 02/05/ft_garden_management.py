class GardenManager:
    def __init__(self):
        self.plants = []

    def add_plant(self, plant: str):
        if not plant.name:
            raise ValueError("Plant name cannot be empty")
        else:
            self.plants.append(plant)

    def check_health(self):
        for plant in self.plants:

    def water_plant(self):
        print("Opening watering level")
        for plant in self.plants:
            print(f"Watering {plant.name} - success")
            plant.water_level += 1
        print("Closing watering level")


class Plant:
    def __init__(self, name: str):
        self.name = name
        self.water_level = 0


def test_garden_management():
    tomato = Plant("tomato")
    cactus = Plant("cactus")
    empty = Plant("")
    garden = GardenManager()
    garden.add_plant(tomato)
    garden.add_plant(cactus)
    try:
        garden.add_plant(empty)
    except ValueError as e:
        print(e)
    garden.water_plant()


if __name__ == "__main__":
    test_garden_management()
