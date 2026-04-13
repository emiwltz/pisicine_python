from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int):
        res1 = spell1(target, power)
        res2 = spell2(target, power)
        return (res1, res2)

    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplifer(target, power):
        new_power = power * multiplier
        return base_spell(target, new_power)

    return amplifer


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def new_spell(target, power):
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"

    return new_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    def spell_list(target, power):
        all_spells = []
        for spell in spells:
            spell_result = spell(target, power)
            all_spells.append(spell_result)
        return all_spells

    return spell_list


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Attack {target} for {power} damage"


def can_cast(target: str, power: int) -> bool:
    return power >= 10


def main():
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    print(combined("Dragon", 10))
    print()

    print("Testing power amplifier...")
    amplified = power_amplifier(fireball, 3)
    print(amplified("Dragon", 10))
    print()

    print("Testing conditional caster...")
    conditional_spell = conditional_caster(can_cast, fireball)
    print(conditional_spell("Dragon", 15))
    print(conditional_spell("Dragon", 5))
    print()

    print("Testing spell sequence...")
    sequence = spell_sequence([fireball, heal])
    print(sequence("Dragon", 10))


if __name__ == "__main__":
    main()
