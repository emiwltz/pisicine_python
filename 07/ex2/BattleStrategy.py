from abc import ABC, abstractmethod

from ex0.Creature import Creature
from ex2.exceptions import InvalidStrategyError


class BattleStrategy(ABC):
    error_label: str = "battle"

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        """Return whether the strategy can be applied to this Creature."""

    @abstractmethod
    def act(self, creature: Creature) -> list[str]:
        """Return the ordered list of actions performed by the Creature."""

    def _raise_invalid(self, creature: Creature) -> None:
        raise InvalidStrategyError(
            f"Invalid Creature '{creature.name}' for this "
            f"{self.error_label} strategy"
        )
