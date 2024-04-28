import math
import tabulate
from misc import input_x

def factorial(n):
    """
    Calculate the factorial of a non-negative integer.

    Parameters:
    n (int): The number for which factorial is to be calculated.

    Returns:
    int: The factorial of the given number.

    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def power_series_arcsin(x, eps=1e-6, max_iter=500):
    """
    Calculates the power series approximation of the arcsin function.

    Parameters:
    x (float): The value for which to calculate the arcsin.
    eps (float, optional): The desired accuracy of the approximation. Defaults to 1e-6.
    max_iter (int, optional): The maximum number of iterations to perform. Defaults to 500.

    Returns:
    tuple: A tuple containing the approximation result and a table of intermediate results.

    Raises:
    ValueError: If the absolute value of x is greater than or equal to 1.
    """

    result = 0
    n = 0
    table = []

    while n < max_iter:
        term = (factorial(2*n) / (4**n * (factorial(n))**2)) * (x**(2*n+1) / (2*n+1))
        result += term
        table.append([n, result])

        if abs(term) < eps:
            break

        n += 1

    return result, table

def arsin_series():
    """
    Calculates the arcsine of a given value using a power series approximation.

    This function prompts the user to enter a value for `x` (where abs(x) < 1) and a value for the precision `eps`.
    It then calculates the arcsine of `x` using a power series approximation with the given precision.
    The result is compared with the `math.asin` function and displayed along with the number of terms used in the calculation.

    Returns:
        None
    """
    x = input_x()
    eps = float(input("Enter a value for the precision (eps): "))

    result, table = power_series_arcsin(x, eps)

    # Compare with math.asin
    math_asin = math.asin(x)
    print("The value of arcsin({}) using math.asin is {}".format(x, math_asin))
    print("The value of arcsin({}) is approximately {}".format(x, result))
    print("The calculation required {} terms".format(len(table)))

    # Add x, math.asin and eps to each row in the table
    for row in table:
        row.insert(0, x)
        row.append(math_asin)
        row.append(eps)

    print(tabulate.tabulate(table, headers=["x", "Term", "Value", "math.asin", "eps"], tablefmt="grid"))
