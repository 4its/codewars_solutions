def find_uniq(arr):
    for item in set(arr):
        if arr.count(item) < len(set(arr)):
            return item


def find_uniq2(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b


list1 = [1, 1, 1, 2, 1, 1]          # Expect 2
list2 = [0, 0, 0.55, 0, 0]          # Expect 0.55
list3 = [0, 1, 1, 1, 1, 1, 1, 1]    # Expect 0
list4 = [3, 10, 3, 3, 3]            # Expect 10
# list5 =   # Expect 0.55
# list6 =   # Expect 0.55


print(find_uniq(list1))
print(find_uniq(list2))
print(find_uniq(list3))
print(find_uniq(list4))

print(find_uniq2(list1))
print(find_uniq2(list2))
print(find_uniq2(list3))
print(find_uniq2(list4))
