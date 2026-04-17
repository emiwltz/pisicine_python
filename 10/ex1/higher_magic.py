from collections.abc import Callable


Spell = Callable[[str, int], str]
Condition = Callable[[str, int], bool]


def spell_combiner(
    spell1: Spell,
    spell2: Spell,
) -> Callable[[str, int], tuple[str, str]]:
    def combined(target: str, power: int) -> tuple[str, str]:
        res1 = spell1(target, power)
        res2 = spell2(target, power)
        return res1, res2

    return combined


def power_amplifier(base_spell: Spell, multiplier: int) -> Spell:
    def amplified_spell(target: str, power: int) -> str:
        new_power = power * multiplier
        return base_spell(target, new_power)

    return amplified_spell


def conditional_caster(condition: Condition, spell: Spell) -> Spell:
    def new_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"

    return new_spell


def spell_sequence(spells: list[Spell]) -> Callable[[str, int], list[str]]:
    def spell_list(target: str, power: int) -> list[str]:
        all_spells: list[str] = []
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
    _ = target
    return power >= 10


def main() -> None:
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    combined_result = combined("Dragon", 10)
    print(
        "Combined spell result: "
        f"{combined_result[0]} | {combined_result[1]}"
    )
    print()

    print("Testing power amplifier...")
    amplified = power_amplifier(fireball, 3)
    print(f"Original: {fireball('Dragon', 10)}")
    print(f"Amplified: {amplified('Dragon', 10)}")
    print()

    print("Testing conditional caster...")
    conditional_spell = conditional_caster(can_cast, fireball)
    print(f"Valid cast: {conditional_spell('Dragon', 15)}")
    print(f"Invalid cast: {conditional_spell('Dragon', 5)}")
    print()

    print("Testing spell sequence...")
    sequence = spell_sequence([fireball, heal])
    print(sequence("Dragon", 10))


if __name__ == "__main__":
    main()
