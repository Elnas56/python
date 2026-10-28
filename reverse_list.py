def reverse_list(items):
    keep = []
    for item in items:
        keep.insert(0, item)
    return keep    

print(reverse_list([1, 2, 3, 4]))
print(reverse_list(["a", "b", "c"]))

