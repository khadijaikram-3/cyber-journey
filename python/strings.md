# Python Strings (Day 2)

## 1. Basics of Strings
- Created using single (`' '`) or double (`" "`) quotes.
- **Multiline strings:** Created using triple quotes (`''' '''` or `""" """`).
- **Escape Sequences:** Used for characters hard to type directly.
  - `\n`: Newline
  - `\t`: Tab
  - `\\`: Single backslash
- **The `in` operator:** Checks if a string contains specific characters.
  - `print('Hello' in 'Hello world')` -> `True`

## 2. Indexing and Slicing
- Strings are **immutable** (cannot be changed in place, only reassigned).
- **Length:** `len(my_str)`
- **Indexing:** Zero-based (starts at 0). Negative indexing starts from the end (`-1` is the last character).
- **Slicing:** `string[start:stop:step]`
  - Stop index is non-inclusive.
  - To reverse a string: `my_str[::-1]`

## 3. String Operations
- **Concatenation:** `name + age_str` (Cannot concatenate a string with an integer directly; must use `str()`).
- **Repetition:** `"A" * 3` -> `"AAA"`.

## 4. String Interpolation (f-strings)
- The modern way to insert variables into strings.
- Prefix the string with `f` and use curly braces `{}`.
  - `name = "John"`
  - `print(f"My name is {name}")` -> `My name is John`

## 5. String Methods
- `.upper()`: Uppercases all letters.
- `.lower()`: Lowercases all letters.
- `.strip()`: Removes leading/trailing whitespace.
- `.replace(old, new)`: Replaces a substring.
- `.split(separator)`: Splits a string into a list.
- `.join(collection)`: Joins a list into a string.
- `.startswith(prefix)` / `.endswith(suffix)`: Returns a boolean.
- `.find(substring)`: Returns the index of the first occurrence (or `-1`).
- `.count(substring)`: Returns the number of occurrences.
- `.capitalize()`: Capitalizes the first character and lowercases the rest.
- `.isupper()` / `.islower()`: Returns a boolean if all cased characters are upper/lowercase.
- `.title()`: Capitalizes the first letter of each word.
