def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(
        artifacts,
        key=lambda artifact: artifact["power"],
        reverse=True,
    )


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    if not mages:
        return {"max_power": 0, "min_power": 0, "avg_power": 0.0}
    max_mage = max(mages, key=lambda mage: mage["power"])
    min_mage = min(mages, key=lambda mage: mage["power"])
    return {
        "max_power": max_mage["power"],
        "min_power": min_mage["power"],
        "avg_power": round(
            sum(map(lambda mage: mage["power"], mages)) / len(mages),
            2,
        ),
    }


def main() -> None:
    artifacts = [
        {"name": "Fire Staff", "power": 92, "type": "staff"},
        {"name": "Crystal Orb", "power": 85, "type": "focus"},
        {"name": "Shadow Cloak", "power": 77, "type": "armor"},
    ]
    mages = [
        {"name": "Aeris", "power": 40, "element": "wind"},
        {"name": "Drako", "power": 70, "element": "fire"},
        {"name": "Luna", "power": 55, "element": "ice"},
    ]

    print("Testing artifact sorter...")
    for artifact in artifact_sorter(artifacts):
        print(f"{artifact['name']} ({artifact['power']} power)")
    print()

    print("Testing power filter...")
    for mage in power_filter(mages, 50):
        print(f"{mage['name']} ({mage['power']} power)")
    print()

    print("Testing spell transformer...")
    print(" ".join(spell_transformer(["fireball", "heal", "shield"])))
    print()

    print("Testing mage stats...")
    print(mage_stats(mages))


if __name__ == "__main__":
    main()
