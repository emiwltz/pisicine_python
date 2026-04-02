from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, creature_type: str) -> None:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Creature name must be a non-empty string")
        if not isinstance(creature_type, str) or not creature_type.strip():
            raise ValueError("Creature type must be a non-empty string")
        self.name = name
        self.creature_type = creature_type

    def describe(self) -> str:
        return f"{self.name} is a {self.creature_type} type Creature"

    @abstractmethod
    def attack(self) -> str:
        """Return the Creature attack message."""
