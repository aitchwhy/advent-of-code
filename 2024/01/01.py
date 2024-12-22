import os
from collections import defaultdict


def parse_input(file_path):
    left_col = []
    right_col = []
    with open(file_path, "r") as file:
        for line in file:
            left, right = map(int, line.split())
            left_col.append(left)
            right_col.append(right)
    return left_col, right_col


def solve_part1(left_col, right_col):
    print("############# part 1")
    left_sorted = sorted(left_col)
    right_sorted = sorted(right_col)

    diff_summed = 0
    for left, right in zip(left_sorted, right_sorted):
        print(left, right)
        diff = abs(left - right)
        print(f"Difference: {diff}")
        diff_summed += diff

    return diff_summed


def solve_part2(left_col, right_col):
    print("############# part 2")
    # similarity score = sum(each LEFT num * count of LEFT num in RIGHT col)
    # NOTE: repeated numbers on LEFT just summed again
    
    right_col_dict = defaultdict(int)
    for r in right_col:
        right_col_dict[r] += 1
        
    similarity_score = 0
    for l in left_col:
        similarity_score += l * right_col_dict[l]
    return similarity_score


def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # input_file_path = os.path.join(current_dir, '01.example')
    input_file_path = os.path.join(current_dir, "01.in")

    left_col, right_col = parse_input(input_file_path)
    result_part1 = solve_part1(left_col, right_col)
    print(f"Sum of differences: {result_part1}")
    result_part2 = solve_part2(left_col, right_col)
    print(f"Similarity scores sum: {result_part2}")


if __name__ == "__main__":
    main()
