def fibonacci(n):
    """
    Calculate the nth Fibonacci number using recursion.

    Args:
        n (int): The position in the Fibonacci sequence (0-indexed)

    Returns:
        int: The nth Fibonacci number

    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    # Test the function with some values
    test_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print("Fibonacci sequence:")
    for i in test_values:
        result = fibonacci(i)
        print(f"F({i}) = {result}")
