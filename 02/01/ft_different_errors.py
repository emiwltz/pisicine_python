#!/usr/bin/env python3


def garden_operations(action: str) -> None:
    if action == "ValueError":
        i = int("FUUU")
    elif action == "ZeroDivisionError":
        i = 23 / 0
    elif action == "FileNotFoundError":
        file = open("nude.png")
    elif action == "KeyError":
        plants = {"tulipe": 3, "rose": 5}
        plants["missing_plant"]

def test_error_types() -> None:
    try:
        garden_operations("ValueError")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    try:
        garden_operations("ZeroDivisionError")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    try:
        garden_operations("FileNotFoundError")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file")
    try:
        garden_operations("KeyError")
    except KeyError:
        print("Caught KeyError: 'missing_plant'")
    try:
        garden_operations("KeyError")
    except (ValueError, ZeroDivisionError, KeyError, FileNotFoundError):
        print("Caught one of multiple error types")


def main():
    test_error_types()


if __name__ == "__main__":
    main()
