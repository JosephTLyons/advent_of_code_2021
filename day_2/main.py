import math
from collections import Counter
from pathlib import Path


def get_directions_from_file():
    current_directory = Path(__file__).parent / "input.txt"

    with open(current_directory, "r") as input_file:
        directions = [line.split() for line in input_file]
        return [(direction, int(distance)) for direction, distance in directions]


def main():
    directions = get_directions_from_file()
    counter = Counter()

    for direction, distance in directions:
        match direction:
            case "forward":
                counter["horizontal"] += distance
                counter["vertical"] += counter["aim"] * distance
            case "down":
                counter["aim"] += distance
            case "up":
                counter["aim"] -= distance

    print(counter["horizontal"] * counter["vertical"])


if __name__ == "__main__":
    main()
