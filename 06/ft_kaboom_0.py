import alchemy.grimoire


def main() -> None:
    record = alchemy.grimoire.light_spell_record(
        "Fantasy",
        "Earth, wind and fire",
    )
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    print(f"Testing record light spell: {record}")


if __name__ == "__main__":
    main()
