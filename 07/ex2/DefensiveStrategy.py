from typing import cast

from ex0.Creature import Creature
from ex1.HealCapability import HealCapability
from ex2.BattleStrategy import BattleStrategy


class DefensiveStrategy(BattleStrategy):
    error_label = "defensive"

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> list[str]:
        if not self.is_valid(creature):
            self._raise_invalid(creature)

        healer = cast(HealCapability, creature)
        return [creature.attack(), healer.heal()]
