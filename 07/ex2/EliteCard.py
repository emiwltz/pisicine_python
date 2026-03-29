from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def play(self, game_state: dict) -> dict:
        pass

    def attack(self, target) -> dict:
        pass

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        pass
