from typing import Generator


def generate_event(
    event_count: int,
) -> Generator[tuple[str, int, str], None, None]:
    players = ("alice", "bob", "charlie")
    actions = (
        "killed monster",
        "found treasure",
        "leveled up",
        "helped a friend",
    )
    levels = (5, 12, 8, 15, 3, 10, 7)

    for index in range(event_count):
        yield (
            players[index % len(players)],
            levels[index % len(levels)],
            actions[index % len(actions)],
        )


def event_analytics(event_count: int) -> None:
    print("=== Game Data Stream Processor ===")
    print()
    print(f"Processing {event_count} game events...")
    print()

    total_events = 0
    high_level = 0
    treasure_events = 0
    level_up_events = 0

    for player, level, action in generate_event(event_count):
        total_events += 1
        if level >= 10:
            high_level += 1
        if action == "found treasure":
            treasure_events += 1
        if action == "leveled up":
            level_up_events += 1
        if total_events <= 3:
            print(
                f"Event {total_events}: Player {player} "
                f"(level {level}) {action}"
            )

    if total_events > 3:
        print("...")

    print()
    print("=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}")
    print()
    print("Memory usage: Constant (streaming)")


def fibonacci_generator(count: int) -> Generator[int, None, None]:
    first_value = 0
    second_value = 1

    for _ in range(count):
        yield first_value
        first_value, second_value = second_value, first_value + second_value


def is_prime(number: int) -> bool:
    if number < 2:
        return False

    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True


def prime_generator(count: int) -> Generator[int, None, None]:
    found = 0
    candidate = 2

    while found < count:
        if is_prime(candidate):
            yield candidate
            found += 1
        candidate += 1


def print_series(title: str, values: Generator[int, None, None]) -> None:
    print(title, end="")
    first_value = True
    for value in values:
        if not first_value:
            print(", ", end="")
        print(value, end="")
        first_value = False
    print()


def main() -> None:
    event_analytics(1000)
    print()
    print("=== Generator Demonstration ===")
    print_series(
        "Fibonacci sequence (first 10): ",
        fibonacci_generator(10),
    )
    print_series("Prime numbers (first 5): ", prime_generator(5))


if __name__ == "__main__":
    main()
