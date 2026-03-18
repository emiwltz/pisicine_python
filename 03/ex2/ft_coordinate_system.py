import sys
import math


def parsing(string: str):
    coordinates = string.split(",")
    for i in range(len(coordinates)):
        try:
            coordinates[i] = int(coordinates[i])
        except ValueError:
            print(f"{i} is not an int")
            return
    coordinates = tuple(coordinates)
    print(coordinates)
    start = (0, 0, 0)
    x1, y1, z1 = start
    x2, y2, z2 = coordinates
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    print(distance)


def main():
    if len(sys.argv) <= 1:
        print("No argments passed")
    else:
        parsing(sys.argv[1])


if __name__ == "__main__":
    main()
