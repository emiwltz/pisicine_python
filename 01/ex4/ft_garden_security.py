#!/usr/bin/env python3


class SecurePlant:
    def __init__(self, name: str, height: int, age_days: int) -> None:
        self.name = name
        self._height = 0
        self._age_days = 0
        if height >= 0:
            self._height = height
        if age_days >= 0:
            self._age_days = age_days

    def set_height(self, height: int) -> None:
        if height < 0:
            print("Security: Negative height rejected")
            return
        self._height = height
        print(f"Height updated: {self._height}cm [OK]")

    def set_age(self, age_days: int) -> None:
        if age_days < 0:
            print("Security: Negative age rejected")
            return
        self._age_days = age_days
        print(f"Age updated: {self._age_days} days [OK]")

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age_days

    def get_info(self) -> str:
        return f"{self.name} ({self._height}cm, {self._age_days} days)"


def main() -> None:
    print("=== Garden Security System ===")

    plant = SecurePlant("Rose", 25, 30)
    print(f"Plant created: {plant.name}")
    plant.set_height(plant.get_height())
    plant.set_age(plant.get_age())
    print()

    print("Invalid operation attempted: height -5cm [REJECTED]")
    plant.set_height(-5)
    print()

    print(f"Current plant: {plant.get_info()}")


if __name__ == "__main__":
    main()
