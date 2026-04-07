from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int):
        res1 = spell1(target, power)
        res2 = spell2(target, power)
        return (res1, res2)

    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplifer(target, power):
        result = power * multiplier
        return base_spell(target, result)

    return amplifer


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def new_spell(target, power):
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return new_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    spell_list = []
    def


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Attack {target} for {power} damage"


def main():
    combined = spell_combiner(fireball, heal)
    print(combined("Dragon", 10))
    amplifed = power_amplifier(fireball, 10)
    print(amplifed("Dragon", 10))


if __name__ == "__main__":
    main()
