import random
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, card: Card) -> None:
        if isinstance(card, Card):
            self.cards.append(card)
        else:
            raise ValueError("Not a valid card")

    def remove_card(self, card_name: str) -> bool:
        index = 0
        for card in self.cards:
            if card.name == card_name:
                self.cards.pop(index)
                return True
            index += 1
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if self.cards:
            return self.cards.pop(0)
        else:
            raise ValueError("Deck is empty")

    def get_deck_stats(self) -> dict:
        if self.cards:
            deck_size = len(self.cards)
            spell_card = 0
            creature_card = 0
            artefact_card = 0
            total_cost = 0
            for card in self.cards:
                if isinstance(card, SpellCard):
                    spell_card += 1
                if isinstance(card, CreatureCard):
                    creature_card += 1
                if isinstance(card, ArtifactCard):
                    artefact_card += 1
                total_cost += card.cost

            average_cost = round(total_cost / deck_size, 2)
            return {
                "total_cards": deck_size,
                "creatures": creature_card,
                "artifacts": artefact_card,
                "spells": spell_card,
                "avg_cost": average_cost,
            }
        else:
            raise ValueError("Deck is empty")
