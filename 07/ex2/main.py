from ex2.EliteCard import EliteCard


def main():
    print()
    print("=== DataDeck Ability System ===")
    print()

    elite_card = EliteCard("Arcane Warrior", 3, "legendary", 3, 3, 3, 5)
    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']\n"
          "- Combatable: ['attack', 'defend', 'get_combat_stats']\n"
          "- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")
    print()

    print(f"Playing elite_card: {elite_card.play({'mana': 5})}")
    print()
    print("Playing Arcane Warrior (Elite Card):")
    print("Combat phase:")
    print(f"Attack result: {elite_card.attack('Enemy')}")
    print(f"Defense result: {elite_card.defend(3)}")
    print()

    print("Magic phase:")
    print(f"Spell cast: {elite_card.cast_spell('Fireball', ['enemy1', 'enemy2'])}")
    print(f"Mana chanell: {elite_card.channel_mana(3)}")
    print()

    print("Get card info:")
    print(f"Combat info: {elite_card.get_combat_stats()}")
    print(f"Magic info: {elite_card.get_magic_stats()}")


if __name__ == "__main__":
    main()
