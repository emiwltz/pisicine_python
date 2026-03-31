from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        health: int,
        attack_power: int,
        defense_power: int,
        spell_mana: int,
    ):
        super().__init__(name, cost, rarity)
        if (
            isinstance(health, int)
            and isinstance(attack_power, int)
            and isinstance(spell_mana, int)
            and isinstance(defense_power, int)
            and health > 0
            and attack_power > 0
            and spell_mana > 0
            and defense_power > 0
        ):
            self.health = health
            self.attack_power = attack_power
            self.defense_power = defense_power
            self.spell_mana = spell_mana
            self.is_active = False
        else:
            raise ValueError(
                "Health, attack_power, defense_power and speel_power must be a positive int"
            )

    def play(self, game_state: dict) -> dict:
        if not isinstance(game_state, dict):
            raise ValueError("game_state must be a dict")
        if "mana" not in game_state:
            raise ValueError("game_state must contain a mana key")

        available_mana = game_state["mana"]
        if not isinstance(available_mana, int):
            raise ValueError("mana must be an int")
        if not self.is_playable(available_mana):
            raise ValueError("Not enough mana to play this elite card")

        remaining_mana = available_mana - self.cost
        game_state["mana"] = remaining_mana
        move = {
            "card_played": self.name,
            "mana_used": self.cost,
            "remaining_mana": remaining_mana,
            "status": "Elite card summoned to battlefield",
        }
        self.is_active = True
        return move

    def attack(self, target) -> dict:
        if self.is_active and self.health > 0:
            attack_move = {
                "attacker": self.name,
                "target": target,
                "damage_dealt": self.attack_power,
                "combat_resolved": True,
            }
            return attack_move
        raise ValueError(f"{self.name} must be activated and alive before")

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        if self.spell_mana < 4:
            raise ValueError("Card have not enough mana")
        if self.is_active and self.health > 0:
            self.spell_mana -= 4
            return {
                "caster": self.name,
                "spell": spell_name,
                "targets": targets,
                "mana_used": 4
            }
        raise ValueError(f"{self.name} must be activated and alive before")

    def channel_mana(self, amount: int) -> dict:
        if not isinstance(amount, int) or amount < 0:
            raise ValueError("Amount must be a positive int")
        if self.is_active and self.health > 0:
            self.spell_mana += amount
            return {"channeled": amount, "total_mana": self.spell_mana}

        raise ValueError(f"{self.name} must be activated and alive before")

    def get_magic_stats(self) -> dict:
        return {
            "name": self.name,
            "spell_mana": self.spell_mana,
            "is_active": self.is_active,
        }

    def defend(self, incoming_damage: int) -> dict:
        if not isinstance(incoming_damage, int) or incoming_damage <= 0:
            raise ValueError("incoming_damage must be a postive int")
        if self.is_active and self.health > 0:
            damage_blocked = min(incoming_damage, self.defense_power)
            damage_taken = incoming_damage - damage_blocked
            self.health -= damage_taken
            is_alive = True
            if self.health <= 0:
                is_alive = False
                self.health = 0
            return {
                "defender": self.name,
                "damage_taken": damage_taken,
                "damage_blocked": damage_blocked,
                "is_alive": is_alive,
            }

        raise ValueError(f"{self.name} must be activated and alive before")

    def get_combat_stats(self) -> dict:
        return {
            "name": self.name,
            "health": self.health,
            "attack_power": self.attack_power,
            "defense_power": self.defense_power,
            "is_active": self.is_active,
        }
