from typing import cast

from ex0.Creature import Creature
from ex1.TransformCapability import TransformCapability
from ex2.BattleStrategy import BattleStrategy


class AggressiveStrategy(BattleStrategy):
    error_label = "aggressive"

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> list[str]:
        if not self.is_valid(creature):
            self._raise_invalid(creature)

        transformer = cast(TransformCapability, creature)
        return [transformer.transform(), creature.attack(), transformer.revert()]
