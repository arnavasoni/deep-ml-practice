def poly_term_derivative(c: float, x: float, n: float) -> float:
    # Your code here
    # c is coefficient
    # x is the variable
    # n is the power

    # provided polynomial term: c*x**(n)
    return c * n * x ** (n-1) # the derivative of the polynomial