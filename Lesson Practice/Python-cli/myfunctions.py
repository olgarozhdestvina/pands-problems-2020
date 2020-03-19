# Olga Rozhdestvina
# Calculate the factorial of a number

def factorial(n):
    """ Returns the factorial of n.
    e.g. factorial(7) = 7x6x5x4x3x2x1 = 5040
    """
    answer = 1
    for i in range(n, 1, -1):
        answer = answer * i
    return answer
if __name__ == "__main__":
    assert factorial(7) == 5040
    assert factorial(1) == 1