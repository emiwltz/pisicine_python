from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex1.Deck import Deck


def main():
    print()
    print("=== DataDeck Deck Builder ===")
    print()

    print("Building deck with different card types...")
    creature = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    artifact = ArtifactCard("Mana Crystal", 2, "Rare", 3, "Permanent: +1 mana per turn")
    spell = SpellCard("Lightning Bolt", 3, "Rare", "damage")

    deck = Deck()
    deck.add_card(creature)
    deck.add_card(artifact)
    deck.add_card(spell)
    print(deck.get_deck_stats())
    print()

    print("Shuffling cards")
    deck.shuffle()

    print("Drawing and playing cards:")
    print()
    game_state = {"mana": 7}

    card1 = deck.draw_card()
    card2 = deck.draw_card()
    card3 = deck.draw_card()
    cards = [card1, card2, card3]

    for card in cards:
        try:
            print(f"Drew: {card.name}")
            print(card.play(game_state))
            print()
        except Exception as e:
            print(e)

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
