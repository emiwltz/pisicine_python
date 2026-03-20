import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        coordinates_input = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )
        coordinates = coordinates_input.split(",")
        if len(coordinates) != 3:
            print("Invalid syntax")
            continue

        values: list[str] = []
        for coordinate in coordinates:
            values.append(coordinate.strip())

        parsed_values: list[float] = []
        has_error = False
        for value in values:
            try:
                parsed_values.append(float(value))
            except ValueError as error:
                print(f"Error on parameter '{value}': {error}")
                has_error = True
                break

        if has_error:
            continue
        return (
            parsed_values[0],
            parsed_values[1],
            parsed_values[2],
        )


def distance_to_center(position: tuple[float, float, float]) -> float:
    x_value, y_value, z_value = position
    return math.sqrt((x_value ** 2) + (y_value ** 2) + (z_value ** 2))


def distance_between(
    start_position: tuple[float, float, float],
    end_position: tuple[float, float, float],
) -> float:
    return math.sqrt(
        ((end_position[0] - start_position[0]) ** 2)
        + ((end_position[1] - start_position[1]) ** 2)
        + ((end_position[2] - start_position[2]) ** 2)
    )


def main() -> None:
    print("=== Game Coordinate System ===")
    print()

    print("Get a first set of coordinates")
    first_position = get_player_pos()
    print(f"Got a first tuple: {first_position}")
    print()

    print(
        f"It includes: X={first_position[0]}, "
        f"Y={first_position[1]}, Z={first_position[2]}"
    )
    first_distance = round(distance_to_center(first_position), 4)
    print(f"Distance to center: {first_distance:.4f}")
    print()

    print("Get a second set of coordinates")
    second_position = get_player_pos()
    second_distance = round(
        distance_between(first_position, second_position),
        4,
    )
    print(
        "Distance between the 2 sets of coordinates: "
        f"{second_distance:.4f}"
    )


if __name__ == "__main__":
    main()
