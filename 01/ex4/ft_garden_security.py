#!/usr/bin/env python3

class SecurePlant:
    def __init__(self, name: str, height: int, age_days: int) -> None:
        self.name = name
        self._height = 0
        self._age_days = 0
        self.set_height(height)
        self.set_age(age_days)

    def set_height(self, height: int) -> None:
        if height < 0:
            print("[SECURITY] Rejected height:", height)
            return
        self._height = height
        print("Height updated:", self._height)

    def set_age(self, age_days: int) -> None:
        if age_days < 0:
            print("[SECURITY] Rejected age:", age_days)
            return
        self._age_days = age_days
        print("Age updated:", self._age_days)

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age_days

    def get_info(self) -> str:
        return f"{self.name}: ({self._height}cm, {self._age_days} days)"


def main():
    print("=== Garden Security System ===")

    plant = SecurePlant("Coquelicot", 2, 3)
    print("Current:", plant.get_info())

    plant.set_height(-2)
    plant.set_age(-1)

    plant.set_height(12)

    print("Final:", plant.get_info())


if __name__ == "__main__":
    main()
