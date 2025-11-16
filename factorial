def run_tests():
    test_cases = [
        (1, 1),
        (2, 2),
        (3, 6),
        (5, 120),
        (10, 3628800),
    ]
    for n, expected in test_cases:
        result = factorial(n)
        assert result == expected, f"FAILED: factorial({n}) != {result}, expected {expected}"
    print("✅ All tests passed!")

MAX_N = 100
cache = [1]*(MAX_N+1)
max_computed_n = 1

def factorial(n):
    """
    factorial(n) = n*(n-1)*(n-2)*....*1
    factorial(n) = n*factorial(n-1)
    factorial(n-1) = (n-1)*factorial(n-2)

    2*3 = 3+3
    n*(n-1)*(n-2) = (n-1) + (n-1) 
    """
    # recursive solution not optimized - Time O(n), Space O(n)
    # if n == 1:
    #     return output
    # else:
    #     return n*factorial(n-1)

    # for loop - Time O(n), Space O(1)
    # for idx in range(2, n+1):
    #     for _ in range(output):
    #         output += idx - 1
    # return output 

    # DP Memoization 

    # outputList = [1, 2, 6, 24, ...,]
    global max_computed_n

    if n < max_computed_n:
        return cache[n]   
    else:
        for idx in range(max_computed_n, n+1):
            print("here", idx)
            cache[idx] = cache[idx-1] * idx
            max_computed_n = idx
        return cache[n]            


if __name__ == "__main__":
    run_tests()

