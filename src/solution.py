def sort(width: float, height: float, length: float, mass: float) -> str:
    """
    Determines the stack category for a package.

    Args:
        width (float): Width in centimeters (> 0)
        height (float): Height in centimeters (> 0)
        length (float): Length in centimeters (> 0)
        mass (float): Mass in kilograms (> 0)

    Returns:
        str: "STANDARD", "SPECIAL", or "REJECTED"

    Raises:
        ValueError: If any dimension or mass is <= 0
    """

    # Initialize variables
    is_bulky = False
    is_heavy = False

    # Cannot have negative dimensions or mass
    if width <= 0 or height <= 0 or length <= 0 or mass <= 0:
        raise ValueError("Dimensions and mass must be non-negative integers.")

    # Calculate the volume in cubic centimeters
    volume = width * height * length

    if volume >= 1000000 or width >= 150 or height >= 150 or length >= 150:
        is_bulky = True

    if mass >= 20:
        is_heavy = True

    # Determine the stack based on the conditions
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"

    return "STANDARD"



