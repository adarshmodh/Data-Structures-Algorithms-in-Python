def permutationStep(num: int) -> int:
    digits = list(str(num))
    n = len(digits)

    # Step 1: Find the pivot (first digit from right that is smaller than its next digit)
    i = n - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1

    if i == -1:
        return -1  # No larger permutation possible

    # Step 2: Find the smallest digit on right of pivot that's bigger than pivot
    j = n - 1
    while digits[j] <= digits[i]:
        j -= 1

    # Step 3: Swap pivot and this digit
    digits[i], digits[j] = digits[j], digits[i]

    # Step 4: Reverse the suffix
    digits[i + 1:] = reversed(digits[i + 1:])

    return int(''.join(digits))


# Example usage:
print(permutationStep(12))    # 21
print(permutationStep(513))   # 531
print(permutationStep(2017))  # 2071
print(permutationStep(9))     # -1
print(permutationStep(111))   # -1
