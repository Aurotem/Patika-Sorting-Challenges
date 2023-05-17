numbers = [22, 27, 16, 2, 18, 6]
for number in range(len(numbers)):
    temp_number = 0
    for alt_number in range(len(numbers)):
        if numbers[alt_number] < numbers[number]:
            temp_number = numbers[number]
            numbers[number] = numbers[alt_number]
            numbers[alt_number] = temp_number
print(f"Selection Sort yöntemi ile varılan sonuç: {numbers}")

# ---------- MERGE SORT -----------
# 0. Aşama: [16, 21, 11, 8, 12, 22]
# 1. Aşama: [16, 21, 11] -- [8, 12, 22]
# 2. Aşama: [16] - [21, 11] - [8, 12] - [22]
# 3. Aşama: [16] [21] [11] [8] [12] [22]
# 4. Aşama: [11] - [16, 21] - [8, 12] - [22]
# 5. Aşama: [8, 11, 12, 16, 21, 22]

# ----------- BINARY SEARCH --------------
#                                        7
#                                    5       8
#                                  1       6    9
#                                0    3  4
#                                   2
#
