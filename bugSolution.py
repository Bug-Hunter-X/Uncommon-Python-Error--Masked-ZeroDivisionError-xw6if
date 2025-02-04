def function_with_uncommon_error_solution(a, b):
    if a == 0:
        return float('inf')  # Or handle as appropriate, raising an exception or returning a specific value
    else:
        return a + b