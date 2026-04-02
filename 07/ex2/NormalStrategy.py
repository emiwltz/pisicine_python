from ex0.Creature import Creature
from ex2.BattleStrategy import BattleStrategy


class NormalStrategy(BattleStrategy):
    error_label = "normal"

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> list[str]:
        if not self.is_valid(creature):
            self._raise_invalid(creature)
        return [creature.attack()]
