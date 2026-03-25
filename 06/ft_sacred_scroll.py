import alchemy


def main():

    print("=== Sacred Scroll Mastery ===")
    print()

    print("Testing direct module access:")
    print(alchemy.elements.create_fire())
    print(alchemy.elements.create_water())
    print(alchemy.elements.create_earth())
    print(alchemy.elements.create_air())

    print()

    print("Testing package-level access (controlled by __init__.py):")
    try:
        print(alchemy.create_fire())
    except AttributeError as e:
        print(e)

    try:
        print(alchemy.create_water())
    except AttributeError as e:
        print(e)

    try:
        print(alchemy.create_earth())
    except AttributeError as e:
        print(e)

    try:
        print(alchemy.create_air())
    except AttributeError as e:
        print(e)

    print()

    print("Package metadata:")
    print(alchemy.__version__)
    print(alchemy.__author__)


if __name__ == "__main__":
    main()
