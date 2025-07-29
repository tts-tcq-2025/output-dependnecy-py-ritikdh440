def generate_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    color_map = []
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            number = i * 5 + j + 1
            color_map.append((number, major, minor))
    return color_map

def format_color_map(color_map):
    # BUG: formatting is inconsistent and columns are NOT aligned properly
    lines = []
    for number, major, minor in color_map:
        # No padding, so misalignment exists
        lines.append(f'{number} | {major} | {minor}')
    return "\n".join(lines)

def print_color_map():
    color_map = generate_color_map()
    output = format_color_map(color_map)
    print(output)
    return len(color_map)


def test_color_map_length():
    # Weak test - only counts lines, will pass falsely
    assert print_color_map() == 25

def test_color_map_formatting():
    color_map = generate_color_map()
    output = format_color_map(color_map)

    # Generate expected output with proper alignment
    expected_lines = []
    for number, major, minor in color_map:
        expected_lines.append(f'{str(number).rjust(2)} | {major.ljust(7)} | {minor}')
    
    expected_output = "\n".join(expected_lines)

    assert output == expected_output, "Output formatting is misaligned or incorrect!"


test_color_map_length()
test_color_map_formatting()
