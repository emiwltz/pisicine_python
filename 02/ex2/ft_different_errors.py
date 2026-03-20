#!/usr/bin/env python3


def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        10 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "garden" + 1


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    for operation_number in range(5):
        print(f"Testing operation {operation_number}...")
        try:
            garden_operations(operation_number)
            print("Operation completed successfully")
        except ValueError as error:
            print(f"Caught ValueError: {error}")
        except ZeroDivisionError as error:
            print(f"Caught ZeroDivisionError: {error}")
        except FileNotFoundError as error:
            print(f"Caught FileNotFoundError: {error}")
        except TypeError as error:
            print(f"Caught TypeError: {error}")

    print()
    print("Testing multiple catches together...")
    try:
        garden_operations(3)
    except (
        ValueError,
        ZeroDivisionError,
        FileNotFoundError,
        TypeError,
    ) as error:
        print(f"Caught multiple error types at once: {error}")

    print()
    print("All error types tested successfully!")


def main() -> None:
    test_error_types()


if __name__ == "__main__":
    main()
