#!/usr/bin/env python3


def check_temperature(temp_str: str) -> int | None:
    try:
        temperature = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None

    if temperature < 0:
        print(f"Error: {temperature}°C is too cold for plants (min 0°C)")
        return None
    if temperature > 40:
        print(f"Error: {temperature}°C is too hot for plants (max 40°C)")
        return None

    print(f"Temperature {temperature}°C is perfect for plants!")
    return temperature


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===")
    print()

    for value in ["25", "abc", "100", "-50"]:
        print(f"Testing temperature: {value}")
        check_temperature(value)
        print()

    print("All tests completed - program didn't crash!")


def main() -> None:
    test_temperature_input()


if __name__ == "__main__":
    main()
