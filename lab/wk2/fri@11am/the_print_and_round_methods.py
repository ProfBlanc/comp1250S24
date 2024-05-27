whole_number = round(12345.67)  # 12346
one_decimal_place = round(98.765, 1) # 98.8

print(123, 1.23, True, "hi")  # each arg is sep by 1 space

print(123, 1.23, True, "hi", sep="!!!", end=".\n\t")

print(123, 1.23, True, "hi", sep="!" * 3 ,end="?")
