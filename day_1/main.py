from pathlib import Path
from more_itertools import sliding_window


def get_measurements_from_file():
    current_directory = Path(__file__).parent / "input.txt"

    with open(current_directory, "r") as input_file:
        return [int(line) for line in input_file]


def compare_adjacent_values(values):
    greater_than_previous = 0

    for sum_a, sum_b in sliding_window(values, 2):
        if sum_b > sum_a:
            greater_than_previous += 1

    return greater_than_previous


def main():
    measurements = get_measurements_from_file()
    greater_than_previous = compare_adjacent_values(measurements)
    print(greater_than_previous)

    sums = [sum(values) for values in sliding_window(measurements, 3)]
    greater_than_previous = compare_adjacent_values(sums)
    print(greater_than_previous)


if __name__ == "__main__":
    main()
