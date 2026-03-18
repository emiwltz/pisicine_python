import sys


def main() -> None:
    print("=== Player Score Analytics ===")

    if len(sys.argv) <= 1:
        print(
            "No scores provided. Usage: "
            "python3 ft_score_analytics.py <score1> <score2> ..."
        )
        return

    scores = []
    index = 1
    while index < len(sys.argv):
        try:
            scores.append(int(sys.argv[index]))
        except ValueError:
            print(f"Error: '{sys.argv[index]}' is not a valid score")
            return
        index += 1

    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / len(scores)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    main()
