for x in range(10):
    if x % 2 == 0:
        continue  # Continue is used to skip the current block, and return to the "for" or "while" statement.
    print(x)

for i in range(1, 10):
    if i % 5 == 0:
        break
# print(i)
else:
    print("this is not printed because for loop is terminated because of break but because not due to fail in condition")

numbers = [951, 402, 984, 651, 360, 69, 408, 319, 601, 484, 980, 507, 725, 547, 544, 615, 83, 165, 141,
           501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941]
for i in numbers:
    if i is 575:
        break
    if i % 2 != 0:
        continue
    print(i)
