def list_comprehensions(players: list):
    print("=== List Comprehension Examples ===")
    high_scorer = [x.get("name") for x in players if x.get("score") > 200]
    print(f"High scorers (>2000): {high_scorer}")
    score_doubled = [x.get("score") * 2 for x in players]
    print(f"Scores doubled: {score_doubled}")
    active_player = [x.get("name") for x in players if x.get("is_active") == 1]
    print(f"Active players: {active_player}")
    print()


def dict_comprehensions(players: list):
    print("=== Dict Comprehension Examples ===")
    player_scores = {x.get("name"): x.get("score") for x in players}
    print(f"Player scores: {player_scores}")


def set_comprehensions(players: list):
    pass


def main():
    alice = {
        "name": "alice",
        "score": 250,
        "is_active": True,
        "region": "Gard",
        "achievements": {"first_kill", "rich", "new_player"},
    }
    bob = {
        "name": "bob",
        "score": 180,
        "is_active": False,
        "region": "Lyon",
        "achievements": {"new_player", "explorer"},
    }
    charlie = {
        "name": "charlie",
        "score": 420,
        "is_active": False,
        "region": "Paris",
        "achievements": {"first_kill", "arena_winner", "rich"},
    }
    diana = {
        "name": "diana",
        "score": 310,
        "is_active": True,
        "region": "Marseille",
        "achievements": {"healer", "team_player", "new_player"},
    }
    players = [alice, bob, charlie, diana]
    print("=== Game Analytics Dashboard ===")
    print()
    list_comprehensions(players)
    dict_comprehensions(players)
    set_comprehensions(players)


if __name__ == "__main__":
    main()
