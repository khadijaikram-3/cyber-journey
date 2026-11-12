# Python Basics - Day 1

## Why Python in Cybersecurity?
- Automating repetitive tasks (e.g., extracting data, managing files).
- Building custom security tools (e.g., port scanners, brute-forcers).
- Analyzing threats and processing logs.
- Detecting vulnerabilities.

## 1. Variables and Naming
- Variables are used to store data.
- **Snake Case:** Variable names should be lowercase, with words separated by an underscore (e.g., `my_integer_var`).
- **Comments:** Start with a `#`. The computer ignores them. They are for human readers.

## 2. The `print()` Function
- Outputs text or variables to the screen.
- When separating multiple items with a comma, Python automatically adds a space.
- Example: `print("Hello", "World")` outputs `Hello World`.

## 3. Data Types
Python has four main data types you will use constantly:
1. **Integer (`int`)**: A whole number without decimals (e.g., 10, -5).
2. **Float (`float`)**: A number with a decimal point (e.g., 4.50, -0.4).
3. **String (`str`)**: A sequence of characters enclosed in single or double quotes (e.g., 'hello', "world").
4. **Boolean (`bool`)**: Represents True or False.

## 4. Checking Data Types: type() and isinstance()
Sometimes you need to verify what type of data a variable is holding before performing operations on it.

- **type(variable):** Tells you exactly what the data type is.
- **isinstance(variable, data_type):** Returns True or False based on whether the variable matches the specified type.
