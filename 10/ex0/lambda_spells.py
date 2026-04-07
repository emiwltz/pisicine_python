
def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(
        artifacts,
        key=lambda artifact: artifact["power"],
        reverse=True
    )


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(
        lambda mage: mage["power"] >= min_power,
        mages
    ))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(
        lambda spell: "* " + spell + " *",
        spells
    ))


def mage_stats(mages: list[dict]) -> dict:
    return {
        "max_power": max(mages, key=lambda mage: mage["power"]),
        "min_power": min(mages, key=lambda mage: mage["power"]),
        "avg_power": round(
            sum(map(lambda mage: mage["power"], mages)) / len(mages),
            2)
    }


def main():
    print("Testing artifact sorter...")
    mages = [
        {"name": "Aeris", "power": 40, "element": "wind"},
        {"name": "Drako", "power": 70, "element": "fire"},
        {"name": "Luna", "power": 55, "element": "ice"},
    ]
    avg_mages = mage_stats(mages)
    print(avg_mages)


if __name__ == "__main__":
    main()
