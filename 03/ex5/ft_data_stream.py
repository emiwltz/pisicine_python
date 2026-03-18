def generate_event(event_nbr: int):
    players = ("alice", "bob", "charlie")
    actions = ("killed monster", "leveled up", "found treasure", "helped a friend")
    levels = (2, 3, 12, 4, 5, 8, 15)
    for i in range(event_nbr):
        event = (
            players[i % len(players)],
            levels[i % len(levels)],
            actions[i % len(actions)],
        )
        yield event


def event_analytics(event_nbr: int):
    print("=== Game Data Stream Processor ===")
    print(f"Processing {event_nbr} game events...")
    print()
    total_event = 0
    high_level = 0
    treasure_event = 0
    level_up_event = 0
    for player, level, action in generate_event(event_nbr):
        total_event += 1
        if level >= 10:
            high_level += 1
        if action == "leveled up":
            level_up_event += 1
        elif action == "found treasure":
            treasure_event += 1
        if total_event <= 3:
            print(f"Event {total_event}: Player {player} (level {level}) {action}")
    if total_event > 3:
        print("...")
    print()
    print("=== Stream Analytics ===")
    print(f"Total events processed: {total_event}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure_event}")
    print(f"Level-up events: {level_up_event}")
    print()
    print("Memory usage: Constant (streaming)")


def fibonacci_generator(fib_nbr: int):
    a = 0
    b = 1
    for i in range(fib_nbr):
        yield a
        tmp = a
        a = b
        b = tmp + b


def fibonacci_display(fib_nbr: int):
    for i in fibonacci_generator(fib_nbr):
        print(i)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for divisor in range(2, n):
        if n % divisor == 0:
            return False
    return True


def prime_generator(count: int):
    found = 0
    candidate = 2

    while found < count:
        if is_prime(candidate):
            yield candidate
            found += 1
        candidate += 1


def prime_display(count: int):
    print(f"Prime numbers (first {count}): ", end="")
    first = True
    for prime in prime_generator(count):
        if not first:
            print(", ", end="")
        print(prime, end="")
        first = False
    print()


def main():
    event_analytics(1000)
    fibonacci_display(10)
    prime_display(10)


if __name__ == "__main__":
    main()
