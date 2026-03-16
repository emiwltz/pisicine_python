import sys


def main():
    if len(sys.argv) <= 1:
        print("No arguments passed !")
    else:
        score = []
        for i in range(1, len(sys.argv)):
            try:
                score.append(int(sys.argv[i]))
            except ValueError:
                print(f"{sys.argv[i]} is not an int")
                return
        print(f"Scores processed: {score}")
        print(f"Total players: {len(score)}")
        total = 0
        for y in score:
            total = total + y
        print(f"Total scores: {total}")
        print(f"Average score: {total / len(score)}")
        print(f"Max score: {max(score)}")
        print(f"Min score: {min(score)}")
        print(f"Range: {max(score) - min(score)}")


if __name__ == "__main__":
    main()
