import math


def parse_coordinates(string: str) -> tuple[int, int, int] | None:
    coordinates = string.split(",")
    if len(coordinates) != 3:
        print("Error parsing coordinates: expected 3 comma-separated values")
        return None

    try:
        x_value = int(coordinates[0])
        y_value = int(coordinates[1])
        z_value = int(coordinates[2])
    except ValueError as error:
        print(f"Error parsing coordinates: {error}")
        print(
            "Error details - Type: "
            f"{error.__class__.__name__}, Args: {error.args}"
        )
        return None

    return tuple([x_value, y_value, z_value])


def distance_from_origin(position: tuple[int, int, int]) -> float:
    x_value, y_value, z_value = position
    return math.sqrt((x_value ** 2) + (y_value ** 2) + (z_value ** 2))


def main() -> None:
    print("=== Game Coordinate System ===")
    print()

    start_position = tuple([10, 20, 5])
    print(f"Position created: {start_position}")
    print(
        "Distance between (0, 0, 0) and "
        f"{start_position}: {distance_from_origin(start_position):.2f}"
    )
    print()

    valid_string = "3,4,0"
    print(f'Parsing coordinates: "{valid_string}"')
    parsed_position = parse_coordinates(valid_string)
    if parsed_position is not None:
        print(f"Parsed position: {parsed_position}")
        print(
            "Distance between (0, 0, 0) and "
            f"{parsed_position}: {distance_from_origin(parsed_position)}"
        )
    print()

    invalid_string = "abc,def,ghi"
    print(f'Parsing invalid coordinates: "{invalid_string}"')
    parse_coordinates(invalid_string)
    print()

    if parsed_position is not None:
        print("Unpacking demonstration:")
        x_value, y_value, z_value = parsed_position
        print(f"Player at x={x_value}, y={y_value}, z={z_value}")
        print(f"Coordinates: X={x_value}, Y={y_value}, Z={z_value}")


if __name__ == "__main__":
    main()
