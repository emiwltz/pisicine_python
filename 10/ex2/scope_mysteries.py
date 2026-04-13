from collections.abc import Callable


def mage_counter() -> Callable:
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable:
    count = 0

    def counter(add):
        nonlocal count
        count += add
        return count + initial_power

    return counter


def enchantment_factory(enchantment_type: str) -> Callable:
    pass


def memory_vault() -> dict[str, Callable]:
    pass


def main():
    counter1 = mage_counter()
    print(counter1())
    print(counter1())

    acumulator = spell_accumulator(100)
    print(acumulator(4))
    print(acumulator(4))
    print(acumulator(2))


if __name__ == "__main__":
    main()
