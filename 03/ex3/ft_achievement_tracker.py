def set_analytics(alice: set, bob: set, charlie: set):
    print("=== Achievement Analytics ===")
    print(f"All unique achievements: {charlie.union(bob).union(alice)}")
    print(f"Total unique achievements: {len(charlie.union(bob).union(alice))}")
    print()
    print(f"Common to all players: {charlie.intersection(bob).intersection(alice)}")
    bob_unique = bob.difference(charlie).difference(alice)
    alice_unique = alice.difference(charlie).difference(bob)
    charlie_unique = charlie.difference(bob).difference(alice)
    rare_item = bob_unique.union(charlie_unique).union(alice_unique)
    print(f"Rare achievements (1 player): {rare_item}")
    print()
    print(f"Alice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")


def main():
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
    print(f"Alice achievement: {alice}")
    print(f"Bob achievement: {bob}")
    print(f"Charlie achievement: {charlie}")
    print()
    set_analytics(alice, bob, charlie)


if __name__ == "__main__":
    main()
