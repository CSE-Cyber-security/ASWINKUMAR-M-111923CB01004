"""Print the Fibonacci series for a requested number of terms."""

def fibonacci_series(n: int) -> list[int]:
    """Return the first n terms of the Fibonacci series."""
    if n < 0:
        raise ValueError("Number of terms cannot be negative.")

    series = []
    first, second = 0, 1

    for _ in range(n):
        series.append(first)
        first, second = second, first + second

    return series


def main() -> None:
    try:
        terms = int(input("Enter the number of terms: "))
        if terms < 0:
            print("Please enter a non-negative integer.")
            return

        result = fibonacci_series(terms)
        print("Fibonacci series:")
        print(" ".join(map(str, result)) if result else "(empty series)")
    except ValueError:
        print("Invalid input. Please enter a whole number.")


if __name__ == "__main__":
    main()
