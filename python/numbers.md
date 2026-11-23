# Python Numbers & Formatting

## 1. Integers vs. Floats
- **Integers (`int`)**: Whole numbers (10, -5, 0).
- **Floats (`float`)**: Numbers with decimals (3.14, -0.5).
- **Mixing:** Adding an `int` and a `float` results in a `float`.

## 2. Math Operators
- **Floor Division (`//`)**: Divides and returns the greatest integer (e.g., `7 // 2` = `3`).
- **Exponentiation (`**`)**: Raises to a power (e.g., `2 ** 3` = `8`).

## 3. Math Functions
- **`round(number, decimals)`**: Rounds a number. `round(12.5, 2)` returns `12.5`.
- **`abs(number)`**: Returns the absolute (positive) value.
- **`pow(number, power)`**: Raises a number to a power.

## 4. F-String Number Formatting
- **Syntax:** `f"{value:.2f}"`
- **Breakdown:**
  - `:` introduces the format.
  - `.2` sets two decimal places.
  - `f` means fixed-point notation.
- **Example:** `value = 12.5` -> `f"{value:.2f}"` displays `12.50`. The original `value` is still `12.5`.
- **Difference from `round()`:** `round()` returns a number (no trailing zeros). `:.2f` returns a string (always shows two decimal places).
