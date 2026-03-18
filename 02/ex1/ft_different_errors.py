#!/usr/bin/env python3


def garden_operations(error_type: str) -> None:
    if error_type == "ValueError":
        int("abc")
    elif error_type == "ZeroDivisionError":
        10 / 0
    elif error_type == "FileNotFoundError":
        open("missing.txt")
    elif error_type == "KeyError":
        plants = {"rose": 5, "tulip": 3}
        plants["missing_plant"]


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    print()

    print("Testing ValueError...")
    try:
        garden_operations("ValueError")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    print()

    print("Testing ZeroDivisionError...")
    try:
        garden_operations("ZeroDivisionError")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    print()

    print("Testing FileNotFoundError...")
    try:
        garden_operations("FileNotFoundError")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    print()

    print("Testing KeyError...")
    try:
        garden_operations("KeyError")
    except KeyError:
        print("Caught KeyError: 'missing_plant'")
    print()

    print("Testing multiple errors together...")
    try:
        garden_operations("KeyError")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")
    print()

    print("All error types tested successfully!")


def main() -> None:
    test_error_types()


if __name__ == "__main__":
    main()
