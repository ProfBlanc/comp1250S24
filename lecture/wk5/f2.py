names = ["joe", "bob", "mary"]
nums = [1, 10, 100]

merged = names + nums

print(merged)

repeated = names * 3

print(repeated)

nums.extend(names)  # arg = another list (tuple, set, other iterable)

print(nums)

merged.pop(5)  # remove from an index

copied = merged.copy()

print(merged, copied)

merged.append("hello")

print(merged, copied)

mystery = merged  # NOT copying values => creating a pointer. Pointer = shortcut

merged.append(1234)

print(mystery, merged)

mystery.insert(0, -987)

print(mystery, merged)

copy_using_slicing = mystery[0:len(mystery)]  # copy values w/o using copy() method

if 1234 in merged:
    position = merged.index(1234)  # if value does not exist => runtime error
    print(position)