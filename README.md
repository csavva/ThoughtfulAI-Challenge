# Package Sorting Function

## Objective
This repository contains a Python implementation of a function that determines which stack a package should be dispatched to based on its **dimensions** and **mass**, following Thoughtful’s robotic automation factory rules.

## Rules

A package is **bulky** if:
- Its volume (`width × height × length`) is **≥ 1,000,000 cm³**, OR
- Any single dimension is **≥ 150 cm**

A package is **heavy** if:
- Its mass is **≥ 20 kg**

Stacks:
- **STANDARD** → Not bulky and not heavy
- **SPECIAL** → Bulky **or** heavy (but not both)
- **REJECTED** → Bulky **and** heavy

## Function

```python
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
```

### Example Usage

```python

from solution import sort

print(sort(100, 100, 100, 10))  # SPECIAL (bulky by volume)
print(sort(10, 10, 10, 1))      # STANDARD
print(sort(150, 10, 10, 20))    # REJECTED
```

## Tests

Tests are written using **pytest** and are located in `test_sort.py`.

### Run tests
```bash
pip install -r requirements.txt
pytest
```

### Check coverage
```bash
pytest --cov=solution --cov-report=term-missing
```

### Example coverage output
```
Name                 Stmts   Miss  Cover   Missing
--------------------------------------------------
server/solution.py      15      0   100%
--------------------------------------------------
TOTAL                   15      0   100%
```

## Project Structure
```
.
├── README.md
├── requirements.txt
├── solution.py
├── test_sort.py
└── .gitignore
```

## Requirements
- Python 3.8+
- pytest
- pytest-cov

Install dependencies using:
```bash
pip install -r requirements.txt
```

## Author
Christos Savva - 8 August 2025