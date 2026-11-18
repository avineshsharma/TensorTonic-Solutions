
def dot_product(x: list, y: list) -> float:

    if len(x) != len(y):
        raise ValueError("Both lists must have the same length")
    result = 0

    for i in range(len(x)):
        result += x[i] * y[i]

    return float(result)
