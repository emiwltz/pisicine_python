#!/usr/bin/env python3


def check_temperature(temp_str: str) -> int | None:
    try:
        nbr = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return
    if nbr < 0:
        print(f"Error: temperature {nbr}°C is too cold for plants")
    elif nbr > 40:
        print(f"Error: temperature {nbr}°C is too hot for plants")
    else:
        print(f"temperature {nbr}°C is perfect for plants")
        return nbr


def check_temperature_input() -> None:
    temp1 = "21"
    temp2 = "-3515"
    temp3 = "0"
    temp4 = "def"
    temp5 = "54DS"
    check_temperature(temp1)
    check_temperature(temp2)
    check_temperature(temp3)
    check_temperature(temp4)
    check_temperature(temp5)


def main():
    check_temperature_input()


if __name__ == "__main__":
    main()
