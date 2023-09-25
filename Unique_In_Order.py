"""
Unique In Order
Implement the function unique_in_order which takes as argument a sequence and
returns a list of items without any elements with the same value next to each
other and preserving the original order of elements.

For example:
unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]
"""


def unique_in_order(sequence):
    result = []
    for item in sequence:
        if not result or item != result[-1]:
            result.append(item)
    return result


"""Should work with empty sequence"""
print(unique_in_order(""))  # []
print(unique_in_order([]))  # []
print(unique_in_order(()))  # []
"""Should work with single element sequence"""
print(unique_in_order("A"))   # ["A"]
print(unique_in_order(["A"]))   # ["A"]
print(unique_in_order(("A",)))   # ["A"]
"""Should reduce duplicates"""
print(unique_in_order("AA"))   # ["A"]
print(unique_in_order("AAAABBBCCDAABBB"))   # ["A", "B", "C", "D", "A", "B"]
"""Should be case-sensitive"""
print(unique_in_order("ABBCcA"))   # ["A", "B", "C", "c", "A"]
"""Should work with different element types"""
print(unique_in_order([1, 2, 3, 3, -1]))   # [1, 2, 3, -1]
print(unique_in_order(["a", "b", "b", "a"]))   # ["a", "b", "a"]
