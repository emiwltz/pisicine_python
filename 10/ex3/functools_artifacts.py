from collections.abc import Callable
import functools
import operator
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    operations: dict[str, Callable[[int, int], int]] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min,
    }
    if not spells:
        return 0
    if operation not in operations:
        raise ValueError(f"Unknown operation: {operation}")
    return functools.reduce(operations[operation], spells)


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"{element.title()} enchantment strikes {target} with {power} power"


def partial_enchanter(
    base_enchantment: Callable[[int, str, str], str],
) -> dict[str, Callable[[str], str]]:
    special1 = functools.partial(base_enchantment, 50, "fire")
    special2 = functools.partial(base_enchantment, 50, "ice")
    special3 = functools.partial(base_enchantment, 50, "lightning")

    return {
        "fire": special1,
        "ice": special2,
        "lightning": special3,
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n must be >= 0")
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def dispatch(spell: Any) -> str:
        return "Unknown spell type"

    @dispatch.register
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatch.register
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @dispatch.register
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return dispatch


def main() -> None:
    spell_powers = [10, 20, 30, 40]

    print("Testing spell reducer...")
    print("Sum:", spell_reducer(spell_powers, "add"))
    print("Product:", spell_reducer(spell_powers, "multiply"))
    print("Max:", spell_reducer(spell_powers, "max"))
    print("Min:", spell_reducer(spell_powers, "min"))
    print()

    print("Testing partial enchanter...")
    enchants = partial_enchanter(base_enchantment)
    print(enchants["fire"]("Dragon"))
    print(enchants["ice"]("Goblin"))
    print(enchants["lightning"]("Wizard"))
    print()

    print("Testing memoized fibonacci...")
    print("Fib(0):", memoized_fibonacci(0))
    print("Fib(1):", memoized_fibonacci(1))
    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(15):", memoized_fibonacci(15))
    print("Cache info:", memoized_fibonacci.cache_info())
    print()

    print("Testing spell dispatcher...")
    dispatch = spell_dispatcher()
    print(dispatch(42))
    print(dispatch("fireball"))
    print(dispatch(["fireball", "heal", "shield"]))
    print(dispatch(3.14))


if __name__ == "__main__":
    main()
