def sum(a, b):
    """
    A simple function to add two numbers.
    
    Args:
        a (float): First number
        b (float): Second number
        
    Returns:
        float: The sum of a and b
    """
    return a + b


def main():
    """
    Demonstrate the sum function.
    """
    rint("Demonstrating sum function:")
    print(f"5 + 3 = {sum(5, 3)}")
    print(f"10.5 + 2.7 = {sum(10.5, 2.7)}")
    print(f"-1 + 5 = {sum(-1, 5)}")


if __name__ == "__main__":
    main()