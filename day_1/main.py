from pathlib import Path
from more_itertools import sliding_window


def get_measurements_from_file():
    current_directory = Path(__file__).parent / "input.txt"

    with open(current_directory, "r") as input_file:
        return [int(line) for line in input_file]


def get_greater_than_previous_count(values):
    greater_than_previous_count = 0

    for sum_a, sum_b in sliding_window(values, 2):
        if sum_b > sum_a:
            greater_than_previous_count += 1

    return greater_than_previous_count


def main():
    measurements = get_measurements_from_file()
    greater_than_previous = get_greater_than_previous_count(measurements)
    print(greater_than_previous)

    sums = [sum(values) for values in sliding_window(measurements, 3)]
    greater_than_previous = get_greater_than_previous_count(sums)
    print(greater_than_previous)


if __name__ == "__main__":
    main()
