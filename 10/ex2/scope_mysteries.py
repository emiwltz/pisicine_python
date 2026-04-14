from collections.abc import Callable


def mage_counter() -> Callable:
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable:
    total_power = initial_power

    def counter(add):
        nonlocal total_power
        total_power += add
        return total_power

    return counter


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchantment_maker(item):
        return f"{enchantment_type} {item}"

    return enchantment_maker


def memory_vault() -> dict[str, Callable]:
    vault = {}

    def store(key, value):
        vault[key] = value

    def recall(key):
        if key in vault:
            return vault[key]
        return "Memory not found"

    return {"store": store, "recall": recall}


def main():
    counter1 = mage_counter()
    print(counter1())
    print(counter1())

    acumulator = spell_accumulator(100)
    print(acumulator(4))
    print(acumulator(4))
    print(acumulator(2))

    factory = enchantment_factory("Fire")
    print(factory("sword"))

    vault = memory_vault()
    vault["store"]("secret", 42)
    print(vault["recall"]("secret"))
    print(vault["recall"]("unknown"))


if __name__ == "__main__":
    main()
