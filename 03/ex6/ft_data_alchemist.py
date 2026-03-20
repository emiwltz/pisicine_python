import random


def main() -> None:
    players = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kevin",
        "Liam",
    ]
    capitalized_players = [player.capitalize() for player in players]
    already_capitalized_players = [
        player for player in players if player == player.capitalize()
    ]
    score_dict = {
        player: random.randint(0, 1000)
        for player in capitalized_players
    }
    score_average = round(
        sum(score_dict.values()) / len(score_dict),
        2,
    )
    high_scores = {
        player: score_dict[player]
        for player in score_dict
        if score_dict[player] > score_average
    }

    print("=== Game Data Alchemist ===")
    print()
    print(f"Initial list of players: {players}")
    print(
        "New list with all names capitalized: "
        f"{capitalized_players}"
    )
    print(
        "New list of capitalized names only: "
        f"{already_capitalized_players}"
    )
    print()
    print(f"Score dict: {score_dict}")
    print(f"Score average is {score_average:.2f}")
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
