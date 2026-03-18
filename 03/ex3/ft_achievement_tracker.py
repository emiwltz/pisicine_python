def set_analytics(
    alice: set[str],
    bob: set[str],
    charlie: set[str],
) -> None:
    all_achievements = alice.union(bob).union(charlie)
    common_achievements = alice.intersection(bob).intersection(charlie)
    rare_achievements = (
        alice.difference(bob).difference(charlie)
        .union(bob.difference(alice).difference(charlie))
        .union(charlie.difference(alice).difference(bob))
    )

    print("=== Achievement Analytics ===")
    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}")
    print()
    print(f"Common to all players: {common_achievements}")
    print(f"Rare achievements (1 player): {rare_achievements}")
    print()
    print(f"Alice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")


def main() -> None:
    alice = {"first_kill", "level_10", "treasure_hunter", "speed_demon"}
    bob = {"first_kill", "level_10", "boss_slayer", "collector"}
    charlie = {
        "level_10",
        "treasure_hunter",
        "boss_slayer",
        "speed_demon",
        "perfectionist",
    }

    print("=== Achievement Tracker System ===")
    print()
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")
    print()
    set_analytics(alice, bob, charlie)


if __name__ == "__main__":
    main()
