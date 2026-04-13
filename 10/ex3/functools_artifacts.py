from collections.abc import Callable
from typing import Any
import operator
from functools import reduce, partial, lru_cache, singledispatch


def spell_reducer(spells: list[int], operation: str) -> int:
    operations = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min,
    }
    if not spells:
        return 0
    try:
        result = reduce(operations[operation], spells)
        return result
    except KeyError:
        return "error: unknown operation"


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"{power}pv attack of type: {element} on {target}"


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    special1 = partial(base_enchantment, 50, "fire")
    special2 = partial(base_enchantment, 50, "ice")
    special3 = partial(base_enchantment, 50, "lightning")

    return {
        "fire": special1,
        "ice": special2,
        "lightning": special3,
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n must be >= 0")
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
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


def main():
    lst = [1, 2, 3, 4]
    print("Testing spell reducer...")
    print("Add:", spell_reducer(lst, "add"))
    print("Multiply:", spell_reducer(lst, "multiply"))
    print("Max:", spell_reducer(lst, "max"))
    print("Min:", spell_reducer(lst, "min"))
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
