from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int):
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
        move = {"card_played": self.name,
                "mana_used": self.cost, "effect": "Creature summoned to battlefield"}
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
