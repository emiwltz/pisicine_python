from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        durability: int,
        effect: str
    ):
        super().__init__(name, cost, rarity)
        if isinstance(durability, int) and durability > 0:
            self.durability = durability
        else:
            raise ValueError("durability must be a positive int")
        if isinstance(effect, str) and effect:
            self.effect = effect
        else:
            raise ValueError("Effect cannot be empty")
        self.__is_active = False

    def play(self, game_state: dict) -> dict:
        if self.__is_active:
            raise ValueError("Card already active")
        if not isinstance(game_state, dict):
            raise ValueError("game_state must be a dict")
        if "mana" not in game_state:
            raise ValueError("game_state must contain a mana key")

        available_mana = game_state["mana"]
        if not isinstance(available_mana, int):
            raise ValueError("mana must be an int")
        if not self.is_playable(available_mana):
            raise ValueError("Not enough mana to play this card")

        self.__is_active = True
        remaining_mana = available_mana - self.cost
        game_state["mana"] = remaining_mana
        move = {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect,
            "remaining_mana": remaining_mana,
        }
        return move

    def activate_ability(self) -> dict:
        if not self.__is_active:
            raise ValueError("Artifact must be in play before activation")
        if self.durability <= 0:
            raise ValueError("Artifact is destroyed")

        self.durability -= 1
        ability_result = {
            "artifact": self.name,
            "ability_activated": self.effect,
            "durability_remaining": self.durability,
            "still_active": self.durability > 0,
        }
        if self.durability == 0:
            self.__is_active = False
        return ability_result
