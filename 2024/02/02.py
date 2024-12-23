from dataclasses import dataclass
from typing import List

# def process_input(content):
#     lines = content.strip().split("\n")
#     sequences = []
#     for line in lines:
#         sequence = [int(x) for x in line.split()]
#         sequences.append(sequence)
#     return sequences


# def is_sequence_safe(sequence):
#     if len(sequence) < 2:
#         return True

#     differences = [sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1)]

#     # Check if all differences are in the same direction
#     all_increasing = all(diff > 0 for diff in differences)
#     all_decreasing = all(diff < 0 for diff in differences)

#     # Check if differences are between 1 and 3
#     valid_differences = all(1 <= abs(diff) <= 3 for diff in differences)

#     return (all_increasing or all_decreasing) and valid_differences


@dataclass
class Report:
    levels: List[int]

    def is_safe(self):
        if len(self.levels) < 2:
            return True
        diffs = [(n - p) for p, n in zip(self.levels, self.levels[1:])]
        all_inc = all(d > 0 for d in diffs)
        all_dec = all(d < 0 for d in diffs)
        all_valid_diffs = all(1 <= abs(d) <= 3 for d in diffs)
        return (all_inc or all_dec) and all_valid_diffs

    def is_safe_with_dampener(self):
        if self.is_safe():
            return True

        # check safe with one level removed (dampener)
        for i in range(len(self.levels)):
            dampened_levels = self.levels[:i] + self.levels[i + 1:]
            if Report(dampened_levels).is_safe():
                return True
        return False


def parse_input(file_path) -> List[Report]:
    reports = []
    with open(file_path, "r") as f:
        for levels in f:
            r = Report([int(x) for x in levels.strip().split()])
            reports.append(r)
    return reports


# def is_safe_with_dampener(sequence):
#     # First check if sequence is already safe
#     if is_sequence_safe(sequence):
#         return True

#     # Try removing each number once and check if resulting sequence is safe
#     for i in range(len(sequence)):
#         new_sequence = sequence[:i] + sequence[i + 1 :]
#         if is_sequence_safe(new_sequence):
#             return True

#     return False


# Read the file content
in_file = "/Users/hank/src/advent-of-code/2024/02/02.in"
example_file = "/Users/hank/src/advent-of-code/2024/02/02.example"

# reports = parse_input(example_file)
reports = parse_input(in_file)
# parse_input(in_file)

# Part 1: Count safe sequences
safe_count = [r.is_safe() for r in reports].count(True)
print(f"Part 1 Answer: {safe_count}")

# # Part 2: Count safe sequences with Problem Dampener

safe_count_with_dampener = [r.is_safe_with_dampener() for r in reports].count(True)
print(f"Part 2 Answer: {safe_count_with_dampener}")

##################################

# import os


# def parse_input(file_path) -> List[List]:
#     reports = []
#     with open(file_path, "r") as file:
#         for line in file:
#             levels = map(int, line.split())
#             reports.append(list(levels))
#     return reports


# def is_safe(report):
#     if len(report) < 2:
#         return True

#     is_increasing = report[0] < report[1]

#     # is_increasing = all(l1 < l2 for l1, l2 in zip(report, report[1:]))
#     # is_decreasing = all(l1 > l2 for l1, l2 in zip(report, report[1:]))
#     # if not is_increasing and not is_decreasing:
#     #     return False

#     if is_increasing:
#         return all(
#             ((l1 < l2) and (1 <= abs(l1 - l2) <= 3))
#             for l1, l2 in zip(report, report[1:])
#         )
#     else:
#         return all(
#             ((l1 > l2) and (1 <= abs(l1 - l2) <= 3))
#             for l1, l2 in zip(report, report[1:])
#         )


# def solve_part1(reports: List[List[int]]) -> int:
#     print(
#         "############# part 1 : calc how many reports are SAFE i.e. lists of inc or dec"
#     )

#     safe_report_count = 0
#     for r in reports:
#         # print(r)
#         if is_safe(r):
#             safe_report_count += 1
#     return safe_report_count


# def solve_part2(reports: List[List[int]]) -> int:
#     print("############# part 2")
#     # # similarity score = sum(each LEFT num * count of LEFT num in RIGHT col)
#     # # NOTE: repeated numbers on LEFT just summed again

#     safe_report_count = 0
#     for r in reports:
#         # print(r)
#         if (
#             is_safe(r)
#             or is_safe([r[0], r[1], r[2], r[3]])
#             or is_safe([r[0], r[1], r[2], r[4]])
#             or is_safe([r[0], r[1], r[3], r[4]])
#             or is_safe([r[0], r[2], r[3], r[4]])
#             or is_safe([r[1], r[2], r[3], r[4]])
#         ):
#             safe_report_count += 1
#     return safe_report_count


# def main():
#     current_dir = os.path.dirname(os.path.abspath(__file__))
#     # input_file_path = os.path.join(current_dir, "02.example")
#     input_file_path = os.path.join(current_dir, "02.in")

#     reports = parse_input(input_file_path)
#     result_part1 = solve_part1(reports)
#     print(f"count(safe reports): {result_part1}")
#     result_part2 = solve_part2(reports)
#     print(f"count(safe reports with ONE allowed omit level): {result_part2}")


# if __name__ == "__main__":
#     main()
