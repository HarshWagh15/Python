numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
count_positive_numbers=0

for num in numbers:
    if num > 0:
        count_positive_numbers += 1
print("Total positive numbers are:",count_positive_numbers)