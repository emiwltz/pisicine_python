from ex0.Card import Card


class CreatureCard(Card):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int
    ):
        super().__init__(name, cost, rarity)
        self.type = "Creature"
        if (
            isinstance(attack, int)
            and isinstance(health, int)
            and attack > 0
            and health > 0
        ):
            self.attack = attack
            self.health = health
        else:
            raise ValueError(
                "Invalid data: attack and health must be a positive int")

    def play(self, game_state: dict) -> dict:
        if not isinstance(game_state, dict):
            raise ValueError("game_state must be a dict")
        if "mana" not in game_state:
            raise ValueError("game_state must contain a mana key")

        available_mana = game_state["mana"]
        if not isinstance(available_mana, int):
            raise ValueError("mana must be an int")
        if not self.is_playable(available_mana):
            raise ValueError("Not enough mana to play this creature")

        remaining_mana = available_mana - self.cost
        game_state["mana"] = remaining_mana
        move = {
            "card_played": self.name,
            "mana_used": self.cost,
            "remaining_mana": remaining_mana,
            "effect": "Creature summoned to battlefield",
        }
        return move

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info.update(
            {"attack": self.attack, "health": self.health, "type": self.type})
        return info

    def attack_target(self, target) -> dict:
        attack_move = {'attacker': self.name, 'target': target,
                       'damage_dealt': self.attack, 'combat_resolved': True}
        return attack_move
