from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str):
        if name:
            self.name = name
        else:
            raise ValueError("Name cannot be empty")
        if isinstance(cost, int) and cost >= 0:
            self.cost = cost
        else:
            raise ValueError("Cost must be a positive int")
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        info = {"name": self.name, "cost": self.cost, "rarity": self.rarity}
        return info

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost
