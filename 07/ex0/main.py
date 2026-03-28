from ex0.CreatureCard import CreatureCard


def main():
    print()
    print("=== DataDeck Card Foundation ===")
    print()

    print("Testing Abstract Base Class Design:")
    print()

    print("CreatureCard Info:")
    fire_dragon = CreatureCard("test", 5, "rare", 4, 5)
    print(fire_dragon.get_card_info())
    print()

    game_state = {}
    print("Playing Fire Dragon with 6 mana available:")
    print(f"Playable: {fire_dragon.is_playable(6)}")
    print(f"Play result: {fire_dragon.play(game_state)}")
    print()

    target = "Goblin Warrior"
    print("Fire Dragon attacks Goblin Warrior:")
    print(f"Attack result: {fire_dragon.attack_target(target)}")
    print()

    print("Testing insufficient mana (3 available):")
    print(f"Playable: {fire_dragon.is_playable(3)}")


if __name__ == "__main__":
    main()
