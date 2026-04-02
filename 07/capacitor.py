from typing import cast

from ex0.Creature import Creature
from ex0.CreatureFactory import CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.HealCapability import HealCapability
from ex1.TransformCapability import TransformCapability


def test_healing_creature(label: str, creature: Creature) -> None:
    print(label)
    print(creature.describe())
    print(creature.attack())
    print(cast(HealCapability, creature).heal())


def test_transforming_creature(label: str, creature: Creature) -> None:
    print(label)
    print(creature.describe())
    print(creature.attack())

    transformer = cast(TransformCapability, creature)
    print(transformer.transform())
    print(creature.attack())
    print(transformer.revert())


def test_healing_factory(factory: CreatureFactory) -> None:
    print("Testing Creature with healing capability")
    test_healing_creature("base:", factory.create_base())
    test_healing_creature("evolved:", factory.create_evolved())


def test_transform_factory(factory: CreatureFactory) -> None:
    print("Testing Creature with transform capability")
    test_transforming_creature("base:", factory.create_base())
    test_transforming_creature("evolved:", factory.create_evolved())


def main() -> None:
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    test_healing_factory(healing_factory)
    test_transform_factory(transform_factory)


if __name__ == "__main__":
    main()
