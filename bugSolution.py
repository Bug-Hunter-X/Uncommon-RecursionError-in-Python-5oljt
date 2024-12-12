def function_with_uncommon_error_solution(x, depth=0):
    if depth > 1000:  # Setting a recursion depth limit
        raise RecursionError("Maximum recursion depth exceeded")
    if x == 0:
        return 1
    else:
        return x / function_with_uncommon_error_solution(x - 1, depth + 1)

# Example usage (safe):
print(function_with_uncommon_error_solution(5))