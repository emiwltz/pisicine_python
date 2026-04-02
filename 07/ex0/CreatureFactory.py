from abc import ABC, abstractmethod

from ex0.Creature import Creature


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        """Create the base Creature for a family."""

    @abstractmethod
    def create_evolved(self) -> Creature:
        """Create the evolved Creature for a family."""
