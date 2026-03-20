import random


ACHIEVEMENTS = [
    "Crafting Genius",
    "World Savior",
    "Master Explorer",
    "Collector Supreme",
    "Untouchable",
    "Boss Slayer",
    "Strategist",
    "Speed Runner",
    "Survivor",
    "Treasure Hunter",
    "Hidden Path Finder",
    "Sharp Mind",
]


def gen_player_achievements() -> set[str]:
    achievement_count = random.randint(5, 9)
    return set(random.sample(ACHIEVEMENTS, achievement_count))


def get_all_distinct_achievements(
    players: list[tuple[str, set[str]]],
) -> set[str]:
    distinct_achievements: set[str] = set()
    for _, achievements in players:
        distinct_achievements = distinct_achievements.union(achievements)
    return distinct_achievements


def get_common_achievements(
    players: list[tuple[str, set[str]]],
) -> set[str]:
    common_achievements = set(ACHIEVEMENTS)
    for _, achievements in players:
        common_achievements = common_achievements.intersection(
            achievements
        )
    return common_achievements


def get_unique_achievements(
    players: list[tuple[str, set[str]]],
    player_index: int,
) -> set[str]:
    other_achievements: set[str] = set()
    current_index = 0
    while current_index < len(players):
        if current_index != player_index:
            other_achievements = other_achievements.union(
                players[current_index][1]
            )
        current_index += 1
    return players[player_index][1].difference(other_achievements)


def main() -> None:
    players = [
        ("Alice", gen_player_achievements()),
        ("Bob", gen_player_achievements()),
        ("Charlie", gen_player_achievements()),
        ("Dylan", gen_player_achievements()),
    ]

    print("=== Achievement Tracker System ===")
    print()

    for player_name, achievements in players:
        print(f"Player {player_name}: {achievements}")
    print()

    all_distinct_achievements = get_all_distinct_achievements(players)
    common_achievements = get_common_achievements(players)

    print(f"All distinct achievements: {all_distinct_achievements}")
    print()
    print(f"Common achievements: {common_achievements}")
    print()

    player_index = 0
    while player_index < len(players):
        player_name = players[player_index][0]
        unique_achievements = get_unique_achievements(players, player_index)
        print(f"Only {player_name} has: {unique_achievements}")
        player_index += 1
    print()

    full_achievement_set = set(ACHIEVEMENTS)
    for player_name, achievements in players:
        missing_achievements = full_achievement_set.difference(achievements)
        print(f"{player_name} is missing: {missing_achievements}")


if __name__ == "__main__":
    main()
