def open_or_senior(data):
    return ['Senior' if age >= 55 and handi > 7 else 'Open' for (age, handi)
            in data]


if __name__ == '__main__':
    print(open_or_senior([(45, 12), (55, 21), (19, -2), (104, 20)]))
    print(open_or_senior([(59, 12), (55, -1), (12, -2), (12, 12)]))
