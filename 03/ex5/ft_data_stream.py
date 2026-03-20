import random
import typing


PLAYERS = ["alice", "bob", "charlie", "dylan"]
ACTIONS = [
    "run",
    "eat",
    "sleep",
    "grab",
    "move",
    "climb",
    "swim",
    "release",
    "use",
]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        yield (
            random.choice(PLAYERS),
            random.choice(ACTIONS),
        )


def consume_event(
    events: list[tuple[str, str]],
) -> typing.Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        event_index = random.randrange(len(events))
        yield events.pop(event_index)


def main() -> None:
    print("=== Game Data Stream Processor ===")

    event_generator = gen_event()
    for event_index in range(1000):
        event = next(event_generator)
        print(
            f"Event {event_index}: Player {event[0]} "
            f"did action {event[1]}"
        )

    events: list[tuple[str, str]] = []
    for _ in range(10):
        events.append(next(event_generator))

    print(f"Built list of 10 events: {events}")
    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")


if __name__ == "__main__":
    main()
