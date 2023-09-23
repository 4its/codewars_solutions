def circle_area(r):
    PI = 3.14
    if r > 0:
        return PI * r**2
    raise ValueError


if __name__ == '__main__':
    print(circle_area(1))
    print(circle_area(-1))