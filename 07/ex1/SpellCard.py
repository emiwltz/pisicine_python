from ex0.Card import Card


class SpellCard(Card):
    VALID_EFFECT_TYPES = ("damage", "heal", "buff", "debuff")

    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        if effect_type not in self.VALID_EFFECT_TYPES:
            raise ValueError(
                "effect_type must be damage, heal, buff, or debuff"
            )
        self.effect_type = effect_type
        self.__has_been_played = False

    def play(self, game_state: dict) -> dict:
        if self.__has_been_played:
            raise ValueError("Spell cards can only be played once")
        if not isinstance(game_state, dict):
            raise ValueError("game_state must be a dict")
        if "mana" not in game_state:
            raise ValueError("game_state must contain a mana key")

        available_mana = game_state["mana"]
        if not isinstance(available_mana, int):
            raise ValueError("mana must be an int")
        if not self.is_playable(available_mana):
            raise ValueError("Not enough mana to play this spell")

        targets = game_state.get("targets", [])
        resolved_effect = self.resolve_effect(targets)
        remaining_mana = available_mana - self.cost
        game_state["mana"] = remaining_mana
        self.__has_been_played = True
        move = {
            "card_played": self.name,
            "mana_used": self.cost,
            "remaining_mana": remaining_mana,
            "effect": resolved_effect["description"],
        }
        return move

    def resolve_effect(self, targets: list) -> dict:
        if not isinstance(targets, list):
            raise ValueError("targets must be a list")

        descriptions = {
            "damage": "Deal 3 damage to target",
            "heal": "Restore 3 health to target",
            "buff": "Grant +2 power to target",
            "debuff": "Reduce target power by 2",
        }

        effect = {
            "effect_type": self.effect_type,
            "targets": targets,
            "description": descriptions[self.effect_type],
        }
        return effect
