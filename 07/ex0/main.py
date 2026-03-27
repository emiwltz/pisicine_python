from CreatureCard import CreatureCard


def main():
    test = CreatureCard("test", 3, "rare", 4, 5)
    print(test.get_card_info())


if __name__ == "__main__":
    main()
