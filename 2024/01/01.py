import os

# input is 2 columns of ints
# match left column with right column IN ASCENDING ORDER


# Solve : Sort left col. Sort right col. Match numbers, print pairs, calc diff. Sum diffs

# TODO: parse input

def parse_input(file_path):
    left_col = []
    right_col = []
    with open(file_path, 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            left_col.append(left)
            right_col.append(right)
    return left_col, right_col

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))
# input_file_path = os.path.join(current_dir, '01.example')
input_file_path = os.path.join(current_dir, '01.in')
left_col, right_col = parse_input(input_file_path)

# print(left_col)
# print(right_col)

left_col.sort()
right_col.sort()


# print(left_col)
# print(right_col)

zipped = zip(left_col, right_col)
diff_summed = 0
for left, right in zipped:
    print(left, right)
    diff = abs(left - right)
    print(f"Difference: {diff}")
    diff_summed += diff
    
print(f"Sum of differences: {diff_summed}")


# TODO: calculate diffs + return sum
