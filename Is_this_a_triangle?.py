"""Is this a triangle?"""


def is_triangle(a, b, c) -> bool:
    return (a < b + c) and (b < a + c) and (c < a + b)


print(is_triangle(1, 2, 2))
print(is_triangle(7, 2, 2))
print(is_triangle(1, 2, 3))
print(is_triangle(1, 3, 2))
print(is_triangle(3, 1, 2))
print(is_triangle(5, 1, 2))
print(is_triangle(1, 2, 5))
print(is_triangle(2, 5, 1))
print(is_triangle(4, 2, 3))
