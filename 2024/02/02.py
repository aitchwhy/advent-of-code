import os
from typing import List


def parse_input(file_path) -> List[List]:
    reports = []
    with open(file_path, "r") as file:
        for line in file:
            levels = map(int, line.split())
            reports.append(list(levels))
    return reports


def solve_part1(reports: List[List[int]]) -> int:
    print(
        "############# part 1 : calc how many reports are SAFE i.e. lists of inc or dec"
    )

    def is_safe(report):
        if len(report) < 2:
            return True

        is_increasing = report[0] < report[1]

        # is_increasing = all(l1 < l2 for l1, l2 in zip(report, report[1:]))
        # is_decreasing = all(l1 > l2 for l1, l2 in zip(report, report[1:]))
        # if not is_increasing and not is_decreasing:
        #     return False

        if is_increasing:
            return all(
                ((l1 < l2) and (1 <= abs(l1 - l2) <= 3))
                for l1, l2 in zip(report, report[1:])
            )
        else:
            return all(
                ((l1 > l2) and (1 <= abs(l1 - l2) <= 3))
                for l1, l2 in zip(report, report[1:])
            )
            
    safe_report_count = 0
    for r in reports:
        print(r)
        if is_safe(r):
            safe_report_count += 1
    return safe_report_count


def solve_part2(left_col, right_col):
    print("############# part 2")
    # # similarity score = sum(each LEFT num * count of LEFT num in RIGHT col)
    # # NOTE: repeated numbers on LEFT just summed again

    # right_col_dict = defaultdict(int)
    # for r in right_col:
    #     right_col_dict[r] += 1

    # similarity_score = 0
    # for l in left_col:
    #     similarity_score += l * right_col_dict[l]
    # return similarity_score


def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # input_file_path = os.path.join(current_dir, "02.example")
    input_file_path = os.path.join(current_dir, "02.in")

    reports = parse_input(input_file_path)
    result_part1 = solve_part1(reports)
    print(f"count(safe reports): {result_part1}")
    # result_part2 = solve_part2(reports)
    # print(f"Sum of differences: {result_part2}")


if __name__ == "__main__":
    main()
