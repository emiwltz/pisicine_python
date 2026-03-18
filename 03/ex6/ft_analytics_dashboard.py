def list_comprehensions(players: list[dict[str, object]]) -> None:
    print("=== List Comprehension Examples ===")
    high_scorers = [
        player["name"] for player in players if player["score"] > 2000
    ]
    scores_doubled = [player["score"] * 2 for player in players]
    active_players = [
        player["name"] for player in players if player["is_active"]
    ]

    print(f"High scorers (>2000): {high_scorers}")
    print(f"Scores doubled: {scores_doubled}")
    print(f"Active players: {active_players}")
    print()


def dict_comprehensions(players: list[dict[str, object]]) -> None:
    print("=== Dict Comprehension Examples ===")
    player_scores = {player["name"]: player["score"] for player in players}
    score_categories = {
        "high": len([player for player in players if player["score"] > 2000]),
        "medium": len(
            [
                player for player in players
                if 1800 <= player["score"] <= 2000
            ]
        ),
        "low": len([player for player in players if player["score"] < 1800]),
    }
    achievement_counts = {
        player["name"]: len(player["achievements"]) for player in players
    }

    print(f"Player scores: {player_scores}")
    print(f"Score categories: {score_categories}")
    print(f"Achievement counts: {achievement_counts}")
    print()


def set_comprehensions(players: list[dict[str, object]]) -> None:
    print("=== Set Comprehension Examples ===")
    unique_players = {player["name"] for player in players}
    unique_achievements = {
        achievement
        for player in players
        for achievement in player["achievements"]
    }
    active_regions = {
        player["region"] for player in players if player["is_active"]
    }

    print(f"Unique players: {unique_players}")
    print(f"Unique achievements: {unique_achievements}")
    print(f"Active regions: {active_regions}")
    print()


def combined_analysis(players: list[dict[str, object]]) -> None:
    top_performer = max(players, key=lambda player: player["score"])
    scores = [player["score"] for player in players]
    unique_achievements = {
        achievement
        for player in players
        for achievement in player["achievements"]
    }

    print("=== Combined Analysis ===")
    print(f"Total players: {len(players)}")
    print(f"Total unique achievements: {len(unique_achievements)}")
    print(f"Average score: {sum(scores) / len(scores)}")
    print(
        "Top performer: "
        f"{top_performer['name']} ({top_performer['score']} points, "
        f"{len(top_performer['achievements'])} achievements)"
    )


def main() -> None:
    players = [
        {
            "name": "alice",
            "score": 2300,
            "is_active": True,
            "region": "north",
            "achievements": {
                "first_kill",
                "level_10",
                "treasure_hunter",
                "speed_demon",
                "boss_slayer",
            },
        },
        {
            "name": "bob",
            "score": 1800,
            "is_active": True,
            "region": "east",
            "achievements": {
                "first_kill",
                "explorer",
                "team_player",
            },
        },
        {
            "name": "charlie",
            "score": 2150,
            "is_active": True,
            "region": "central",
            "achievements": {
                "arena_winner",
                "rich",
                "collector",
                "healer",
            },
        },
        {
            "name": "diana",
            "score": 2050,
            "is_active": False,
            "region": "north",
            "achievements": {
                "new_player",
                "boss_slayer",
                "first_kill",
            },
        },
    ]

    print("=== Game Analytics Dashboard ===")
    print()
    list_comprehensions(players)
    dict_comprehensions(players)
    set_comprehensions(players)
    combined_analysis(players)


if __name__ == "__main__":
    main()
