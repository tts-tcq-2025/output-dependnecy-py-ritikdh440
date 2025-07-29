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
    # Strong test - compares against properly aligned expected output
    # This test WILL FAIL and expose the formatting bug
    color_map = generate_color_map()
    output = format_color_map(color_map)
    
    expected_output = (
        " 1 | White  | Blue\n"
        " 2 | White  | Orange\n"
        " 3 | White  | Green\n"
        " 4 | White  | Brown\n"
        " 5 | White  | Slate\n"
        " 6 | Red    | Blue\n"
        " 7 | Red    | Orange\n"
        " 8 | Red    | Green\n"
        " 9 | Red    | Brown\n"
        "10 | Red    | Slate\n"
        "11 | Black  | Blue\n"
        "12 | Black  | Orange\n"
        "13 | Black  | Green\n"
        "14 | Black  | Brown\n"
        "15 | Black  | Slate\n"
        "16 | Yellow | Blue\n"
        "17 | Yellow | Orange\n"
        "18 | Yellow | Green\n"
        "19 | Yellow | Brown\n"
        "20 | Yellow | Slate\n"
        "21 | Violet | Blue\n"
        "22 | Violet | Orange\n"
        "23 | Violet | Green\n"
        "24 | Violet | Brown\n"
        "25 | Violet | Slate"
    )
    
    assert output == expected_output, "Output formatting is misaligned or incorrect!"

test_color_map_length()
test_color_map_formatting()
