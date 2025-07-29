def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            print(f'{i * 5 + j + 1} | {major} | {minor}')  # Bug: numbering starts at 1 instead of 0
    return len(major_colors) * len(minor_colors)


result = print_color_map()
assert(result == 25)
print("All is well (maybe!)")
