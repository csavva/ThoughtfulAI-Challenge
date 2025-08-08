


def sort(width: int, height: int, length: int, mass: int) -> str:
    """
    Provides the name of the stack where a package should go based on its dimensions and mass.

    Args:
        width (int): The width of the item in centimeters.
        height (int): The height of the item in centimeters.
        length (int): The length of the item in centimeters.
        mass (int): The mass of the item in kilograms.

    Returns:
        str: The name of the stack where the package should go.
    """

    # Initialize variables
    is_bulky = False
    is_heavy = False

    # Cannot have negative dimensions or mass
    if width < 0 or height < 0 or length < 0 or mass < 0:
        raise ValueError("Dimensions and mass must be non-negative integers.")

    # Calculate the volume in cubic centimeters
    volume = width * height * length

    if volume > 1000000:
        is_bulky = True

    if mass > 20:
        is_heavy = True

    # Determine the stack based on the conditions
    if is_bulky and is_heavy:
        stack_name = "REJECTED"
    elif is_bulky or is_heavy:
        stack_name = "SPECIAL"
    else:
        stack_name = "STANDARD"

    return stack_name


