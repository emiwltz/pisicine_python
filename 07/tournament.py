from ex0 import AquaFactory, FlameFactory
from ex0.CreatureFactory import CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    AggressiveStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
    NormalStrategy,
)
from ex2.BattleStrategy import BattleStrategy

Opponent = tuple[CreatureFactory, BattleStrategy]


def get_factory_label(factory: CreatureFactory) -> str:
    labels = {
        "AquaFactory": "Aquabub",
        "FlameFactory": "Flameling",
        "HealingCreatureFactory": "Healing",
        "TransformCreatureFactory": "Transform",
    }
    return labels.get(factory.__class__.__name__, factory.__class__.__name__)


def get_strategy_label(strategy: BattleStrategy) -> str:
    name = strategy.__class__.__name__
    return name.removesuffix("Strategy")


def summarize_opponents(opponents: list[Opponent]) -> str:
    summary_parts = []

    for factory, strategy in opponents:
        part = f"({get_factory_label(factory)}+{get_strategy_label(strategy)})"
        summary_parts.append(part)

    return f"[ {', '.join(summary_parts)} ]"


def battle(opponents: list[Opponent]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for index, (first_factory, first_strategy) in enumerate(opponents):
        for second_factory, second_strategy in opponents[index + 1:]:
            first_creature = first_factory.create_base()
            second_creature = second_factory.create_base()

            print("* Battle *")
            print(first_creature.describe())
            print("vs.")
            print(second_creature.describe())
            print("now fight!")

            try:
                first_actions = first_strategy.act(first_creature)
                second_actions = second_strategy.act(second_creature)
            except InvalidStrategyError as error:
                print(f"Battle error, aborting tournament: {error}")
                return

            for action in first_actions:
                print(action)
            for action in second_actions:
                print(action)


def run_tournament(title: str, opponents: list[Opponent]) -> None:
    print(title)
    print(summarize_opponents(opponents))
    battle(opponents)


def main() -> None:
    normal_strategy = NormalStrategy()
    aggressive_strategy = AggressiveStrategy()
    defensive_strategy = DefensiveStrategy()

    tournament_zero = [
        (FlameFactory(), normal_strategy),
        (HealingCreatureFactory(), defensive_strategy),
    ]
    tournament_one = [
        (FlameFactory(), aggressive_strategy),
        (HealingCreatureFactory(), defensive_strategy),
    ]
    tournament_two = [
        (AquaFactory(), normal_strategy),
        (HealingCreatureFactory(), defensive_strategy),
        (TransformCreatureFactory(), aggressive_strategy),
    ]

    run_tournament("Tournament 0 (basic)", tournament_zero)
    print()
    run_tournament("Tournament 1 (error)", tournament_one)
    print()
    run_tournament("Tournament 2 (multiple)", tournament_two)


if __name__ == "__main__":
    main()
