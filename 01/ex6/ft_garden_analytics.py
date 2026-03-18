class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.set_height(height)
        self.set_age(age)

    def grow(self) -> None:
        self.height += 1

    def age_plant(self) -> None:
        self.age += 1

    @staticmethod
    def is_valid_value(value: int) -> bool:
        return value >= 0

    @staticmethod
    def validate_height_or_age(value: int) -> None:
        if not Plant.is_valid_value(value):
            raise ValueError("height or age cannot be negative")

    def set_height(self, height: int) -> None:
        self.validate_height_or_age(height)
        self.height = height

    def set_age(self, age: int) -> None:
        self.validate_height_or_age(age)
        self.age = age

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"

    def get_garden_display(self) -> str:
        return f"- {self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.blooming = False

    def bloom(self) -> None:
        self.blooming = True

    def grow(self) -> None:
        super().grow()
        self.bloom()

    def get_info(self) -> str:
        base = super().get_info()
        return f"{base}, {self.color} color"

    def get_garden_display(self) -> str:
        status = "blooming" if self.blooming else "not blooming"
        return (
            f"- {self.name}: {self.height}cm, "
            f"{self.color} flowers ({status})"
        )


class PrizeFlower(FloweringPlant):
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        color: str,
        prize_points: int,
    ) -> None:
        super().__init__(name, height, age, color)
        self.prize_points = prize_points

    def get_info(self) -> str:
        base = super().get_info()
        return f"{base}, {self.prize_points} prize points"

    def get_garden_display(self) -> str:
        base = super().get_garden_display()
        return f"{base}, Prize points: {self.prize_points}"


class Garden:
    def __init__(self, name: str) -> None:
        self.name = name
        self.plants: list[Plant] = []
        self.plants_added = 0
        self.total_growth = 0

    def add_plant(self, plant: Plant) -> str:
        self.plants.append(plant)
        self.plants_added += 1
        return f"Added {plant.name} to {self.name}'s garden"

    def grow_all(self) -> list[str]:
        messages = [f"{self.name} is helping all plants grow..."]
        for plant in self.plants:
            plant.grow()
            plant.age_plant()
            self.total_growth += 1
            messages.append(f"{plant.name} grew 1cm")
        return messages

    def get_plant_lines(self) -> str:
        if not self.plants:
            return "- No plants in garden"

        lines = []
        for plant in self.plants:
            lines.append(plant.get_garden_display())
        return "\n".join(lines)


class GardenManager:
    total_gardens_managed = 0

    class GardenStats:
        @staticmethod
        def count_plant_types(garden: "Garden") -> tuple[int, int, int]:
            regular = 0
            flowering = 0
            prize = 0

            for plant in garden.plants:
                if isinstance(plant, PrizeFlower):
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1
            return regular, flowering, prize

        @staticmethod
        def calculate_score(garden: "Garden") -> int:
            score = 0

            for plant in garden.plants:
                if isinstance(plant, PrizeFlower):
                    score += plant.height + 20 + plant.prize_points
                elif isinstance(plant, FloweringPlant):
                    score += plant.height + 10
                else:
                    score += plant.height
            return score

    def __init__(self, network_name: str) -> None:
        self.network_name = network_name
        self.gardens: list[Garden] = []

    @classmethod
    def create_garden_network(cls, name: str) -> "GardenManager":
        return cls(name)

    @classmethod
    def get_total_gardens_managed(cls) -> int:
        return cls.total_gardens_managed

    @staticmethod
    def validate_height(height: int) -> bool:
        return height >= 0

    def add_garden(self, garden: Garden) -> None:
        self.gardens.append(garden)
        GardenManager.total_gardens_managed += 1

    def get_garden(self, name: str) -> "Garden | None":
        for garden in self.gardens:
            if garden.name == name:
                return garden
        return None

    def build_garden_report(self, garden_name: str) -> str:
        garden = self.get_garden(garden_name)
        if garden is None:
            return "Garden not found"

        regular, flowering, prize = self.GardenStats.count_plant_types(garden)

        report = f"=== {garden.name}'s Garden Report ===\n"
        report += "Plants in garden:\n"
        report += garden.get_plant_lines()
        report += "\n"
        report += (
            f"Plants added: {garden.plants_added}, "
            f"Total growth: {garden.total_growth}cm\n"
        )
        report += (
            f"Plant types: {regular} regular, {flowering} flowering, "
            f"{prize} prize flowers"
        )
        return report

    def get_scores_summary(self) -> str:
        scores = []

        for garden in self.gardens:
            score = self.GardenStats.calculate_score(garden)
            scores.append(f"{garden.name}: {score}")

        return "Garden scores - " + ", ".join(scores)


def main() -> None:
    manager = GardenManager.create_garden_network("Community Garden Network")

    alice_garden = Garden("Alice")
    bob_garden = Garden("Bob")

    manager.add_garden(alice_garden)
    manager.add_garden(bob_garden)

    oak = Plant("Oak Tree", 100, 365)
    rose = FloweringPlant("Rose", 25, 30, "red")
    sunflower = PrizeFlower("Sunflower", 50, 45, "yellow", 10)
    fern = Plant("Fern", 40, 120)
    lily = FloweringPlant("Lily", 42, 20, "white")

    print("=== Garden Management System Demo ===")
    print()
    print(alice_garden.add_plant(oak))
    print(alice_garden.add_plant(rose))
    print(alice_garden.add_plant(sunflower))
    print()

    bob_garden.add_plant(fern)
    bob_garden.add_plant(lily)

    for message in alice_garden.grow_all():
        print(message)

    print()
    print(manager.build_garden_report("Alice"))
    print()
    print(f"Height validation test: {GardenManager.validate_height(25)}")
    print(manager.get_scores_summary())
    print(
        f"Total gardens managed: "
        f"{GardenManager.get_total_gardens_managed()}"
    )


if __name__ == "__main__":
    main()
